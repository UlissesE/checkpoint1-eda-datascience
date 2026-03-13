import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed/dataset_clean.csv")

df = data[['ai_adoption_rate', 'productivity_change_percent']].copy()
print(df.head(8))
print(df.shape)
print("media : \n", df.mean())
print("mediana :  \n", df.median())
print("Moda: \n", df.mode())
print("Variância amostral: \n", df.var(ddof=1))
print("DP amostral: \n", df.std(ddof=1))

plt.hist(df['ai_adoption_rate'], bins="auto", alpha=0.7, label="AI Adoption")
plt.hist(df['productivity_change_percent'], bins="auto", alpha=0.7,label="Produtividade")
plt.title("Histograma: Adoção AI / Aumento Produtividade")
plt.xlabel("%")
plt.ylabel("frequência")
plt.legend()
plt.show()