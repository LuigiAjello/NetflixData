import pandas as pd 
from dotenv import load_dotenv
import os
from meuspacotes.Colunas import Mostrar_colunas
from meuspacotes.NumeroFilmes import Contar_filmes
from meuspacotes.DiretoresProducoes import Diretores_Producoes
from meuspacotes.CincoDiretores import cinco_diretores_filme_serie, cinco_diretores_filme, cinco_diretores_serie
from meuspacotes.GenerosPopulares import Generos_populares_filmes, Generos_populares_series
from meuspacotes.CompararFilmeSerie import comparar_filmes_series_por_ano
from meuspacotes.ProducoesPaises import paises_com_mais_producoes

def main():
  # Carregar variáveis do arquivo .env
    load_dotenv()
    
    # Obter o caminho do CSV a partir da variável de ambiente
    csv_path = os.getenv('CSV_PATH')

    if not csv_path:
        print("Erro: Caminho para o arquivo CSV não encontrado no .env.")
        return

    # Carregar o DataFrame com os dados do arquivo CSV
    df = pd.read_csv(csv_path)

    print("\nRESPOSTAS:\n\n")
    # Análises principais
    Contar_filmes(df)
    print(".......................................\n")
    Mostrar_colunas(df)
    print(".......................................\n")
    Diretores_Producoes(df)
    print(".......................................\n")
    cinco_diretores_filme_serie(df)
    print(".......................................\n")
    cinco_diretores_serie(df)
    print(".......................................\n")
    cinco_diretores_filme(df)
    print(".......................................\n")

    # Insights e gráficos
    print("\nINSIGHT:\n\n")
    Generos_populares_filmes(df)
    print(".......................................\n")
    Generos_populares_series(df)
    print(".......................................\n")
    paises_com_mais_producoes(df)
    print(".......................................\n")
    comparar_filmes_series_por_ano(df)
    print(".......................................\n")

if __name__ == '__main__':
    main()
