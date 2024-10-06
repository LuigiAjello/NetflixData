def cinco_diretores_filme_serie (df):
    # Contar o número de filmes e séries por diretor
    contagem_diretores = df['director'].value_counts().dropna()

    # Obter os 5 diretores com mais produções
    top_5_diretores = contagem_diretores.head(5)

    # Exibir os 5 diretores com mais filmes e séries
    print(f"5 diretores com mais filmes e séries:\n{top_5_diretores}")


def cinco_diretores_filme (df):
    # Filtrar apenas os registros de filmes
    filmes = df[df['type'] == 'Movie']

    # Contar o número de filmes por diretor
    contagem_diretores_filmes = filmes['director'].value_counts().dropna()

    # Obter os 5 diretores com mais filmes
    top_5_diretores_filmes = contagem_diretores_filmes.head(5)

    print(f"5 diretores com mais filmes:\n {top_5_diretores_filmes}")


def cinco_diretores_serie (df):
    # Filtrar apenas os registros de séries
    series = df[df['type'] == 'TV Show']

    # Contar o número de séries por diretor
    contagem_diretores_series = series['director'].value_counts().dropna()

    # Obter os 5 diretores com mais séries
    top_5_diretores_series = contagem_diretores_series.head(5)

    print(f"5 diretores com mais séries: \n{top_5_diretores_series}")
