from os.path import join
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
from os import path, mkdir
import pandas as pd

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

    dump(model, model_path + "/model.joblib")

def predict_model(data, first_day, username):
    
    final_day = first_day + pd.DateOffset(months=1) - pd.DateOffset(days=1)
    model_path = f'../users/{username}/model.joblib'
    
    model = load(model_path)

    for date_actual in pd.date_range(start=first_day, end=final_day, freq='H'):
        
        date_index = data.index[data['Fecha'] == date_actual][0]

        previous_indices = [date_index - 24 * i for i in [1, 7, 30]]

        features_anteriores = data.iloc[previous_indices]

        from time import sleep
        print(features_anteriores.head(10))
        sleep(30)


    cost = model.predict(data)

    return cost