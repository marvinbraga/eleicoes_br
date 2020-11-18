# coding=utf-8
"""
Todos os direitos registrados.
Marcus Vinicius Braga, 2020.
Classes de Adapters para API ElectionBR.
"""
from core.abstracts import AbstractAdapterElection
import electionsBR as api


class AdapterElectionBR(AbstractAdapterElection):
    """ Adapter para API ElectionBR. """

    def __init__(self):
        self._obj = api

    def get_elections(self, **kwargs):
        """
        Método para recuperar as informações sobre as eleições.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_elections(**kwargs)

    def get_candidates(self, **kwargs):
        """
        Método para recuperar as informações sobre os candidatos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_candidates(**kwargs)

    def get_coalitions(self, **kwargs):
        """
        Método para recuperar as informações sobre coligações.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_coalitions(**kwargs)

    def get_assets(self, **kwargs):
        """
        Método para recuperar as informações sobre ativos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_assets(**kwargs)

    def get_affiliated(self, **kwargs):
        """
        Método para recuperar as informações sobre filiados.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_filiates(**kwargs)

    def get_secretaries(self, **kwargs):
        """
        Método para recuperar as informações sobre secretários.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_secretaries(**kwargs)

    def get_votes(self, **kwargs):
        """
        Método para recuperar as informações sobre votos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._obj.get_votes(**kwargs)
