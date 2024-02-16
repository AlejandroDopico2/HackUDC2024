from datetime import date
import math
from pandas import read_csv


def process_csv(csv_path: str, out_path: str):
    df = read_csv(csv_path, parse_dates=['datetime'])

    grouped_df = df.groupby('Código universal de punto de suministro')

    for group_id, group_df in grouped_df:
        df['Mes_cos'] = df['datetime'].dt.month.apply(math.cos)
        df['Mes_sin'] = df['datetime'].dt.month.apply(math.sin)
        df['Año'] = df['datetime'].dt.year

        df['Dia_cos'] = df['datetime'].dt.day.apply(math.cos)
        df['Dia_sin'] = df['datetime'].dt.day.apply(math.sin)

        df['Dia_week'] = df['datetime'].dt.date.apply(date.weekday)

        df['finde'] = df['Dia_week'].apply(lambda x: 0 if x < 5 else 1)

        seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
        month_to_season = dict(zip(range(1, 13), seasons))

        df['Estacion'] = df['datetime'].dt.month.apply(lambda x: month_to_season[x])

        out_file= f"{out_path}house_{group_id}.csv"

        df.to_csv(out_file, index=False)

    return df


if __name__ == '__main__':
    electrodatos = "../data/electrodatos.csv"
    out_folder = "/home/agarcia/Escritorio/hackudc/data/"
    # process_csv(electrodatos)
    process_csv(electrodatos,out_folder)
