import pandas as pd
from .ml_utils.data_utils import getPriceEveryday, getYearlyFeatures, lagData, radianEngineeringData, splitDatetime
from .ml_utils.model import train_model, predict_model
import requests


def prepareDataToTrain(df):
    df = splitDatetime(df)
    df = getPriceEveryday(df)
    df = getYearlyFeatures(df)
    df = lagData(df)
    df = radianEngineeringData(df)
    df = pd.get_dummies(df, columns=['Estacion', 'Finde'])

    return df

def fit_model(username):
    #user
    df = pd.read_csv(f"../users/{username}/data.csv", parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y'))

    df = prepareDataToTrain(df)
    targets = df['Consumo']
    df.drop(['Consumo'], axis=1, inplace=True)
    
    print(df.head())
    train_model((df, targets), username)

def predict(username):

    data = pd.read_csv(f"../users/{username}/data.csv", parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y'))
    max_date_index = data['Fecha'].idxmax()
    first_day = data.iloc[max_date_index]
    previous_index = max_date_index - 24 * 30
    previous_data = data.iloc[previous_index:]

    previous_data = previous_data.reset_index()

    predict_model(previous_data, first_day['Fecha'], username)
