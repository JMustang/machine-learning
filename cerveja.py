# %%
import pandas as pd

df = pd.read_excel("data/dados_cerveja.xlsx")
df.head()
# %%

features = ["temperatura", "copo", "espuma", "cor"]
target = "classe"

x = df[features]
y = df[target]

x = x.replace(
    {
        "mud": 1,
        "pint": 2,
        "sim": 1,
        "não": 0,
        "clara": 0,
        "escura": 1,
    }
)
x
# %%
from sklearn import tree

model = tree.DecisionTreeClassifier()

model.fit(x, y)
# %%
