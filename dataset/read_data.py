import numpy as np
import pandas as pd


def process_csv(csv_path: str, out_path: str):
    df = pd.read_csv(csv_path, parse_dates=['Fecha'])

    # Agrupar por 'Código universal de punto de suministro'
    grouped_df = df.groupby('Código universal de punto de suministro')

    for group_id, group_df in grouped_df:
        group_df['Mes_cos'] = np.cos(group_df['Fecha'].dt.month)
        group_df['Mes_sin'] = np.sin(group_df['Fecha'].dt.month)
        group_df['Año'] = group_df['Fecha'].dt.year

        group_df['Dia_cos'] = np.cos(group_df['Fecha'].dt.day)
        group_df['Dia_sin'] = np.sin(group_df['Fecha'].dt.day)

        group_df['Dia_week'] = group_df['Fecha'].dt.dayofweek

        group_df['finde'] = (group_df['Dia_week'] < 5).astype(int)

        seasons = [4,4,1,1,1,2,2,2,3,3,3,4]
        month_to_season = dict(zip(range(1, 13), seasons))

        group_df['Estacion'] = group_df['Fecha'].dt.month.map(month_to_season)

        out_file = f"{out_path}house_{group_id}.csv"
        group_df.to_csv(out_file, index=False)

    return grouped_df


if __name__ == '__main__':
    electrodatos = "../data/electrodatos.csv"
    out_folder = "/home/agarcia/Escritorio/hackudc/data/"
    # process_csv(electrodatos)
    process_csv(electrodatos,out_folder)
