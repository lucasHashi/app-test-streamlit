import pandas as pd
import numpy as np
import json
import requests
from pprint import pprint

def main():
    url_json_dados = 'https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/dados_completos.json'
    json_dados = requests.get(url_json_dados)
    json_dados = json_dados.json()

    #pprint(json_dados['Crops']['Vegetables']['Spinach'])

    for colheita in json_dados:
        #print(colheita)
        linhas_atual = []
        for categoria in json_dados[colheita]:
            #print(categoria)
            for produto in json_dados[colheita][categoria]:
                item = json_dados[colheita][categoria][produto]
                item['categoria'] = categoria
                linhas_atual.append(item)

        df_atual = pd.DataFrame(linhas_atual)
        nome_csv = 'colheita_'+str(colheita)+'.csv'
        df_atual.to_csv(nome_csv)

def teste_csv():
    df = pd.read_csv('https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/final.csv', sep='?')
    print(df.head())
    



if __name__ == "__main__":
    teste_csv()