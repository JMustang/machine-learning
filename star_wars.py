#  A República luta por continuar existindo. Liderado pelos generais Jedi, o exército de clones enfrenta o exército separatista. Os dróides são muitos e as batalhas já foram melhores. Alguns soldados têm falhado em meio ao campo de batalha sem que se conheça a causa.

# O alto conselho Jedi entra em ação. A partir de informações documentadas por seus generais, o conselho exige da equipe de War Analytics (o B.I. da velha república) insights capazes de estancar o sangramento e manter a galáxia sob o comando do Senado Galáctico.

# %%
import pandas as pd

df = pd.read_parquet("data/dados_clones.parquet")
df.head()

# %%
target = "Status "
features = [
    "p2o_master_id",
    "Massa(em kilos)",
    "General Jedi encarregado",
    "Estatura(cm)",
    "Distância Ombro a ombro",
    "Tamanho do crânio",
    "Tamanho dos pés",
    "Tempo de existência(em meses)",
]

x = df[features]
y = df[target]

# %%
from sklearn import tree

model = tree.DecisionTreeClassifier()

model.fit(x, y)

# %%
df["General Jedi encarregado"].unique()

# %%
