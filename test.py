# coding=utf-8
"""
Client
"""
from tse.files_manager import FilesManager
from tse.prefeitos import ConsolidadorVotosPrefeito
from sqlalchemy import create_engine


print('Carregando dados...')
arquivos = FilesManager('E:/TSE/2020/zip/')
print('Carregando arquivos...')
cons = ConsolidadorVotosPrefeito(files=arquivos)
print('Pronto!')

engine = create_engine('postgresql://scott:tiger@localhost:5432/eleicoes_bd')
arq = arquivos.files[2]
arq.content.to_sql('table_name', engine, if_exists='append')
