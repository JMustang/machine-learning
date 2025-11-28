# machine-learning 🍕📊

Projeto de exemplo para previsão de preço de pizza usando regressão linear com scikit-learn.

Este repositório contém um app simples em Streamlit (`app.py`) e um notebook (`main.ipynb`) para explorar o dataset `pizzas.csv`.

---

## 🎯 Objetivo

Demonstrar um fluxo mínimo de Machine Learning com Python: carregar dados, treinar um modelo de regressão linear e expor uma interface web simples para prever o preço de uma pizza a partir do seu diâmetro.

---

## 🗂️ Estrutura do projeto

- `app.py` — App Streamlit que treina um modelo (LinearRegression) e permite prever preços.
- `main.ipynb` — Notebook exploratório com visualizações (scatter plot) e análise inicial.
- `pizzas.csv` — Dataset com duas colunas: diâmetro e preço.
- `env/` — Virtualenv já criado (opcional).

---

## 🛠️ Requisitos

- Python 3.10/3.11 recomendado (Python 3.14 pode ter menos pacotes pré-compilados).
- `pip` (ou `conda` / `mamba`).
- (Opcional) Homebrew em macOS para instalar ferramentas nativas (`cmake`, `apache-arrow`, `ninja`).

Principais dependências Python (exemplos):

- pandas
- scikit-learn
- streamlit

Se quiser criar um ambiente com venv:

```bash
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install pandas scikit-learn streamlit
```

Ou, usando conda (recomendado para evitar builds locais de pacotes nativos):

```bash
conda create -n mlpy python=3.11 -y
conda activate mlpy
conda install -c conda-forge pandas scikit-learn streamlit -y
conda install -c conda-forge pyarrow -y  # se precisar do pyarrow
```

---

## 🚀 Executando o app

1. Ative seu ambiente virtual (venv ou conda):

```bash
source env/bin/activate  # venv
# ou
conda activate mlpy     # conda
```

1. Instale as dependências (se ainda não fez):

```bash
# Recomendado: instalar tudo a partir do arquivo de dependências
pip install -r requirements.txt

# Alternativa: instalar individualmente
pip install pandas scikit-learn streamlit
```

1. Execute o Streamlit:

```bash
streamlit run app.py
```

Abra o navegador na URL informada pelo Streamlit (geralmente `http://localhost:8501`).

---

## 📘 Notebook

Abra `main.ipynb` em um ambiente Jupyter (ex.: `jupyter notebook` ou `jupyter lab`) e execute as células para explorar os gráficos e a análise dos dados.

---

## 📁 Data

O arquivo `pizzas.csv` tem duas colunas (cabeçalho): `Diâmetro;preço` (o separador é `;`). Exemplo:

```csv
Diâmetro;preço
20;50
22;55
24;60
...
```

Se você usando `pd.read_csv('pizzas.csv')`, certifique-se de passar `sep=';'` ou ajustar conforme o formato do seu CSV:

```python
df = pd.read_csv('pizzas.csv', sep=';')
```

---

## 🩺 Dicas de troubleshooting

- Solução rápida: usar o nome correto ou normalizar as colunas assim que carregar os dados:
-- Solução rápida: usar o nome correto ou normalizar as colunas assim que carregar os dados:

```python
import unicodedata

def normalize(col):
    s = ''.join(
        c for c in unicodedata.normalize('NFKD', col)
        if not unicodedata.combining(c)
    )
    return s.lower().strip().replace(' ', '_')

df = pd.read_csv('pizzas.csv', sep=';')
df.columns = [normalize(c) for c in df.columns]
# agora use df['diametro'] e df['preco']
```

- Erro na instalação do `pyarrow` com pip (CMake/compilador):

- Problema: pip tentou compilar o `pyarrow` localmente (requer `cmake` e `apache-arrow` C++); no macOS com Python recente, nem sempre há wheel disponível.

- Solução 1 (recomendado): utilizar conda e instalar `pyarrow` a partir do `conda-forge`:

```bash
conda install -c conda-forge pyarrow
```

- Solução 2: instalar dependências de build via Homebrew e expor o Arrow C++ ao CMake:

```bash
brew install apache-arrow cmake ninja
export Arrow_DIR="$(brew --prefix apache-arrow)/lib/cmake/arrow"
export CMAKE_PREFIX_PATH="$Arrow_DIR:$CMAKE_PREFIX_PATH"
source env/bin/activate
pip install --upgrade pip setuptools wheel cython
pip install pyarrow
```

- Solução 3: fallback — usar Python 3.10/3.11 onde há wheels disponibiladas e evitar compilação manual.

---

## ✅ Notas finais

- O projeto é intencionalmente simples para demonstrar um fluxo de ML com poucas linhas.
- Recomendo manter as colunas normalizadas (sem acentos) para evitar problemas em código e integração com bibliotecas externas.
