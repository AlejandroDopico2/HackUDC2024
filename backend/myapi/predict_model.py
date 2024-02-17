import pandas as pd
from .ml_utils.data_utils import getPriceEveryday, getYearlyFeatures, lagData, radianEngineeringData, splitDatetime
from .ml_utils.model import train_model, predict_model

def prepareDataToTrain(df):
    df = splitDatetime(df)
    df = getPriceEveryday(df)
    df = getYearlyFeatures(df)
    df = lagData(df)
    df = radianEngineeringData(df)
    df = pd.get_dummies(df, columns=['Estacion', 'Finde'])

    return df

def fit_model(user):
    #user

    df = pd.read_csv(f"../users/{user}/data.csv", parse_dates=["Fecha"], date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y'))

    df = prepareDataToTrain(df)
    targets = df['Consumo']
    df.drop(['Consumo'], axis=1, inplace=True)
    
    print(df.head())
    train_model((df, targets), user)

# def predict():


