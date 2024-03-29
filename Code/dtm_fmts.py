sas_date_fmts = (
    'AFRDFDD', 'AFRDFDE', 'AFRDFDE', 'AFRDFDN', 'AFRDFDWN', 'AFRDFMN', 'AFRDFMY', 'AFRDFMY', 'AFRDFWDX', 'AFRDFWKX',
    'ANYDTDTE', 'B8601DA', 'B8601DA', 'B8601DJ', 'CATDFDD', 'CATDFDE', 'CATDFDE', 'CATDFDN', 'CATDFDWN', 'CATDFMN',
    'CATDFMY', 'CATDFMY', 'CATDFWDX', 'CATDFWKX', 'CRODFDD', 'CRODFDE', 'CRODFDE', 'CRODFDN', 'CRODFDWN', 'CRODFMN',
    'CRODFMY', 'CRODFMY', 'CRODFWDX', 'CRODFWKX', 'CSYDFDD', 'CSYDFDE', 'CSYDFDE', 'CSYDFDN', 'CSYDFDWN', 'CSYDFMN',
    'CSYDFMY', 'CSYDFMY', 'CSYDFWDX', 'CSYDFWKX', 'DANDFDD', 'DANDFDE', 'DANDFDE', 'DANDFDN', 'DANDFDWN', 'DANDFMN',
    'DANDFMY', 'DANDFMY', 'DANDFWDX', 'DANDFWKX', 'DATE', 'DATE', 'DAY', 'DDMMYY', 'DDMMYY', 'DDMMYYB', 'DDMMYYC',
    'DDMMYYD', 'DDMMYYN', 'DDMMYYP', 'DDMMYYS', 'DESDFDD', 'DESDFDE', 'DESDFDE', 'DESDFDN', 'DESDFDWN', 'DESDFMN',
    'DESDFMY', 'DESDFMY', 'DESDFWDX', 'DESDFWKX', 'DEUDFDD', 'DEUDFDE', 'DEUDFDE', 'DEUDFDN', 'DEUDFDWN', 'DEUDFMN',
    'DEUDFMY', 'DEUDFMY', 'DEUDFWDX', 'DEUDFWKX', 'DOWNAME', 'E8601DA', 'E8601DA', 'ENGDFDD', 'ENGDFDE', 'ENGDFDE',
    'ENGDFDN', 'ENGDFDWN', 'ENGDFMN', 'ENGDFMY', 'ENGDFMY', 'ENGDFWDX', 'ENGDFWKX', 'ESPDFDD', 'ESPDFDE', 'ESPDFDE',
    'ESPDFDN', 'ESPDFDWN', 'ESPDFMN', 'ESPDFMY', 'ESPDFMY', 'ESPDFWDX', 'ESPDFWKX', 'EURDFDD', 'EURDFDE', 'EURDFDE',
    'EURDFDN', 'EURDFDWN', 'EURDFMN', 'EURDFMY', 'EURDFMY', 'EURDFWDX', 'EURDFWKX', 'FINDFDD', 'FINDFDE', 'FINDFDE',
    'FINDFDN', 'FINDFDWN', 'FINDFMN', 'FINDFMY', 'FINDFMY', 'FINDFWDX', 'FINDFWKX', 'FRADFDD', 'FRADFDE', 'FRADFDE',
    'FRADFDN', 'FRADFDWN', 'FRADFMN', 'FRADFMY', 'FRADFMY', 'FRADFWDX', 'FRADFWKX', 'FRSDFDD', 'FRSDFDE', 'FRSDFDE',
    'FRSDFDN', 'FRSDFDWN', 'FRSDFMN', 'FRSDFMY', 'FRSDFMY', 'FRSDFWDX', 'FRSDFWKX', 'HUNDFDD', 'HUNDFDE', 'HUNDFDE',
    'HUNDFDN', 'HUNDFDWN', 'HUNDFMN', 'HUNDFMY', 'HUNDFMY', 'HUNDFWDX', 'HUNDFWKX', 'IS8601DA', 'IS8601DA', 'ITADFDD',
    'ITADFDE', 'ITADFDE', 'ITADFDN', 'ITADFDWN', 'ITADFMN', 'ITADFMY', 'ITADFMY', 'ITADFWDX', 'ITADFWKX', 'JDATEMD',
    'JDATEMDW', 'JDATEMNW', 'JDATEMON', 'JDATEQRW', 'JDATEQTR', 'JDATESEM', 'JDATESMW', 'JDATEWK', 'JDATEYDW', 'JDATEYM',
    'JDATEYMD', 'JDATEYMD', 'JDATEYMW', 'JNENGO', 'JNENGO', 'JNENGOW', 'JULDATE', 'JULDAY', 'JULIAN', 'JULIAN', 'MACDFDD',
    'MACDFDE', 'MACDFDE', 'MACDFDN', 'MACDFDWN', 'MACDFMN', 'MACDFMY', 'MACDFMY', 'MACDFWDX', 'MACDFWKX', 'MINGUO',
    'MINGUO', 'MMDDYY', 'MMDDYY', 'MMDDYYB', 'MMDDYYC', 'MMDDYYD', 'MMDDYYN', 'MMDDYYP', 'MMDDYYS', 'MMYY', 'MMYYC',
    'MMYYD', 'MMYYN', 'MMYYP', 'MMYYS', 'MONNAME', 'MONTH', 'MONYY', 'MONYY', 'ND8601DA', 'NENGO', 'NENGO', 'NLDATE',
    'NLDATE', 'NLDATEL', 'NLDATEM', 'NLDATEMD', 'NLDATEMDL', 'NLDATEMDM', 'NLDATEMDS', 'NLDATEMN', 'NLDATES', 'NLDATEW',
    'NLDATEW', 'NLDATEWN', 'NLDATEYM', 'NLDATEYML', 'NLDATEYMM', 'NLDATEYMS', 'NLDATEYQ', 'NLDATEYQL', 'NLDATEYQM',
    'NLDATEYQS', 'NLDATEYR', 'NLDATEYW', 'NLDDFDD', 'NLDDFDE', 'NLDDFDE', 'NLDDFDN', 'NLDDFDWN', 'NLDDFMN', 'NLDDFMY',
    'NLDDFMY', 'NLDDFWDX', 'NLDDFWKX', 'NORDFDD', 'NORDFDE', 'NORDFDE', 'NORDFDN', 'NORDFDWN', 'NORDFMN', 'NORDFMY',
    'NORDFMY', 'NORDFWDX', 'NORDFWKX', 'POLDFDD', 'POLDFDE', 'POLDFDE', 'POLDFDN', 'POLDFDWN', 'POLDFMN', 'POLDFMY',
    'POLDFMY', 'POLDFWDX', 'POLDFWKX', 'PTGDFDD', 'PTGDFDE', 'PTGDFDE', 'PTGDFDN', 'PTGDFDWN', 'PTGDFMN', 'PTGDFMY',
    'PTGDFMY', 'PTGDFWDX', 'PTGDFWKX', 'QTR', 'QTRR', 'RUSDFDD', 'RUSDFDE', 'RUSDFDE', 'RUSDFDN', 'RUSDFDWN', 'RUSDFMN',
    'RUSDFMY', 'RUSDFMY', 'RUSDFWDX', 'RUSDFWKX', 'SLODFDD', 'SLODFDE', 'SLODFDE', 'SLODFDN', 'SLODFDWN', 'SLODFMN',
    'SLODFMY', 'SLODFMY', 'SLODFWDX', 'SLODFWKX', 'SVEDFDD', 'SVEDFDE', 'SVEDFDE', 'SVEDFDN', 'SVEDFDWN', 'SVEDFMN',
    'SVEDFMY', 'SVEDFMY', 'SVEDFWDX', 'SVEDFWKX', 'WEEKDATE', 'WEEKDATX', 'WEEKDAY', 'WEEKU', 'WEEKU', 'WEEKV', 'WEEKV',
    'WEEKW', 'WEEKW', 'WORDDATE', 'WORDDATX', 'XYYMMDD', 'XYYMMDD', 'YEAR', 'YYMM', 'YYMMC', 'YYMMD', 'YYMMDD', 'YYMMDD',
    'YYMMDDB', 'YYMMDDC', 'YYMMDDD', 'YYMMDDN', 'YYMMDDP', 'YYMMDDS', 'YYMMN', 'YYMMN', 'YYMMP', 'YYMMS', 'YYMON', 'YYQ',
    'YYQ', 'YYQC', 'YYQD', 'YYQN', 'YYQP', 'YYQR', 'YYQRC', 'YYQRD', 'YYQRN', 'YYQRP', 'YYQRS', 'YYQS', 'YYQZ', 'YYQZ',
    'YYWEEKU', 'YYWEEKV', 'YYWEEKW',
)

