from pathlib import Path

import pandas as pd

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS = RAIZ_PROJETO / 'Dados'


def ler_csv(nome_arquivo):
    return pd.read_csv(PASTA_DADOS / nome_arquivo)


def ler_global():
    return ler_csv('global.csv')


def ler_national():
    return ler_csv('national.csv')


def ler_regional():
    return ler_csv('regional.csv')



if __name__ == '__main__':
    dados = ler_global()

    # Só as colunas de contagem de adeptos (índices 1 a 35).

    colunas_contagem = dados.loc[:, 'christianity_protestant':'otherreligion_all']

    totais = colunas_contagem.sum()
    for coluna, total in totais.items():
        print(f'{coluna:<30} {total:>18,}')


