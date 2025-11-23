import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diametro"]]
y = df[["preço"]]
model.fit(x, y)

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
