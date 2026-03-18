# Importação de bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Etapa 1: Gerar e salvar um CSV com dados simulados
# (mantida a estrutura do modelo, mas agora usando o arquivo real)
try:
    df = pd.read_csv("train.csv")
    if 'LotArea' not in df.columns:
        df = pd.read_csv("train.csv", sep=";")
except FileNotFoundError:
    print("Erro: o arquivo 'train.csv' não foi encontrado na mesma pasta do código.")
    exit()

# Etapa 2: Importação dos dados
try:
    df = pd.read_csv("train.csv")
    if 'LotArea' not in df.columns:
        df = pd.read_csv("train.csv", sep=";")
except FileNotFoundError:
    print("Erro: o arquivo 'train.csv' não foi encontrado na mesma pasta do código.")
    exit()

# Remover espaços extras nos nomes das colunas, se houver
df.columns = df.columns.str.strip()

# Etapa 3: Seleção de colunas relevantes
selected_columns = ['LotArea', 'YearBuilt', 'OverallQual', 'SalePrice']
df_selected = df[selected_columns].copy()

# Etapa 4: Pré-processamento
print("Valores ausentes por coluna:")
print(df_selected.isnull().sum())

# Substituir possíveis textos "NA" por NaN
df_selected = df_selected.replace("NA", np.nan)

# Garantir que as colunas sejam numéricas
for col in selected_columns:
    df_selected[col] = pd.to_numeric(df_selected[col], errors='coerce')

# Preencher valores ausentes com a média
for col in selected_columns:
    df_selected[col].fillna(df_selected[col].mean(), inplace=True)

# Etapa 5: Transformação (normalização da coluna 'SalePrice')
df_selected['SalePrice_norm'] = (
    df_selected['SalePrice'] - df_selected['SalePrice'].mean()
) / df_selected['SalePrice'].std()

# Etapa 6: Mineração de dados (modelo de regressão linear)
X = df_selected[['LotArea', 'YearBuilt', 'OverallQual']]
y = df_selected['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Etapa 7: Interpretação dos resultados
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE (Erro Quadratico Medio): {mse:.2f}")
print(f"R² (Coeficiente de Determinacao): {r2:.2f}")

# Etapa 8: Visualização
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='red')
plt.xlabel("Valores Reais")
plt.ylabel("Valores Previstos")
plt.title("Previsão de Valores com Regressao Linear")
plt.grid(True)
plt.show()