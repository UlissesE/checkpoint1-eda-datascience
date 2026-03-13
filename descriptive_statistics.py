import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed/dataset_clean.csv")


df = data[['ai_adoption_rate', 'productivity_change_percent']].copy()

print(
    """
    ==========================================
    Estatística descritiva “com interpretação”
    ==========================================
    """
)

print(df.head(8))
print("\n")
print("\nMédia:\n", df.mean())
print("\nMediana:\n", df.median())
print("\nModa:\n", df.mode())
print("\nVariância Amostral:\n", df.var(ddof=1))
print("\nDP amostral:\n", df.std(ddof=1))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Ai Adoption Rate Graphics
axes[0].hist(df['ai_adoption_rate'], bins="auto", color="steelblue", alpha=0.7)
axes[0].set_title("Histograma: AI Adoption Rate")
axes[0].set_xlabel("%")
axes[0].set_ylabel("Frequência")

# Productivity Change Percent Graphics
axes[1].hist(df['productivity_change_percent'], bins="auto", color="orange", alpha=0.7)
axes[1].set_title("Histograma: Productivity Change")
axes[1].set_xlabel("%")
axes[1].set_ylabel("Frequência")

plt.tight_layout()
plt.show()