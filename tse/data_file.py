# coding=utf-8
"""
Loader
Todos os direitos reservados.
Marcus Vinicius Braga, 2020.
"""
from tse.file_loader import FileCsvLoader


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
