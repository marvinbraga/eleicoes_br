# coding=utf-8
"""
Todos os direitos registrados.
Marcus Vinicius Braga, 2020.
Classes de Adaptees para API ElectionBR.
"""
from core.abstracts import AbstractAdapterElection
from core.adapters import AdapterElectionBR


class AdapteeElection(AbstractAdapterElection):
    """ Classe para adaptee de Election. """
    def __init__(self, adapter=None):
        self._adapter = adapter
        if adapter is None:
            # inicializa com o adapter padrão
            self._adapter = AdapterElectionBR()

    def get_elections(self, **kwargs):
        """
        Método para recuperar as informações sobre as eleições.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_elections(**kwargs)

    def get_candidates(self, **kwargs):
        """
        Método para recuperar as informações sobre os candidatos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_candidates(**kwargs)

    def get_coalitions(self, **kwargs):
        """
        Método para recuperar as informações sobre coligações.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_coalitions(**kwargs)

    def get_assets(self, **kwargs):
        """
        Método para recuperar as informações sobre ativos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_assets(**kwargs)

    def get_affiliated(self, **kwargs):
        """
        Método para recuperar as informações sobre filiados.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_affiliated(**kwargs)

    def get_secretaries(self, **kwargs):
        """
        Método para recuperar as informações sobre secretários.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_secretaries(**kwargs)

    def get_votes(self, **kwargs):
        """
        Método para recuperar as informações sobre votos.
        :param kwargs: Dict.
        :return: Dict.
        """
        return self._adapter.get_votes(**kwargs)
