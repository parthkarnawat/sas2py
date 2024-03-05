import sys 
import os
sys.path.append(os.path.abspath("./sd2pq"))
import dtm_fmts

import pyarrow as pa
import pyarrow.csv as csv
import pyarrow.parquet as pq

import fsspec
from fsspec import gui

import logging
logger = logging.getLogger('sd2pq')

def get_metadata(session,table: str, libref: str =''):
    # getting the one level or two level sas datasets reference
    if libref:
        tabname = libref+".'"+table.strip().replace("'", "''")+"'n "
    else:
        tabname = "'"+table.strip().replace("'", "''")+"'n "

    code_get_meta = '''
    data work.sasdata2dataframe / view=work.sasdata2dataframe;
        set {tabname};
        length "trial 1'"n 8;
    run;

    data _null_;
        file LOG;
        d = open('work.sasdata2dataframe');
        length var $256;

        put "_metadata_start";
        *Get Dataset Info;
        lr='LRECL='; vn='VARNUMS=';
        lrecl = attrn(d, 'LRECL');
        nvars = attrn(d, 'NVARS');
        put lr lrecl; put vn nvars;

        *Get Column Info;
        vl='VARNAME='; vt='VARTYPE='; ln='VARLEN='; ll='VARLABEL='; vf='VARFMT='; vi='VARINFMT=';
        put vl;
        do i = 1 to nvars;
            var = compress(varname(d, i), '00'x);
            put var;
        end;
        put vt;
        do i = 1 to nvars;
            var = vartype(d, i);
            put var;
        end;
        put ln;
        do i = 1 to nvars;
            var = varlen(d, i);
            put var;
        end;
        put ll;
        do i = 1 to nvars;
            var = varlabel(d, i);
            put var;
        end;
        put vf;
        do i = 1 to nvars;
            var = varfmt(d, i);
            put var;
        end;
        put vi;
        do i = 1 to nvars;
            var = varinfmt(d, i);
            put var;
        end;
        put "_metadata_end";
    run;
    '''

    # getting the sas dataset metadata
    code_get_meta = code_get_meta.format(tabname=tabname)
    ll = session.submit(code_get_meta, "text")

    try:
        l2 = ll['LOG'].rpartition("_metadata_start")
        # print(lrecl)

        dataset_metadata = {}
        dataset_attributes = ("lrecl","varnums")

        for i in dataset_attributes:
            l2 = ll['LOG'].partition(i.upper()+"= ")
            l2 = l2[2].partition("\n")
            dataset_metadata[i] = int(l2[0])
            # print(dataset_metadata[i])

        nvars = dataset_metadata['varnums']
        l2 = l2[2].partition("VARNAME=")
        l2 = l2[2].partition("\n")
        varname = l2[2].split("\n", nvars)
        del varname[nvars]
        # print(varname)

        columns_metadata = {}
        column_attributes = ("vartype","varlen","varlabel","varfmt","varinfmt")
        for i in column_attributes:
            l2 = l2[2].partition(i.upper()+"=")
            l2 = l2[2].partition("\n")
            columns_metadata[i] = l2[2].split("\n", nvars)
            del columns_metadata[i][nvars]
            # print(columns_metadata[i])
        
        varlist = list(varname)
        #print(dvarlist)
        for i in range(len(varlist)):
            varlist[i] = varlist[i].replace("'", "''") # Treatement to take care of single quotes in extended column names

    except Exception as e:
        logger.error("Invalid output produced during sd2csv metadata retireval step. Step failed.\
        \nPrinting the error: {}\nPrinting the SASLOG as diagnostic\n{}".format(str(e), ll['LOG']))
        return None

    code_get_meta  = "proc delete data=work.sasdata2dataframe(memtype=view);run;\n"
    code_get_meta += "data work._n_u_l_l_;output;run;\n"
    code_get_meta += "data _null_; set work._n_u_l_l_ "+tabname+";put 'FMT_CATS=';\n"

    for i in range(nvars):
        code_get_meta += "_tom = vformatn('"+varlist[i]+"'n);put _tom;\n"
    code_get_meta += "stop;\nrun;\nproc delete data=work._n_u_l_l_;run;"

    ll = session.submit(code_get_meta, "text")

    try:
        column_attributes += ("varfmt_name",)
        l2 = ll['LOG'].rpartition("FMT_CATS=")
        l2 = l2[2].partition("\n")
        columns_metadata['varfmt_name'] = l2[2].split("\n", nvars)
        del columns_metadata['varfmt_name'][nvars]
        # print(varcat)
    except Exception as e:
        logger.error("Invalid output produced during sd2csv variable format category retireval step. Step failed.\
        \nPrinting the error: {}\nPrinting the SASLOG as diagnostic\n{}".format(str(e), ll['LOG']))
        return None
    metadata = {'dataset': dataset_metadata, 'columns': { varlist[i] : { j : columns_metadata[j][i] for j in column_attributes} for i in range(nvars) }}
    return (metadata)
