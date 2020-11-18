# coding=utf-8
"""
Teste eleições
"""
from controllers.classes import ControllerEleicaoMunicipal

if __name__ == '__main__':
    controller = ControllerEleicaoMunicipal(ano_eleicao=2016)
    eleitos = controller.eleitos()
    partidos = controller.agrupados()

    # Imprime todos os dados da consulta
    print(controller.data)
    # imprime todos os dados agrupados por partido com filtros.
    print(eleitos[(eleitos['CODIGO_PARTIDO'] == '40') & (eleitos['UF'] == 'PE')].sort_values(
        'TOTAL_VOTOS', ascending=False))
    # Imprime os dados agrupados e totalizados por partido.
    print('TOTAL DE CIDADES:', partidos['CIDADES'].sum())
    print(partidos.sort_values('CIDADES', ascending=False))
