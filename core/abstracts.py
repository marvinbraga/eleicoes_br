# coding=utf-8
"""
Doc
"""
from abc import ABCMeta, abstractmethod


class AbstractAdapterElection(metaclass=ABCMeta):
    """ Interface para adapter de API de eleições. """
    @abstractmethod
    def get_elections(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre as eleições.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_candidates(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre os candidatos.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_coalitions(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre coligações.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_assets(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre ativos.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_affiliated(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre filiados.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_secretaries(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre secretários.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass

    @abstractmethod
    def get_votes(self, **kwargs):
        """
        Método abstrato para recuperar as informações sobre votos.
        :param kwargs: Dict.
        :return: Dict.
        """
        pass
