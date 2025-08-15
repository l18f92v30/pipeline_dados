import os
import time
import pandas as pd

# Chamar a função def get_bitcoin_df()
from GetBitcoin import get_bitcoin_df

# Chamar a função get_commodities_df()
from GetCommodities import get_commodities_df

SLEEP_SECONDS = 3600
CSV_PATH = "Cotacoes.csv"

if __name__ == "__main__":
    # Se quiser garantir cabeçalho na primeira execução, crie o arquivo vazio com header:
    if not os.path.exists(CSV_PATH):
        # escreve cabeçalho apenas uma vez
        cols = ["ativo", "preco", "moeda", "horario_coleta"]
        pd.DataFrame(columns=cols).to_csv(CSV_PATH, index=False)

    while True:
        # Coleta
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        # Junta tudo
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Salva (append sem cabeçalho)
        df.to_csv(CSV_PATH, mode="a", header=False, index=False)

        # Espera próximo ciclo
        time.sleep(SLEEP_SECONDS)

print ("Bitcoin obtido com sucesso")
print ("Commodities obtidas com sucesso")