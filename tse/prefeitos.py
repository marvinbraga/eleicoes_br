# coding=utf-8
"""
Loader
Todos os direitos reservados.
Marcus Vinicius Braga, 2020.
"""
from threading import Thread


class LoadDataFiles:
    """ Classe para fazer a carga dos dados dos arquivos de cada Estado. """

    def __init__(self, files):
        self._files = files

    def _load(self, data_file):
        """
        Método para recuperar os dados de um data_file.
        :param data_file:
        :return: self.
        """
        _ = data_file.content
        print(f'Concluído: {str(data_file)}.')
        return self

    def execute(self):
        """
        Método para recuperar os dados dos estados.
        :return: self
        """
        thread_list = [Thread(target=self._load, args=[file]) for file in self._files]
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
        return self


class ConsolidadorVotosPrefeito:
    """ Classe que gera relatório consolidado com votos de prefeito. """

    def __init__(self, files, columns=None):
        self._columns = columns
        self._files = files
        if self._columns is None:
            self._columns = [
                'CD_ELEICAO', 'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO', 'NR_ZONA', 'NR_SECAO',
                'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA', 'DS_CARGO_PERGUNTA', 'NR_PARTIDO',
                'SG_PARTIDO', 'DT_BU_RECEBIDO', 'CD_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'NR_VOTAVEL',
                'QT_VOTOS', 'NR_URNA_EFETIVADA'
            ]
        self._load_data()

    def _load_data(self):
        """
        Método para fazer a carga de dados
        :return:
        """
        LoadDataFiles(self._files).execute()
