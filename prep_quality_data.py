import pandas as pd

data = pd.read_csv("data/raw/ai_company_adoption.csv")
df = data.copy()

# Visualização inicial
print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
df.info()

print("\n=== % DE NULOS POR COLUNA ===")
print(df.isnull().mean() * 100)

# Regras de limpeza
print("\n=== DUPLICATAS ===")
print(f"Linhas duplicadas: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)

print("\n=== REMOVENDO COLUNAS IRRELEVANTES ===")
colunas_relevantes = [
    'survey_year',
    'country',
    'industry',
    'company_size',
    'num_employees',
    'annual_revenue_usd_millions',
    'ai_adoption_rate',
    'ai_maturity_score',
    'years_using_ai',
    'ai_budget_percentage',
    'productivity_change_percent',
    'task_automation_rate',
    'time_saved_per_week',
    'jobs_displaced',
    'jobs_created',
    'reskilled_employees',
    'revenue_growth_percent',
    'cost_reduction_percent',
    'employee_satisfaction_score',
    'customer_satisfaction'
]
df = df[colunas_relevantes]
print(f"Colunas restantes: {df.shape[1]}\n")
print(df.info())

print("\n=== DATASET FINAL ===")
print(df.shape)