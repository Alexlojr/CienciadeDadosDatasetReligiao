# Ciência de Dados — Dataset de Religião

Análise exploratória de dados sobre a distribuição de religiões no mundo entre 1945 e 2010, em intervalos de 5 anos.

## Dados

Os arquivos ficam em `Dados/` e vêm do **World Religion Project** (Correlates of War):

| Arquivo | Nível | Linhas | Descrição |
|---|---|---|---|
| `global.csv` | Mundo | 14 | Número de adeptos por religião no mundo, por ano |
| `regional.csv` | Região | 70 | O mesmo, por região (África, Ásia, Europa etc.) |
| `national.csv` | País | 1995 | O mesmo, por país |

As colunas seguem o padrão `religiao_vertente` (ex.: `christianity_protestant`, `islam_sunni`). Colunas terminadas em `_all` somam todas as vertentes, e as terminadas em `_percent` são proporções da população.

## Estrutura

```
.
├── Dados/              # CSVs do dataset
├── src/
│   ├── Leitura/
│   │   └── lercsv.py   # funções para carregar os CSVs
│   └── main/
│       └── main.py     # ponto de entrada
├── requirements.txt
└── README.md
```

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
python -m src.main.main
```

Rode os comandos a partir da raiz do projeto. No PyCharm, basta executar o `main.py`.

## Uso

```python
from src.Leitura.lercsv import ler_global, ler_regional, ler_national, ler_csv

df = ler_global()
df_paises = ler_national()
```

Os caminhos são montados a partir da localização do `lercsv.py`, então a leitura funciona de qualquer diretório.
