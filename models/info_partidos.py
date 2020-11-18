# coding=utf-8
"""
Todos os direitos registrados.
Marcus Vinicius Braga, 2020.
Classes de models para eleições no Brasil.
"""
import pandas as pd


class InfoPartidos:
    """ Classe que contém dados estáticos com informações dos partidos. """

    _INFO_PARTIDOS = [
        {'NOME': 'Republicanos', 'SIGLA': 'REPUB', 'CODIGO_PARTIDO': 10, 'IDEOLOGIA': 'Liberal',
         'POSICIONAMENTO': 'Centro/Direita'},
        {'NOME': 'Progressistas', 'SIGLA': 'PP', 'CODIGO_PARTIDO': 11, 'IDEOLOGIA': 'Bandidal',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Democrático Trabalhista', 'SIGLA': 'PDT', 'CODIGO_PARTIDO': 12, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido dos Trabalhadores', 'SIGLA': 'PTralha', 'CODIGO_PARTIDO': 13, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Trabalhista Brasileiro', 'SIGLA': 'PTB', 'CODIGO_PARTIDO': 14, 'IDEOLOGIA': 'Conservador',
         'POSICIONAMENTO': 'Centro/Direita'},
        {'NOME': 'Movimento Democrático Brasileiro', 'SIGLA': 'MDB', 'CODIGO_PARTIDO': 15, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Socialista dos Trabalhadores Unificado', 'SIGLA': 'PSTU', 'CODIGO_PARTIDO': 16,
         'IDEOLOGIA': 'Socialista', 'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Social Liberal', 'SIGLA': 'PSL', 'CODIGO_PARTIDO': 17, 'IDEOLOGIA': 'Liberal',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Rede Sustentabilidade', 'SIGLA': 'REDE', 'CODIGO_PARTIDO': 18, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Podemos', 'SIGLA': 'PODE', 'CODIGO_PARTIDO': 19, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Social Cristão', 'SIGLA': 'PSC', 'CODIGO_PARTIDO': 20, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Comunista Brasileiro', 'SIGLA': 'PCB', 'CODIGO_PARTIDO': 21, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Liberal', 'SIGLA': 'PL', 'CODIGO_PARTIDO': 22, 'IDEOLOGIA': 'Liberal',
         'POSICIONAMENTO': 'Centro/Direita'},
        {'NOME': 'Cidadania', 'SIGLA': 'CID/PPS', 'CODIGO_PARTIDO': 23, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Democratas', 'SIGLA': 'DEM', 'CODIGO_PARTIDO': 25, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Democracia Cristã', 'SIGLA': 'DC', 'CODIGO_PARTIDO': 27, 'IDEOLOGIA': 'Conservador',
         'POSICIONAMENTO': 'Centro/Direita'},
        {'NOME': 'Partido Renovador Trabalhista Brasileiro', 'SIGLA': 'PRTB', 'CODIGO_PARTIDO': 28,
         'IDEOLOGIA': 'Conservador', 'POSICIONAMENTO': 'Ultra/Direita'},
        {'NOME': 'Partido da Causa Operária', 'SIGLA': 'PCO', 'CODIGO_PARTIDO': 29, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Novo', 'SIGLA': 'NOVO', 'CODIGO_PARTIDO': 30, 'IDEOLOGIA': 'Liberal',
         'POSICIONAMENTO': 'Direita'},
        {'NOME': 'Partido da Mobilização Nacional', 'SIGLA': 'PMN', 'CODIGO_PARTIDO': 33, 'IDEOLOGIA': 'Liberal',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido da Mulher Brasileira', 'SIGLA': 'PMB', 'CODIGO_PARTIDO': 35, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Trabalhista Cristão', 'SIGLA': 'PTC', 'CODIGO_PARTIDO': 36, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Socialista Brasileiro', 'SIGLA': 'PSB', 'CODIGO_PARTIDO': 40, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Verde', 'SIGLA': 'PV', 'CODIGO_PARTIDO': 43, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido da Social Democracia Brasileira', 'SIGLA': 'PSDB', 'CODIGO_PARTIDO': 45,
         'IDEOLOGIA': 'Socialista', 'POSICIONAMENTO': 'Esquerda'},
        {'NOME': 'Partido Socialismo e Liberdade', 'SIGLA': 'PSOL', 'CODIGO_PARTIDO': 50, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Patriota', 'SIGLA': 'PATRI', 'CODIGO_PARTIDO': 51, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Esquerda'},
        {'NOME': 'Partido Social Democrático', 'SIGLA': 'PSD', 'CODIGO_PARTIDO': 55, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Partido Comunista do Brasil', 'SIGLA': 'PCdoB', 'CODIGO_PARTIDO': 65, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Avante', 'SIGLA': 'AVANT', 'CODIGO_PARTIDO': 70, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Esquerda'},
        {'NOME': 'Solidariedade', 'SIGLA': 'SOLID', 'CODIGO_PARTIDO': 77, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Centro/Esquerda'},
        {'NOME': 'Unidade Popular', 'SIGLA': 'UP', 'CODIGO_PARTIDO': 80, 'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Ultra/Esquerda'},
        {'NOME': 'Partido Republicano da Ordem Social', 'SIGLA': 'PROS', 'CODIGO_PARTIDO': 90,
         'IDEOLOGIA': 'Socialista',
         'POSICIONAMENTO': 'Esquerda'},
    ]

    @property
    def data(self):
        """
        Método que retorna dados com informações dos partidos.
        :return: DataFrame.
        """
        partidos = pd.DataFrame.from_dict(self._INFO_PARTIDOS)
        # Convertendo os Dados das Colunas
        colunas_categorias = ['IDEOLOGIA', 'POSICIONAMENTO']
        for name in colunas_categorias:
            partidos[name] = partidos[name].astype("category")
        return partidos.copy()
