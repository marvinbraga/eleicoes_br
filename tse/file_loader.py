# coding=utf-8
"""
Loader
Todos os direitos reservados.
Marcus Vinicius Braga, 2020.
"""
from zipfile import ZipFile
import pandas as pd


class FileZipDownloader:
    """ Classe para baixar os arquivos CSV do site do TSE """
    _url_base = 'https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes%/buweb/bweb_%t_%_%.zip'

    def __init__(self, year, states, round, file_id):
        # 31102016132955
        self._file_id = file_id
        # 1 ou 2
        self._round = round
        self._states = states
        self._year = year


class FileCsvLoader:
    """ Classe para carregar o conteúdo do arquivo CSV zipado. """

    def __init__(self, file_name):
        self._file_name = file_name
        self._data = None

    def execute(self):
        """ Executa a carga do conteúdo. """
        zip_file = ZipFile(self._file_name)
        self._data = [
            pd.read_csv(zip_file.open(text_file.filename), encoding="ISO-8859-1", header=0, sep=';')
            for text_file in zip_file.infolist() if text_file.filename.endswith('.csv')
        ][0]
        return self

    @property
    def data(self):
        """ Retorna o valor da propriedade _data. """
        return self._data
