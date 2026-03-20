import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed/dataset_clean.csv")

df = data.copy()

target = "annual_revenue_usd_millions"

def iqr_outliers(series):
    s = series.dropna()
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    mask = (series < low) | (series > high)
    return mask, low, high


mask, low, high = iqr_outliers(df[target])
print(f"{target}: outliers = {mask.sum()} | limites=[{low:.3f}, {high:.3f}]")

df_raw = df[target].dropna()
df_clean = df.loc[~mask, target].dropna()

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].boxplot(df_raw.values, vert=True)
axes[0].set_title(f"ANTES")
axes[0].set_ylabel(target)

axes[1].boxplot(df_clean.values, vert=True)
axes[1].set_title(f"DEPOIS")
axes[1].set_ylabel(target)

plt.suptitle(f"Remoção de outliers via IQR - {target}")
plt.tight_layout()
plt.show()