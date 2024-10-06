# Função para mostrar todas as colunas presentes no DataFrame
def Mostrar_colunas(df): 
    # Obter a lista de todas as colunas no DataFrame
    lista_Colunas = list(df.columns)
    
    # Inicializar um contador para indicar o número da coluna
    i = 1
    
    # Loop através de todas as colunas e imprimir cada uma com seu índice
    for colunas in lista_Colunas:
        print(f"COLUNA {i}: {colunas}")  # Exibir a coluna com seu índice correspondente
        i += 1  # Incrementar o contador para o próximo índice
    