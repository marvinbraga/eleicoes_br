# coding=utf-8
"""
Client
"""
from tse.data_saver import DataSaver
from tse.files_manager import FilesManager
# from tse.prefeitos import ConsolidadorVotosPrefeito

print('Carregando dados...')
arquivos = FilesManager('E:/TSE/2020/zip/')
# print('Carregando arquivos...')
# cons = ConsolidadorVotosPrefeito(files=arquivos)
# print('Pronto!')

ds = DataSaver('postgresql://scott:tiger@localhost:5432/eleicoes_bd', arquivos)
ds.save_file()