sas_time_fmts = (
    'ANYDTTME', 'B8601LZ', 'B8601LZ', 'B8601TM', 'B8601TM', 'B8601TZ', 'B8601TZ', 'E8601LZ', 'E8601LZ', 'E8601TM',
    'E8601TM', 'E8601TZ', 'E8601TZ', 'HHMM', 'HOUR', 'IS8601LZ', 'IS8601LZ', 'IS8601TM', 'IS8601TM', 'IS8601TZ',
    'IS8601TZ', 'JTIMEH', 'JTIMEHM', 'JTIMEHMS', 'JTIMEHW', 'JTIMEMW', 'JTIMESW', 'MMSS', 'ND8601TM', 'ND8601TZ',
    'NLTIMAP', 'NLTIMAP', 'NLTIME', 'NLTIME', 'STIMER', 'TIME', 'TIMEAMPM', 'TOD',
)

sas_datetime_fmts = (
    'AFRDFDT', 'AFRDFDT', 'ANYDTDTM', 'B8601DN', 'B8601DN', 'B8601DT', 'B8601DT', 'B8601DZ', 'B8601DZ', 'CATDFDT',
    'CATDFDT', 'CRODFDT', 'CRODFDT', 'CSYDFDT', 'CSYDFDT', 'DANDFDT', 'DANDFDT', 'DATEAMPM', 'DATETIME', 'DATETIME',
    'DESDFDT', 'DESDFDT', 'DEUDFDT', 'DEUDFDT', 'DTDATE', 'DTMONYY', 'DTWKDATX', 'DTYEAR', 'DTYYQC', 'E8601DN',
    'E8601DN', 'E8601DT', 'E8601DT', 'E8601DZ', 'E8601DZ', 'ENGDFDT', 'ENGDFDT', 'ESPDFDT', 'ESPDFDT', 'EURDFDT',
    'EURDFDT', 'FINDFDT', 'FINDFDT', 'FRADFDT', 'FRADFDT', 'FRSDFDT', 'FRSDFDT', 'HUNDFDT', 'HUNDFDT', 'IS8601DN',
    'IS8601DN', 'IS8601DT', 'IS8601DT', 'IS8601DZ', 'IS8601DZ', 'ITADFDT', 'ITADFDT', 'JDATEYT', 'JDATEYTW', 'JNENGOT',
    'JNENGOTW', 'MACDFDT', 'MACDFDT', 'MDYAMPM', 'MDYAMPM', 'ND8601DN', 'ND8601DT', 'ND8601DZ', 'NLDATM', 'NLDATM',
    'NLDATMAP', 'NLDATMAP', 'NLDATMDT', 'NLDATML', 'NLDATMM', 'NLDATMMD', 'NLDATMMDL', 'NLDATMMDM', 'NLDATMMDS',
    'NLDATMMN', 'NLDATMS', 'NLDATMTM', 'NLDATMTZ', 'NLDATMW', 'NLDATMW', 'NLDATMWN', 'NLDATMWZ', 'NLDATMYM', 'NLDATMYML',
    'NLDATMYMM', 'NLDATMYMS', 'NLDATMYQ', 'NLDATMYQL', 'NLDATMYQM', 'NLDATMYQS', 'NLDATMYR', 'NLDATMYW', 'NLDATMZ',
    'NLDDFDT', 'NLDDFDT', 'NORDFDT', 'NORDFDT', 'POLDFDT', 'POLDFDT', 'PTGDFDT', 'PTGDFDT', 'RUSDFDT', 'RUSDFDT',
    'SLODFDT', 'SLODFDT', 'SVEDFDT', 'SVEDFDT', 'TWMDY', 'YMDDTTM',
)

