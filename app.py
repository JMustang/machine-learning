import streamlit as st
import pandas as pd
import unicodedata

from sklearn.linear_model import LinearRegression


def normalize(col: str) -> str:
    """Normalize column names: remove accents, lowercase, replace spaces with underscore."""
    s = "".join(
        c for c in unicodedata.normalize("NFKD", col) if not unicodedata.combining(c)
    )
    return s.lower().strip().replace(" ", "_")


# read CSV with the explicit separator used in the file and normalize columns
df = pd.read_csv("pizzas.csv", sep=";")
df.columns = [normalize(c) for c in df.columns]

# Verifica se as colunas esperadas existem após normalizar
required = ["diametro", "preco"]
missing = [c for c in required if c not in df.columns]
if missing:
    st.error(
        f"Coluna(s) faltando no CSV após normalização: {', '.join(missing)}. Colunas encontradas: {df.columns.tolist()}"
    )
    st.stop()

# Ensure numeric types for model training
df["diametro"] = pd.to_numeric(df["diametro"], errors="coerce")
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
df = df.dropna(subset=required)

if df.empty:
    st.error("Não há dados válidos para treinar o modelo após a conversão numérica.")
    st.stop()

model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
try:
    model.fit(x, y)
except Exception as ex:
    st.error(f"Falha ao treinar o modelo: {ex}")
    st.stop()

st.title("🍕Previsão de preço de pizza!🍕")
st.divider()

diametro = st.number_input(
    "Digite o tamanho do diametro da pizza (em cm):",
    min_value=10,
    max_value=500,
    step=1,
    key="diametro_input",
)

if diametro:
    preco_previsto = model.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza de {diametro} cm é R$ {preco_previsto:.2f}.")
