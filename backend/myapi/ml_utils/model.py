from os.path import join
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
from os import path, mkdir
import pandas as pd
from .data_utils import getPriceEveryday, getYearlyFeatures, lagDataDistributed, radianEngineeringData, splitDatetime, req_price

import warnings
warnings.filterwarnings('ignore')
import datetime


def train_model(train_data, username):

    model_path = f'../users/{username}'

    X_train, y_train = train_data

    model = RandomForestRegressor(
        max_depth=10,
        min_samples_leaf=4, 
        min_samples_split=2, 
        n_estimators=100
    )

    print("TRAINING")

    model.fit(X_train, y_train)

    if not path.exists(model_path):
        mkdir(model_path)

    model.feature_names = list(X_train.columns.values)

    dump(model, model_path + "/model.joblib")

def predict_model(data, first_day, username):
    first_day = first_day + datetime.timedelta(days=1)
    final_day = first_day + pd.DateOffset(months=1) - pd.DateOffset(days=1)
    model_path = f'../users/{username}/model.joblib'
    
    model = load(model_path)
    precio = req_price()

    prediction = pd.DataFrame(columns=['Fecha', 'Hora', 'Consumo'])

    for date_actual in pd.date_range(start=first_day, end=final_day, freq='H'):
        date_actual = date_actual - datetime.timedelta(hours=1)
        previous_indices = [len(data)-1 - 24 * i for i in [0, 1, 7, 30]]
        features_anteriores = data.iloc[previous_indices]

        df = splitDatetime(features_anteriores)
        df = getYearlyFeatures(df)
        df['Precio'] = precio
        df = lagDataDistributed(df)
        df = radianEngineeringData(df)
        estaciones = [0, 1, 2, 3]
        for estacion in estaciones:
            if df.iloc[0]['Estacion'] == estacion:
                df[f'Estacion_{estacion}'] = True
            else:
                df[f'Estacion_{estacion}'] = False
        
        df["Finde_0"] = df["Finde"].apply(lambda x: not x)
        df["Finde_1"] = df["Finde"]

        df.drop(["Estacion", "Finde", "Consumo", "index"], inplace=True, axis=1)

        columnas_ordenadas = [
            'Ano',
            'Precio',
            'Consumo_lag_hora_1',
            'Precio_lag_hora_1',
            'Consumo_lag_hora_7',
            'Precio_lag_hora_7',
            'Consumo_lag_hora_30',
            'Precio_lag_hora_30',
            'Consumo_lag_hora_anterior_30',
            'Precio_lag_hora_anterior_30',
            'hora_sin',
            'hora_cos',
            'mes_sin',
            'mes_cos',
            'dia_sin',
            'dia_cos',
            'dia_semana_sin',
            'dia_semana_cos',
            'Estacion_0',
            'Estacion_1',
            'Estacion_2',
            'Estacion_3',
            'Finde_0',
            'Finde_1'
        ]
        df = df.reindex(columns=columnas_ordenadas)
        cost = model.predict(df)


        nueva_fila = {
            'index': data.iloc[-1]['index']+1,
            'Código universal de punto de suministro': 10,
            'Fecha': date_actual,
            'Hora': date_actual.hour+1,
            'Consumo': cost[0].round(3),
            'Método de obtención': 'R'
        }

        output = {
            'Fecha': date_actual,
            'Hora': date_actual.hour+1,
            'Consumo': cost[0].round(3),
        }

        data.loc[len(data)] = nueva_fila
        prediction.loc[len(data)] = output
    
    prediction.to_csv(f'../users/{username}/prediction_{first_day}')