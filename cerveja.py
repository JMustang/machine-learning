# %%
import pandas as pd

df = pd.read_excel("data/dados_cerveja.xlsx")
df.head()
# %%

features = ["temperatura", "copo", "espuma", "cor"]
target = "classe"
