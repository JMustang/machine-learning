# %%

import pandas as pd

df = pd.read_excel("data/dados_cerveja_nota.xlsx")
df.head()

# %%

from sklearn import linear_model

X = df[["cerveja"]]
y = df["nota"]

reg = linear_model.LinearRegression()
reg.fit(X, y)
# %%

a, b = reg.intercept_, reg.coef_[0]
print(a, b)
print(f"Nota = {a} + {b} * cerveja")
# %%

predict = reg.predict(X.drop_duplicates())
predict
# %%

import matplotlib.pyplot as plt

plt.plot(X["cerveja"], y, "o")
plt.grid(True)
plt.title("Relação Cerveja vs Nota")
plt.xlabel("Ceveja")
plt.ylabel("Nota")
plt.plot(X.drop_duplicates()["cerveja"], predict, color="red")
# %%
