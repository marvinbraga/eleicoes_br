# coding=utf-8
"""
Todos os direitos registrados.
Marcus Vinicius Braga, 2020.
Classes de controladores para eleições no Brasil.
"""
from controllers.abstracts import AbstractController
import pandas as pd

from core.adaptees import AdapteeElection
from models.info_partidos import InfoPartidos


class ControllerCities(AbstractController):
    """ Controlador para regras de negócio de cidades. """

    def __init__(self, input_data):
        self._input_data = input_data
        self._data = None

    def execute(self):
        """
        Método para executar regra de negócio do controlador.
        :return: Self.
        """
        cidades = self._input_data.groupby('NOME_MUNICIPIO').count()
        dt_eleitos = []
        for i in range(len(cidades.axes[0])):
            cidade = cidades.axes[0][i]
            el = self._input_data[(self._input_data['NOME_MUNICIPIO'] == cidade)]
            eleito = el.sort_values('QTDE_VOTOS', ascending=False).iloc[0]
            dt_eleito = {
                'ANO_ELEICAO': eleito['ANO_ELEICAO'],
                'CIDADE': eleito["NOME_MUNICIPIO"],
                'UF': eleito["UF"],
                'CODIGO_PARTIDO': eleito["NUMERO_CANDIDATO"],
                'TOTAL_VOTOS': eleito["QTDE_VOTOS"],
                'NUM_TURNO': eleito['NUM_TURNO']
            }
            dt_eleitos.append(dt_eleito)

        eleitos = pd.DataFrame.from_dict(dt_eleitos)
        eleitos.sort_values('UF').sort_values('TOTAL_VOTOS', ascending=False)
        self._data = eleitos.copy()
        return self

    @property
    def data(self):
        """
        Método para retornar o valor da propriedade _data.
        :return: Self.
        """
        return self._data


class ControllerMergeTotaisPartidos(AbstractController):
    """ Classe de negócio para unir os dados de dois objetos  """

    def __init__(self, totais, partidos):
        self._partidos = partidos
        # Filtra apenas dados importantes.
        self._totais = totais[['CODIGO_PARTIDO', 'TOTAL_VOTOS']].groupby('CODIGO_PARTIDO').count().sort_values(
            'TOTAL_VOTOS', ascending=False)
        self._data = None

    def execute(self):
        """
        Método para executar regra de negócio do controlador.
        :return: Self.
        """
        partidos = self._partidos
        partidos['CIDADES'] = partidos['CODIGO_PARTIDO'].apply(lambda cod: self._get_total_votos(cod))
        self._data = partidos.sort_values('CIDADES', ascending=False)
        return self

    @property
    def data(self):
        """
        Método para retornar o valor da propriedade _data.
        :return: Valor da propriedade.
        """
        return self._data

    def _get_total_votos(self, cod_partido):
        """
        Método para ser utilizado em apply de DataFrame.
        :param cod_partido: Int.
        :return: Float.
        """
        result = 0
        codigos = self._totais.axes[0]
        for i in range(len(codigos)):
            if int(codigos[i]) == cod_partido:
                result = float(self._totais.values[i])
                break
        return result


class ControllerEleicaoMunicipal(AbstractController):
    """ Controlador para eleições municipais brasileiras. """

    def __init__(self, ano_eleicao=None, municipio=None, estado=None):
        self._estado = estado
        self._municipio = municipio
        self._ano_eleicao = ano_eleicao
        self._adaptee = AdapteeElection()
        self._colunas = ['ANO_ELEICAO', 'NOME_MUNICIPIO', 'UF', 'NUM_TURNO', 'DESCRICAO_CARGO', 'NUMERO_CANDIDATO',
                         'QTDE_VOTOS']
        self._colunas_categorias = ['ANO_ELEICAO', 'NOME_MUNICIPIO', 'UF', 'NUM_TURNO']
        self._data = None
        self._eleitos = None
        self._agrupados = None

    def clear(self):
        """
        Método para limpar dados auxiliares.
        :return: Self.
        """
        self._eleitos = None
        self._agrupados = None
        return self

    def execute(self):
        """
        Método para executar regra de negócio do controlador.
        :return: Self.
        """
        self._data = self.clear()._convert_data(data=self._get_votes())
        return self

    @property
    def data(self):
        """
        Método para retornar o valor da propriedade _data.
        :return: Self.
        """
        if self._data is None:
            self.execute()
        return self._data

    def eleitos(self):
        """
        Método para recuperar informações sobre os eleitos.
        :return: DataFrame.
        """
        if self._eleitos is None:
            self._eleitos = ControllerCities(input_data=self.data).execute().data
        return self._eleitos

    def agrupados(self):
        """
        Método para retornar as informações agrupadas por partido.
        :return: DataFrame.
        """
        if self._agrupados is None:
            self._agrupados = ControllerMergeTotaisPartidos(
                totais=self.eleitos(), partidos=InfoPartidos().data).execute().data
        return self._agrupados

    def _convert_data(self, data):
        """
        Método para converter colunas de categorias.
        :arg data: Dados de votos para serem convertidos. Exige coluna QTDE_VOTOS.
        :return:
        """
        result = data
        for name in self._colunas_categorias:
            result[name] = result[name].astype("category")
        result['QTDE_VOTOS'] = (result['QTDE_VOTOS']).astype(float)
        return result

    def _get_votes(self):
        """
        Métodos para recupera os dados da eleição municipal.
        :return: Dict.
        """
        kwargs = {}
        if self._ano_eleicao:
            kwargs['year'] = self._ano_eleicao
        if self._estado:
            kwargs['state'] = self._estado
        if self._municipio:
            kwargs['city'] = self._municipio

        return self._adaptee.get_votes(position="Prefeito", regional_aggregation="Municipio",
                                       columns_list=self._colunas, **kwargs)
