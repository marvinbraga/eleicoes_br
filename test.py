# coding=utf-8
"""
Client
"""
import os
import pandas as pd
from zipfile import ZipFile

caminho = 'E:\\TSE\\2020\\zip\\'


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


class DataFile:
    """ Classe para guardar as informações sobre o arquivo de dados de cada Estado. """

    def __init__(self, file_name=None):
        self._file_name = file_name
        self._type = ''
        self._round = 0
        self._state = ''
        self._number = ''
        self._content = None
        self._ext = ''
        self._init_data()

    def __str__(self):
        return f'{self._state}, round: {self._round}, file: {self._file_name}'

    def _init_data(self):
        """
        Método para inicializar as propriedades a partir do nome do arquivo.
        :return: self.
        """
        if self._file_name:
            data, self._ext = self._file_name.split('.')
            self._type, r, self._state, self._number = data.split('_')
            self._round = int(r[0])
        return self

    @property
    def ext(self):
        """ Retorna o valor da propriedade _ext. """
        return self._ext

    @property
    def type(self):
        """ Retorna o valor da propriedade _type. """
        return self._type

    @property
    def round(self):
        """ Retorna o valor da propriedade _round. """
        return self._round

    @property
    def state(self):
        """ Retorna o valor da propriedade _state. """
        return self._state

    @property
    def number(self):
        """ Retorna o valor da propriedade _number. """
        return self._number

    @property
    def file_name(self):
        """ Retorna o valor da propriedade _file_name. """
        return self._file_name

    @property
    def content(self):
        """ Retorna o valor da propriedade _content. """
        if self._content is None:
            self._content = FileCsvLoader(self._file_name).execute().data
        return self._content


class FilesManager:
    """ Classe para gerenciar arquivos a serem utilizados. """

    def __init__(self, path):
        self._path = path
        self._files = []
        self._load()

    @property
    def files(self):
        """
        Método para recuperar o valor da propriedade _files.
        :return: list.
        """
        return self._files

    def _load(self):
        """
        Método para executar a carga dos arquivos.
        :return: self.
        """
        for p, _, files in os.walk(os.path.abspath(self._path)):
            for file in files:
                self._files.append(DataFile(os.path.join(p, file)))
        return self

    def __iter__(self):
        return self._files.__iter__()


files = FilesManager(caminho)
for file in files:
    print(file)
