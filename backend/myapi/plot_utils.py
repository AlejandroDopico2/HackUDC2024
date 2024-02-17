import pandas as pd
from .ml_utils.data_utils import *

def getPlotData(csvPath, valor_filtro,option='month'):
    df = pd.read_csv(csvPath, parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y'))
    df = getPriceEveryday(df)
    df = splitDatetime(df)
    df = getYearlyFeatures(df)

    if option == 'month':
        df_ano = df[df['Ano'] == valor_filtro]

        return list(df_ano.groupby('Mes')['Consumo'].apply(list).apply(sum))

    elif option == 'day_month':

        df_mes = df[df['Mes'] == valor_filtro]

        return list(df_mes.groupby('Dia')['Consumo'].apply(list).apply(sum))

    elif option == 'day_week':
        df['Dia_week'] = df['Fecha'].dt.dayofweek

        day_week_consume = df.groupby(['Dia_week'])['Consumo'].sum().tolist()

        return day_week_consume

def get_years(csvPath):
    df = pd.read_csv(csvPath, parse_dates=["Fecha"])

    return df['Ano'].unique()
