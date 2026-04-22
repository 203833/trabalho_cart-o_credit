import pandas as pd
import glob

arquivos = glob.glob("faturas/*.csv")

df_total = pd.DataFrame()

for arquivo in arquivos:
    df = pd.read_csv(arquivo, sep=';')

    df.columns = df.columns.str.lower().str.strip()

    df = df.rename(columns={'valor (em r$)': 'valor'})

    df['valor'] = df['valor'].astype(float)

    df['data de compra'] = pd.to_datetime(
        df['data de compra'], dayfirst=True, errors='coerce'
    )

    df['mes'] = df['data de compra'].dt.month
    df['ano'] = df['data de compra'].dt.year

    df_total = pd.concat([df_total, df], ignore_index=True)

df_total.to_csv("dados_tratados.csv", index=False)