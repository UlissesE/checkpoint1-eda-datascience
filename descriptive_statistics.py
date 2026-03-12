import pandas as pd

data = pd.read_csv("data/processed/dataset_clean.csv")

df = data[['ai_adoption_rate', 'revenue_growth_percent']].copy()
pd.set_option('display.width', None)
print(df.head(50))