import pandas as pd

# Percentual das principais religiões em relação à população
RELIGIOES_PRINCIPAIS = {
    'christianity_percent': 'Cristianismo',
    'islam_percent': 'Islamismo',
    'hinduism_percent': 'Hinduísmo',
    'buddhism_percent': 'Budismo',
    'judaism_percent': 'Judaísmo',
    'noreligion_percent': 'Sem religião',
}


def resumo(df, colunas=RELIGIOES_PRINCIPAIS):
    """Média, mediana, moda, desvio padrão, mínimo e máximo de cada coluna."""
    dados = df[list(colunas)]
    tabela = pd.DataFrame({
        'media': dados.mean(),
        'mediana': dados.median(),
        'moda': dados.mode().iloc[0],
        'desvio_padrao': dados.std(),
        'minimo': dados.min(),
        'maximo': dados.max(),
    })
    return tabela.rename(index=colunas)