sas_encoding_mapping = {
'arabic':      [1, 'iso8859_6', 'iso-8859-6', 'arabic'],
'big5':        [2, 'big5', 'big5-tw', 'csbig5'],
'cyrillic':    [1, 'iso8859_5', 'iso-8859-5', 'cyrillic'],
'ebcdic037':   [1, 'cp037', 'ibm037', 'ibm039'],
'ebcdic273':   [1, 'cp273', '273', 'ibm273', 'csibm273'],
'ebcdic500':   [1, 'cp500', 'ebcdic-cp-be', 'ebcdic-cp-ch', 'ibm500'],
'euc-cn':      [2, 'gb2312', 'chinese', 'csiso58gb231280', 'euc-cn', 'euccn', 'eucgb2312-cn', 'gb2312-1980', 'gb2312-80', 'iso-ir-58'],
'euc-jp':      [4, 'euc_jis_2004', 'jisx0213', 'eucjis2004'],
'euc-kr':      [4, 'euc_kr', 'euckr', 'korean', 'ksc5601', 'ks_c-5601', 'ks_c-5601-1987', 'ksx1001', 'ks_x-1001'],
'greek':       [1, 'iso8859_7', 'iso-8859-7', 'greek', 'greek8'],
'hebrew':      [1, 'iso8859_8', 'iso-8859-8', 'hebrew'],
'ibm-949':     [1, 'cp949', '949', 'ms949', 'uhc'],
'kz1048':      [1, 'kz1048', 'kz_1048', 'strk1048_2002', 'rk1048'],
'latin10':     [1, 'iso8859_16', 'iso-8859-16', 'latin10', 'l10'],
'latin1':      [1, 'latin_1', 'iso-8859-1', 'iso8859-1', '8859', 'cp819', 'latin', 'latin1', 'l1'],
'latin2':      [1, 'iso8859_2', 'iso-8859-2', 'latin2', 'l2'],
'latin3':      [1, 'iso8859_3', 'iso-8859-3', 'latin3', 'l3'],
'latin4':      [1, 'iso8859_4', 'iso-8859-4', 'latin4', 'l4'],
'latin5':      [1, 'iso8859_9', 'iso-8859-9', 'latin5', 'l5'],
'latin6':      [1, 'iso8859_10', 'iso-8859-10', 'latin6', 'l6'],
'latin7':      [1, 'iso8859_13', 'iso-8859-13', 'latin7', 'l7'],
'latin8':      [1, 'iso8859_14', 'iso-8859-14', 'latin8', 'l8'],
'latin9':      [1, 'iso8859_15', 'iso-8859-15', 'latin9', 'l9'],
'ms-932':      [2, 'cp932', '932', 'ms932', 'mskanji', 'ms-kanji'],
'msdos737':    [1, 'cp737'],
'msdos775':    [1, 'cp775', 'ibm775'],
'open_ed-1026':[1, 'cp1026', 'ibm1026'],
'open_ed-1047':[1, 'cp1047'],              # Though this isn't available in base python, it's 3rd party
'open_ed-1140':[1, 'cp1140', 'ibm1140'],
'open_ed-424': [1, 'cp424', 'ebcdic-cp-he', 'ibm424'],
'open_ed-875': [1, 'cp875'],
'pcoem437':    [1, 'cp437', '437', 'ibm437'],
'pcoem850':    [1, 'cp850', '850', 'ibm850'],
'pcoem852':    [1, 'cp852', '852', 'ibm852'],
'pcoem857':    [1, 'cp857', '857', 'ibm857'],
'pcoem858':    [1, 'cp858', '858', 'ibm858'],
'pcoem860':    [1, 'cp860', '860', 'ibm860'],
'pcoem862':    [1, 'cp862', '862', 'ibm862'],
'pcoem863':    [1, 'cp863'],
'pcoem864':    [1, 'cp864', 'ibm864'],
'pcoem865':    [1, 'cp865', '865', 'ibm865'],
'pcoem866':    [1, 'cp866', '866', 'ibm866'],
'pcoem869':    [1, 'cp869', '869', 'cp-gr', 'ibm869'],
'pcoem874':    [1, 'cp874'],
'shift-jis':   [2, 'shift_jis', 'csshiftjis', 'shiftjis', 'sjis', 's_jis'],
'thai':        [1, 'iso8859_11', 'so-8859-11', 'thai'],
'us-ascii':    [1, 'ascii', '646', 'us-ascii'],
'utf-8':       [4, 'utf_8', 'u8', 'utf', 'utf8', 'utf-8'],
'warabic':     [1, 'cp1256', 'windows-1256'],
'wbaltic':     [1, 'cp1257', 'windows-1257'],
'wcyrillic':   [1, 'cp1251', 'windows-1251'],
'wgreek':      [1, 'cp1253', 'windows-1253'],
'whebrew':     [1, 'cp1255', 'windows-1255'],
'wlatin1':     [1, 'cp1252', 'windows-1252'],
'wlatin2':     [1, 'cp1250', 'windows-1250'],
'wturkish':    [1, 'cp1254', 'windows-1254'],
'wvietnamese': [1, 'cp1258', 'windows-1258'],
'any':None,
'dec-cn':None,
'dec-jp':None,
'dec-tw':None,
'ebcdic1025':None,
'ebcdic1026':None,
'ebcdic1047':None,
'ebcdic1112':None,
'ebcdic1122':None,
'ebcdic1130':None,
'ebcdic1137':None,
'ebcdic1140':None,
'ebcdic1141':None,
'ebcdic1142':None,
'ebcdic1143':None,
'ebcdic1144':None,
'ebcdic1145':None,
'ebcdic1146':None,
'ebcdic1147':None,
'ebcdic1148':None,
'ebcdic1149':None,
'ebcdic1153':None,
'ebcdic1154':None,
'ebcdic1155':None,
'ebcdic1156':None,
'ebcdic1157':None,
'ebcdic1158':None,
'ebcdic1160':None,
'ebcdic1164':None,
'ebcdic275':None,
'ebcdic277':None,
'ebcdic278':None,
'ebcdic280':None,
'ebcdic284':None,
'ebcdic285':None,
'ebcdic297':None,
'ebcdic424':None,
'ebcdic425':None,
'ebcdic838':None,
'ebcdic870':None,
'ebcdic875':None,
'ebcdic905':None,
'ebcdic924':None,
'ebcdic-any':None,
'euc-tw':None,
'hp15-tw':None,
'ibm-930':None,
'ibm-933':None,
'ibm-935':None,
'ibm-937':None,
'ibm-939e':None,
'ibm-939':None,
'ibm-942':None,
'ibm-950':None,
'ms-936':None,
'ms-949':None,
'ms-950':None,
'msdos720':None,
'open_ed-037':None,
'open_ed-1025':None,
'open_ed-1112':None,
'open_ed-1122':None,
'open_ed-1130':None,
'open_ed-1137':None,
'open_ed-1141':None,
'open_ed-1142':None,
'open_ed-1143':None,
'open_ed-1144':None,
'open_ed-1145':None,
'open_ed-1146':None,
'open_ed-1147':None,
'open_ed-1148':None,
'open_ed-1149':None,
'open_ed-1153':None,
'open_ed-1154':None,
'open_ed-1155':None,
'open_ed-1156':None,
'open_ed-1157':None,
'open_ed-1158':None,
'open_ed-1160':None,
'open_ed-1164':None,
'open_ed-1166':None,
'open_ed-273':None,
'open_ed-275':None,
'open_ed-277':None,
'open_ed-278':None,
'open_ed-280':None,
'open_ed-284':None,
'open_ed-285':None,
'open_ed-297':None,
'open_ed-425':None,
'open_ed-500':None,
'open_ed-838':None,
'open_ed-870':None,
'open_ed-905':None,
'open_ed-924':None,
'open_ed-930':None,
'open_ed-933':None,
'open_ed-935':None,
'open_ed-937':None,
'open_ed-939e':None,
'open_ed-939':None,
'pc1098':None,
'pciscii806':None,
'pcoem1129':None,
'pcoem921':None,
'pcoem922':None,
'roman8':None
}