# Função para contar o número total de filmes no DataFrame
def Contar_filmes(df): 
    # Contar a quantidade de filmes na coluna 'type'
    # 'df['type'].value_counts()['Movie']' retorna o número de ocorrências de 'Movie'
    total_movies = df['type'].value_counts()['Movie']
    
    # Exibir o total de filmes encontrados na Netflix
    print(f"Total de filmes disponíveis na Netflix: {total_movies}")
