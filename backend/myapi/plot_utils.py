import pandas as pd
from .ml_utils.data_utils import *

def getPlotData(csvPath, option='month'):
    df = pd.read_csv(csvPath, parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y'))
    df = getPriceEveryday(df)
    df = splitDatetime(df)
    df = getYearlyFeatures(df)

    for column_name in df.columns:
        print(column_name)

    # mes_consumo = df.groupby('Mes')['Consumo'].sum().reset_index()
    if option == 'month':
        df['Fecha'] = pd.to_datetime(df['Mes'], format='%m').dt.strftime('%B')

        mes_consumo = df.groupby(['Mes', 'Fecha'])['Consumo'].sum().reset_index()

        print(mes_consumo)

        output = mes_consumo[['Fecha', 'Consumo']].values.tolist()

    elif option == 'day_month':
        day_month_consume = df.groupby('Dia')['Consumo'].sum().reset_index()

        print(day_month_consume)

        output = day_month_consume[['Dia', 'Consumo']].values.tolist()

    elif option == 'day_week':
        df['Nombre_Dia_Semana'] = df['Fecha'].dt.day_name()

        day_week_consume = df.groupby(['Nombre_Dia_Semana'])['Consumo'].sum().reset_index()

        print(day_week_consume)

        output = day_week_consume[['Nombre_Dia_Semana', 'Consumo']].values.tolist()




    # Display the list of lists
    # print("List of Lists [Fecha, Consumo]:", fecha_consumo_lists)
    return output