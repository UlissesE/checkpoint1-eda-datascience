# Checkpoint 1 - EDA: Adoção de IA em Empresas
### Data Science and Statistics Computing — 2ESPV | FIAP

[![Status](https://img.shields.io/badge/status-completed-green.svg)](https://github.com/)

## Autores

| Nome | RM |
|---|---|
| Eduardo Ulisses Pereira da Silva | 566339 |
| Henrique Guedes Silvestre | 562474 |

---

## 📋 Descrição

Este projeto realiza uma **Análise Exploratória de Dados (EDA)** sobre o dataset [Global AI Adoption & Workforce Impact Dataset](https://www.kaggle.com/datasets/mohankrishnathalla/global-ai-adoption-and-workforce-impact-dataset) do Kaggle.

O dataset reúne informações sobre a adoção de IA por empresas em diferentes países e setores econômicos, incluindo indicadores de estágio de adoção, nível de investimento, taxas de automação, mudanças na força de trabalho, produtividade, desempenho organizacional e práticas de governança. O objetivo do projeto é analisar **como a adoção de IA impacta a produtividade das empresas e as mudanças na força de trabalho**, identificando tendências, relações entre variáveis e possíveis impactos no ambiente corporativo moderno.

---

## 📁 Estrutura do Projeto

```
checkpoint1-eda-datascience/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── ai_company_adoption.csv       # dataset original do Kaggle
│   └── processed/
│       └── dataset_clean.csv             # após limpeza e filtragem de colunas
│
├── notebook/
│   └── eda_checkpoint1.ipynb             # notebook principal com toda a análise
│
└── backup/                               # scripts .py usados durante o desenvolvimento

```

---

## 🚀 Como Executar

1. Instale as dependências:
   ```bash
   pip install pandas matplotlib numpy
   ```

2. Abra o notebook:
   ```bash
   code notebook/eda_checkpoint1.ipynb
   ```

3. Execute as células em ordem — cada seção corresponde a uma etapa do checkpoint.

---

## 📊 Etapas da Análise

### 1. Preparação e Qualidade dos Dados
- Carregamento do CSV com `pandas`
- Verificação de nulos por coluna (`isnull().mean() * 100`) — resultado: 0% em todas as colunas
- Remoção de duplicatas com `drop_duplicates()`
- Filtragem de 20 colunas relevantes (removendo identificadores como `response_id` e `company_id`)
- Geração do arquivo `dataset_clean.csv`

### 2. Estatística Descritiva
Variáveis analisadas: `ai_adoption_rate` e `productivity_change_percent`

| Métrica | ai_adoption_rate | productivity_change_percent |
|---|---|---|
| Média | 36,41% | 9,27% |
| Mediana | 36,32% | 9,06% |
| Moda | 0,0 | 0,0 |
| Variância amostral | 211,53 | 31,78 |
| Desvio-padrão amostral | 14,54 | 5,64 |

Média e mediana próximas sugerem distribuição relativamente simétrica. A moda zero indica a presença de um grupo de empresas sem adoção de IA, o que contribui para a variabilidade observada. A mediana é a medida mais adequada para representar o valor típico, por ser robusta a outliers.

### 3. Histogramas
- Ambas as variáveis apresentam leve **assimetria à direita** (cauda à direita)
- Não há evidência forte de bimodalidade, mas pode haver dois perfis: empresas com baixa e alta adoção de IA
- A **mediana** é preferível à média como valor típico, por ser menos sensível a valores extremos

### 4. Correlação e Scatter
Correlações de Pearson calculadas:

| Par de variáveis | Correlação |
|---|---|
| `ai_adoption_rate` × `productivity_change_percent` | 0,675 |
| `task_automation_rate` × `time_saved_per_week` | 0,793 |

O primeiro par sugere correlação positiva moderada — acima de 60% de adoção, a dispersão aumenta, indicando que outros fatores também influenciam a produtividade. O segundo par apresenta relação mais consistente e direta ao longo de toda a faixa de dados.

### 5. Outliers com IQR e Boxplot
Variável analisada: `annual_revenue_usd_millions`

Os valores extremos identificados não representam erros de coleta, mas uma **mistura de perfis reais** — pequenas empresas com receita abaixo de $100M convivendo com grandes multinacionais acima de $5.000M. A mediana (~$100M USD) é mais representativa do cenário típico do que a média, que era puxada para cima pelos casos extremos.

---

## 🔧 Tecnologias

- Python 3.13
- Pandas 3.0.1
- Matplotlib
- NumPy
- Jupyter Notebook (VS Code)

---

## 🤖 Declaração de Uso de IA

A IA foi utilizada como apoio ao longo do projeto, principalmente para debugging, esclarecimento de dúvidas pontuais de sintaxe e auxílio na interpretação dos resultados. Todas as conclusões e textos foram elaborados pelos autores com base nas evidências dos dados.