import matplotlib.pyplot as plt
import pandas as pd

def Generos_populares_filmes(df):
    # Separar apenas filmes
    filmes = df[df['type'] == 'Movie']
    # Separar e contar os gêneros listados em 'listed_in'
    generos = filmes['listed_in'].str.split(', ').explode()
    # Contar a frequência de cada gênero
    generos_populares = generos.value_counts()
    # Exibir os 5 gêneros mais populares
    top_generos_filmes = generos_populares.head(5)

    # Printar os resultados
    print(f"5 gêneros de filmes mais populares na plataforma são:\n{top_generos_filmes}\n")

    # Gerar gráfico de pizza para os gêneros de filmes
    plt.figure(figsize=(8, 8))
    plt.pie(top_generos_filmes, labels=top_generos_filmes.index, autopct='%1.1f%%', startangle=140)
    plt.title("Top 5 Gêneros de Filmes Mais Populares")
    plt.show()


def Generos_populares_series(df):
    # Separar apenas séries
    series = df[df['type'] == 'TV Show']
    # Separar e contar os gêneros listados em 'listed_in'
    generos_series = series['listed_in'].str.split(', ').explode()
    # Contar a frequência de cada gênero
    generos_populares_series = generos_series.value_counts()
    # Exibir os 5 gêneros mais populares entre séries
    top_generos_series = generos_populares_series.head(5)

    # Printar os resultados
    print(f"5 gêneros de séries mais populares na plataforma são:\n{top_generos_series}\n")

    # Gerar gráfico de pizza para os gêneros de séries
    plt.figure(figsize=(8, 8))
    plt.pie(top_generos_series, labels=top_generos_series.index, autopct='%1.1f%%', startangle=140)
    plt.title("Top 5 Gêneros de Séries Mais Populares")
    plt.show()

