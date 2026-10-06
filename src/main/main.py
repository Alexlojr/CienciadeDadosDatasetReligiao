import pandas as pd

from src.Analise.estatistica import resumo
from src.Leitura.lercsv import ler_global, ler_national
from src.Limpeza.limpeza import limpar
from src.Visualizacao.graficos import evolucao_global


def main():
    pd.set_option('display.float_format', '{:.4f}'.format)

    df_global = limpar(ler_global())
    df_national = limpar(ler_national())

    print('\nEstatística descritiva – mundo (proporção da população, 1945–2010)')
    print(resumo(df_global))

    print('\nEstatística descritiva – países (proporção da população, 1945–2010)')
    print(resumo(df_national))

    evolucao_global(df_global)


if __name__ == '__main__':
    main()
