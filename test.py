# coding=utf-8
"""
Client
"""
from tse.data_saver import DataSaver
from tse.files_manager import FilesManager
import pandas as pd
from sqlalchemy import text

# from tse.prefeitos import ConsolidadorVotosPrefeito


print('Carregando dados...')
ds = DataSaver(
    database_url='postgresql://scott:tiger@localhost:5432/eleicoes_bd',
    files=FilesManager('E:/TSE/2020/zip/')
)  # .save_file()
# print('Carregando arquivos...')
# cons = ConsolidadorVotosPrefeito(files=arquivos)
print('Pronto!')

result = pd.read_sql(
    sql=text('select * from view_prefeitos_agrupados'),
    con=ds.engine
)

cidades = pd.read_sql(
    sql=text('select distinct "NM_MUNICIPIO" from urnas u order by "NM_MUNICIPIO"'),
    con=ds.engine)

dt_eleitos = []
for i in range(len(cidades.index)):
    cidade = cidades['NM_MUNICIPIO'][i]
    el = result[(result['NM_MUNICIPIO'] == cidade)]
    eleito = el.sort_values(['NR_TURNO', 'quant'], ascending=[False, False]).iloc[0]
    dt_eleito = {
        'ANO_ELEICAO': 2020,
        'CIDADE': eleito["NM_MUNICIPIO"],
        'UF': eleito["SG_UF"],
        'SG_PARTIDO': eleito["SG_PARTIDO"],
        'TOTAL_VOTOS': eleito["quant"],
        'CONT': 1,
        'NR_TURNO': eleito['NR_TURNO']
    }
    dt_eleitos.append(dt_eleito)

eleitos = pd.DataFrame.from_dict(dt_eleitos)
eleitos.sort_values('TOTAL_VOTOS', ascending=False)
rs = eleitos[['SG_PARTIDO', 'CONT']].groupby('SG_PARTIDO').count().sort_values('CONT', ascending=False)
rs.to_csv('E:\\2020.csv', encoding="ISO-8859-1", sep=';', quotechar='"')