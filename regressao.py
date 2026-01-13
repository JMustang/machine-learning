# %%

import pandas as pd

df = pd.read_excel("data/dados_cerveja_nota.xlsx")
df.head()

# %%

from sklearn import linear_model

x = df[["cerveja"]]
y = df[["nota"]]
# %%
