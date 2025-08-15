import yfinance as yf  # Já possui as bibliotecas pandas e o requests
import pandas as pd # Importando Pandas para utilização do concat
from datetime import datetime

# Site de referência para biblioteca yFinance : https://ranaroussi.github.io/yfinance/reference/yfinance.ticker_tickers.html

def get_commodities_df() -> pd.DataFrame:
    symbols = ["GC=F", "CL=F", "SI=F"]  # Ouro, Petróleo e Prata respectivamente
    dfs = []

    for sym in symbols:
        # Última cotação (1 minuto)
        ultimo_df = yf.Ticker(sym).history(period="1d", interval="1m")[['Close']].tail(1)

        # Estrutura dos dados já renomeados para se adequar
        ultimo_df = ultimo_df.rename(columns={"Close": "preco"})
        ultimo_df["ativo"] = sym
        ultimo_df["moeda"] = "USD"
        ultimo_df["hora_coleta"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #Inclusão de data formatada e retirada dos milisegundos

        # Ordenar colunas
        ultimo_df = ultimo_df[["ativo", "preco", "moeda", "hora_coleta"]]

        dfs.append(ultimo_df)
    
    return pd.concat(dfs, ignore_index=True)

if __name__ == "__main__":
    df = get_commodities_df()
    print(df)
    print("Cotação das commodities obtidas com sucesso")

