import requests
import pandas as pd
from datetime import datetime


# AINDA SENDO ESTRUTURADO
# Obter cotação do dolar
# def obter_cotacao():
#     URL1 = "https://api.exchangerate-api.com/v4/lastest/USD"
#     response = requests.get(URL1) 
#     data = response.josn()
#     return data['rates']

# def converter_moeda(valor, moeda_origem, moeda_destino, taxas)
#     if moeda_origem in taxas and moedas_destino in taxas:
#         taxa_origem = taxas[moeda_origem]
#         taxa_destino = taxas[moeda_destino]
#         valor_em_usd = valor / taxa_origem
#         valor_convertido = valor_em_usd * taxa_destino

def get_bitcoin_df() -> pd.DataFrame:

    # URL cotação do Bitcoin
    URL2 = "https://api.coinbase.com/v2/prices/spot"

    # Retorno da cotação atual
    response = requests.get(URL2)
    dados = response.json()

    # Extração de dados
    preco = float(dados['data']['amount'])
    ativo = dados['data']['base']
    moeda = dados['data']['currency']
    hora_coleta = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #Inclusão de data formatada e retirada dos milisegundos

    # print(preco)
    # print(ativo)
    # print(moeda)
    # print(hora_coleta)  # Descomentar para validar se os dados estão entrando corretamente

    # dataframe = Estrutura de Dados
    df = pd.DataFrame([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'hora_coleta' : hora_coleta
    }])
    #df.to_csv('preco_bitcoin.csv', mode='a', header=False, index=False) # Descomentar para retorno dos dados em .csv

    return df

if __name__ == "__main__":
    df = get_bitcoin_df()
    print(df)
    print("Cotação do Bitcoin obtida com sucesso!")