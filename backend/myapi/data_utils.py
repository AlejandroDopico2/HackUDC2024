import pandas as pd

def getPlotData(csvPath):
    df = pd.read_csv(csvPath)

    # mes_consumo = df.groupby('Mes')['Consumo'].sum().reset_index()

    df['Fecha'] = pd.to_datetime(df['Mes'], format='%m').dt.strftime('%B')

    mes_consumo = df.groupby(['Mes', 'Fecha'])['Consumo'].sum().reset_index()

    print(mes_consumo)

    fecha_consumo_lists = mes_consumo[['Fecha', 'Consumo']].values.tolist()

    # Display the list of lists
    # print("List of Lists [Fecha, Consumo]:", fecha_consumo_lists)
    return fecha_consumo_lists

# if __name__ == '__main__':
#     inputFile = '../../data/user_abel/data_house_0.csv'

#     getPlotData(inputFile)