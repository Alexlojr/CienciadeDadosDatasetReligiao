import pandas as pd


def limpar(df):
    """Limpeza básica: nomes de colunas, duplicatas, nulos e espaços em texto."""
    df = df.copy()

    # Tira o apóstrofo tipográfico dos nomes (islam_shi’a -> islam_shia, baha’i_all -> bahai_all)
    df.columns = df.columns.str.replace('’', '', regex=False)

    linhas_antes = len(df)
    df = df.drop_duplicates()
    duplicatas = linhas_antes - len(df)

    # Nos dados, nulo numa coluna de contagem significa que não houve estimativa.
    # Como são vertentes pequenas (ex.: judaism_reform na Colômbia), preenche com 0.
    nulos = int(df.isna().sum().sum())
    colunas_numericas = df.select_dtypes('number').columns
    df[colunas_numericas] = df[colunas_numericas].fillna(0)

    for coluna in df.select_dtypes(['object', 'string']).columns:
        df[coluna] = df[coluna].str.strip()

    print(f'Limpeza: {duplicatas} duplicatas removidas, {nulos} nulos preenchidos com 0')
    return df
