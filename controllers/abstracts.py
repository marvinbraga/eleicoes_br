# coding=utf-8
from abc import ABCMeta, abstractmethod


class AbstractController(metaclass=ABCMeta):
    """ Interface para controladores de eleições. """

    @abstractmethod
    def execute(self):
        """
        Método para executar regra de negócio do controlador.
        :return: Self.
        """
        pass

    @property
    @abstractmethod
    def data(self):
        """
        Método para retornar o valor da propriedade _data.
        :return: Self.
        """
        pass
