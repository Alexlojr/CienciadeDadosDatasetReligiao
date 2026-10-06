from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from src.Analise.estatistica import RELIGIOES_PRINCIPAIS

PASTA_FIGURAS = Path(__file__).resolve().parents[2] / 'figuras'


def evolucao_global(df_global, mostrar=True):
    """Gráfico de linhas: % da população mundial em cada religião, 1945–2010."""
    dados = (
        df_global[['year', *RELIGIOES_PRINCIPAIS]]
        .rename(columns=RELIGIOES_PRINCIPAIS)
        .melt(id_vars='year', var_name='Religião', value_name='percentual')
    )
    dados['percentual'] *= 100

    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=dados, x='year', y='percentual', hue='Religião', marker='o', ax=ax)
    ax.set_title('Evolução das principais religiões no mundo (1945–2010)')
    ax.set_xlabel('Ano')
    ax.set_ylabel('% da população mundial')
    fig.tight_layout()

    PASTA_FIGURAS.mkdir(exist_ok=True)
    caminho = PASTA_FIGURAS / 'evolucao_global.png'
    fig.savefig(caminho, dpi=150)
    print(f'Gráfico salvo em {caminho}')

    if mostrar:
        plt.show()
    plt.close(fig)
