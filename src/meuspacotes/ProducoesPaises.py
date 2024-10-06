import pandas as pd
import matplotlib.pyplot as plt

def paises_com_mais_producoes(df):
    
    # Contar o número de produções por país
    producoes_por_pais = df['country'].value_counts().head(10)  # Top 10 países

    # Printar os resultados
    print(f"Top 10 países com mais produções:\n{producoes_por_pais}\n")

    # Plotar gráfico de barras
    plt.figure(figsize=(12, 6))
    producoes_por_pais.plot(kind='bar', color='skyblue')
    plt.title('Países com Mais Produções (Top 10)')
    plt.xlabel('País')
    plt.ylabel('Quantidade de Produções')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

