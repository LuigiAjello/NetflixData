def Diretores_Producoes(df):
    # Remover registros com valores vazios em 'director' ou 'cast'
    df_filtrado = df.dropna(subset=['director', 'cast'])
    
    # Identificar diretores que também aparecem no elenco (coluna 'cast')
    diretores_atores = df_filtrado[df_filtrado.apply(lambda row: any(diretor in row['cast'] for diretor in row['director'].split(', ')), axis=1)]
    
    # Obter os nomes dos diretores que atuaram em suas próprias produções
    diretores_atores_nomes = list(diretores_atores['director'].unique())  # Converter para lista para manipulação
    
    # Contar o número de diretores que atuaram em suas próprias produções
    numero_diretores_atores = len(diretores_atores_nomes)
    
    # Criar a mensagem combinada com quebras de linha
    mensagem = f"A quantidade total e o nome de alguns Diretores que também atuaram como atores em suas próprias produções:\n" \
               f"Quantidade total: {numero_diretores_atores}\n" \
               f"Alguns nomes:\n{chr(10).join(diretores_atores_nomes[:5])}"  # Usar chr(10) para quebra de linha em listas

    print(mensagem)