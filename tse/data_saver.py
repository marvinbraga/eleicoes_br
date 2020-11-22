# coding=utf-8
"""
Data Saver
Todos os direitos reservados.
Marcus Vinicius Braga, 2020.
"""
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
import pandas as pd


class DataSaver:
    """ Classe para salvar os dados dos arquivos para a base de dados. """
    def __init__(self, database_url, files):
        self._files = files
        self._database_url = database_url
        self._engine = create_engine(database_url, echo=True)
        self.create_database()

    @property
    def files(self):
        """ Retorna o valor da propriedade _files (FilesManager). """
        return self._files

    @property
    def engine(self):
        """ Retorna o valor da propriedade _engine (sqlalchemy). """
        return self._engine

    def create_database(self):
        """ Método para criar o database na base de dados. """
        if not database_exists(self._engine.url):
            create_database(self._engine.url)
        return self

    def save_file(self, ufs=None):
        """
        Salva os dados do content na base de dados.
        :param ufs: lista com as UFs.
        :return: self.
        """
        if ufs:
            for uf in ufs:
                self.save(self._files.get_by_uf(uf))
        else:
            for arq in self._files.files:
                self.save(arq)
        return self

    def save(self, arq):
        """
        Método para salvar dados do DataFile na base de dados.
        :param arq: DataFile.
        :return: self.
        """
        if arq:
            if self._count_data(arq) == 0:
                arq.content.replace('#NULO#', 0, inplace=True)
                print(f'Salvando {len(arq.content.index)} registros... [{str(arq)}].')
                arq.content.to_sql('urnas', self._engine, chunksize=500, if_exists='append')
                print(f'Pronto! O arquivo [{str(arq)}] foi salvo com sucesso.')
                print('Quantidade de registros salvos: ', self._count_data(arq))
        return self

    def _count_data(self, arq):
        """
        Método para recuperar a quantidade de registros de uma UF na base de dados.
        :param arq: DataFile.
        :return: Int.
        """
        result = pd.read_sql(
            sql=text('select count(*) from urnas where "SG_UF"=' + f"'{arq.state}'"),
            con=self._engine
        )
        return result['count'][0]