def get_arrow_schema(sas_metadata):
    column_metadata = sas_metadata['columns']

    dts = {}
    for key,val in column_metadata.items():
        if val['vartype'] == 'N':
            if val['varfmt_name'] not in dtm_fmts.sas_date_fmts + dtm_fmts.sas_time_fmts + dtm_fmts.sas_datetime_fmts:
                dts[key] = pa.float64()
            elif val['varfmt_name'] in dtm_fmts.sas_date_fmts:
                dts[key] = pa.string()
            elif val['varfmt_name'] in dtm_fmts.sas_time_fmts:
                dts[key] = pa.string()
            elif val['varfmt_name'] in dtm_fmts.sas_datetime_fmts:
                dts[key] = pa.string()
        else:
            dts[key] = pa.string()
    
    columns = []
    for key in column_metadata:
        columns.append(pa.field(key, dts[key], metadata=column_metadata[key]))
    schema = pa.schema(columns, metadata={ str(key) : str(val) for key,val in sas_metadata['dataset'].items()})
    # print(schema)
    return schema
def write_csv(session, csvfile, table, libref):

    metadata = get_metadata(session, table, libref)

    if libref:
        tabname = libref+".'"+table.strip().replace("'", "''")+"'n "
    else:
        tabname = "'"+table.strip().replace("'", "''")+"'n "

    code_write_csv = "data work.sasdata2dataframe / view=work.sasdata2dataframe; set "+tabname+";\nformat "

    column_metadata = metadata['columns']
    for key, val in column_metadata.items():
        if val['vartype'] == 'N':
            code_write_csv += "'"+key.replace("'", "''")+"'n "
            if val['varfmt_name'] in dtm_fmts.sas_date_fmts:
                code_write_csv += 'E8601DA10. '
            else:
                if val['varfmt_name'] in dtm_fmts.sas_time_fmts:
                    code_write_csv += 'E8601TM15.6 '
                else:
                    if val['varfmt_name'] in dtm_fmts.sas_datetime_fmts:
                        code_write_csv += 'E8601DT26.6 '
                    else:
                        code_write_csv += 'best32. '
    code_write_csv += ";\n run;\n"
    ll = session.submit(code_write_csv, "text")

    outname = "_tomodsx"
    code_write_csv    = "filename _tomodsx '"+csvfile+"' lrecl="+str(1048576)+" recfm=v  encoding='utf-8';\n"
    # TODO: try optimizing lrecl for highest performance

    code_write_csv += "proc export data=work.sasdata2dataframe outfile="+outname+" dbms=csv replace;\n"
    code_write_csv += " run;\n"
    code_write_csv += "proc delete data=work.sasdata2dataframe(memtype=view);run;\n"
    code_write_csv += "filename _tomodsx;"

    ll = session.submit(code_write_csv, 'text')
    # print(ll['LOG'])
def write_parquet(session, table, libref):
    write_csv(session, r'C:\Users\2004999\My Data\trial\Data\sd2csv.csv', table, libref)
    schema = get_arrow_schema(get_metadata(sas_session, table, libref))

    # Define the file path of the large CSV file
    file_path = '.\Data\sd2csv.csv'

    # Define options for multithreading and batched reading
    read_options = csv.ReadOptions(block_size=512 * 2**20)  # Set block size = 512 MB 
    parse_options = csv.ParseOptions() #set delimiter and invald row handler
    convert_options = csv.ConvertOptions(column_types=schema)  # Define column data types if needed

    with csv.open_csv(file_path, read_options=read_options, parse_options=parse_options,convert_options=convert_options) as scanner:
        with pq.ParquetWriter('sd2csv.parquet', scanner.schema) as writer:
            for batch in scanner:
                writer.write_batch(batch)

import saspy
sas_session = saspy.SASsession(cfgname='local_com')

import os
dataset_path = r"your_dataset_path"
dataset_name = os.path.basename(dataset_path).split('.')[0]
dataset_directory = os.path.dirname(dataset_path)
sas_session.saslib('mylib', path=dataset_directory)
write_parquet(sas_session, dataset_name, 'mylib')
