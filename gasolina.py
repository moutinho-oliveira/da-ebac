pip install pandas matplotlib seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
dados = pd.read_csv('gasolina.csv')
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x='venda', y='dia', data=dados, marker='o')
plt.title('Variação do Preço da Gasolina')
plt.xlabel('Preço (R$)')
plt.ylabel('Dia')
plt.savefig('gasolina3.png')