# %%
# Importação da biblioteca pandas
import pandas as pd
# %%
def main():
    # Importação do arquivo CSV
    df = pd.read_csv('vgsales/vgsales.csv')
    # %%
    # Visualização do nosso dataframe
    df
    # %%
    # Visualiza apenas as 5 primeiras linhas
    # print(df.head())
    # %%
    # Filtro somente por genero Sports
    df_sports = df[df.Genre == 'Sports']
# %%
main()
