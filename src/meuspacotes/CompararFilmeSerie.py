import pandas as pd
import matplotlib.pyplot as plt

def comparar_filmes_series_por_ano(df):
    # Separar filmes e séries
    filmes = df[df['type'] == 'Movie']
    series = df[df['type'] == 'TV Show']

    # Contar o número de filmes e séries lancados por ano
    filmes_por_ano = filmes['release_year'].value_counts().sort_index()
    series_por_ano = series['release_year'].value_counts().sort_index()

    # Criar um df com as contagens para facilitar a comparação
    comparacao_ano = pd.DataFrame({
        'Filmes': filmes_por_ano,
        'Séries': series_por_ano
    }).fillna(0)  # Preencher com 0 onde não houver valores

    # Ajustar a visualização para anos mais espaçados (de 5 em 5 anos)
    comparacao_ano_filtrada = comparacao_ano[comparacao_ano.index % 5 == 0]
    
    print("Gráfico Comparação de Filmes e Séries por Ano de Lançamento (Intervalos de 5 anos)")

    # Plotar o gráfico comparativo ajustado
    plt.figure(figsize=(14, 7))
    comparacao_ano_filtrada.plot(kind='bar', width=0.8)
    plt.title("Comparação de Filmes e Séries por Ano de Lançamento (Intervalos de 5 anos)")
    plt.xlabel("Ano de Lançamento")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.show()

