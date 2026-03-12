import pandas as pd

df = pd.read_csv("data/processed/dataset_clean.csv")



df = data[['ai_adoption_rate', 'productivity_change_percent']].copy()
pd.set_option('display.width', None)
print(df.head(8))
print("media : \n", df.mean())
print("mediana :  \n", df.median())
print("Moda: \n", df.mode())
print("Variância amostral: \n", df.var(ddof=1))
print("DP amostral: \n", df.std(ddof=1))
