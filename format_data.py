import pandas as pd

df = pd.read_csv('electrodatos.csv')
df.drop(["datetime"], inplace=True, axis = 1)

df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')
df.replace({'Real': 'R', 'Estimado': 'E'}, inplace=True)


# df['Fecha'].dt.strftime()

for value in df['Código universal de punto de suministro'].unique():
    sub_df = df[df.iloc[:, 0] == value]
    df.to_csv(f'electrodatos_{value}.csv', index = False)
