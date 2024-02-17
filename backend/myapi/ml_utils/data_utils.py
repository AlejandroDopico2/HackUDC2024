import numpy as np
import pandas as pd
import requests

def req_price():
    url = "https://api.preciodelaluz.org/v1/prices/avg?zone=PCB"
    r = requests.get(url=url)
    data = r.json()
    
    return data["price"]

def radianEngineeringData(df):
    df['hora_sin'] = np.sin(2 * np.pi * df['Hora'] / 24)
    df['hora_cos'] = np.cos(2 * np.pi * df['Hora'] / 24)

    df['mes_sin'] = np.sin(2 * np.pi * df['Mes'] / 12)
    df['mes_cos'] = np.cos(2 * np.pi * df['Mes'] / 12)

    df['dia_sin'] = np.sin(2 * np.pi * df['Dia'] / 31)
    df['dia_cos'] = np.cos(2 * np.pi * df['Dia'] / 31)

    df['dia_semana_sin'] = np.sin(2 * np.pi * df['Dia_week'] / 7)
    df['dia_semana_cos'] = np.cos(2 * np.pi * df['Dia_week'] / 7)

    columns_to_drop = ['Mes', 'Dia', 'Dia_week', 'Hora', 'Fecha', 'Código universal de punto de suministro', 'Método de obtención']
    df = df.drop(columns_to_drop, axis=1)
    return df

def getPriceEveryday(df):

    prices_df = pd.read_csv('../prices_by_day.csv', parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))

    merged_df = pd.merge(df, prices_df, on=['Hora', 'Fecha'], how='inner')
    merged_df['Precio'] = merged_df['Precio'].str.replace(',', '.').astype(float) / 1000

    return merged_df

def splitDatetime(df):
    df['Ano'] = df['Fecha'].dt.year
    df['Mes'] = df['Fecha'].dt.month
    df['Dia'] = df['Fecha'].dt.day
    df['Dia_week'] = df['Fecha'].dt.dayofweek
    return df

def lagData(df):
    lags = [1, 7, 30]
    for lag in lags:
        df[f'Consumo_lag_hora_{lag}'] = df['Consumo'].shift(lag*24)
        df[f'Precio_lag_hora_{lag}'] = df['Precio'].shift(lag*24)

    df[f'Consumo_lag_hora_anterior_{lag}'] = df['Consumo'].shift(1)
    df[f'Precio_lag_hora_anterior_{lag}'] = df['Precio'].shift(1)

    return df.dropna()

def lagDataDistributed(df):
    lags = [(1, 1), (2, 7), (3, 30)]
    for lag, days in lags:
        df[f'Consumo_lag_hora_{days}'] = df['Consumo'].shift(lag)
        df[f'Precio_lag_hora_{days}'] = df['Precio'].shift(lag)

    df[f'Consumo_lag_hora_anterior_30'] = df['Consumo'].shift(1)
    df[f'Precio_lag_hora_anterior_30'] = df['Precio'].shift(1)

    return df.dropna()

def getYearlyFeatures(df):
    df['Finde'] = (df['Dia_week'] > 5).astype(int)
    df['Estacion'] = df['Mes'] % 12 // 3

    return df

def build_data(day):
    pass
    
