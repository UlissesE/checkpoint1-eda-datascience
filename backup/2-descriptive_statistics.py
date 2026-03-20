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

print(
    """
    ======================================================================
         Histogramas: Ai Adoption Rate X Productivity Change Percent
    ======================================================================
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


print(
    """
    ==========================================
         Correlação entre as variáveis
    ==========================================
    """
)

correlacao = df['ai_adoption_rate'].corr(df['productivity_change_percent'])
corr2 = data['task_automation_rate'].corr(data['time_saved_per_week'])

print("Correlações de Pearson")
print(f"Correlação de Pearson: {correlacao:.3f}")
print(f"\nCorrelação entre automação e tempo economizado: {corr2:.3f}")

fig, axes2 = plt.subplots(1, 2, figsize=(12,4))

# Scatter 1
axes2[0].scatter(
    df['ai_adoption_rate'],
    df['productivity_change_percent'],
    alpha=0.7,
    color="purple"
)
axes2[0].set_title("AI Adoption Rate vs Productivity Change")
axes2[0].set_xlabel("AI Adoption Rate (%)")
axes2[0].set_ylabel("Productivity Change (%)")
axes2[0].grid(True)

# Scatter 2
axes2[1].scatter(
    data['task_automation_rate'],
    data['time_saved_per_week'],
    color="green",
    alpha=0.7
)
axes2[1].set_title("Task Automation Rate vs Time Saved per Week")
axes2[1].set_xlabel("Task Automation Rate (%)")
axes2[1].set_ylabel("Time Saved per Week (hours)")
axes2[1].grid(True)

plt.tight_layout()
plt.show()

