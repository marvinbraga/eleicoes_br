# coding=utf-8
"""
Loader
Todos os direitos reservados.
Marcus Vinicius Braga, 2020.
"""
import os
from tse.data_file import DataFile


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
                self._files.append(DataFile(os.path.normpath(os.path.join(p, file))))
        return self

    def __iter__(self):
        return self._files.__iter__()
