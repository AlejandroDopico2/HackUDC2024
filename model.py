from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

def standarizeData(train, test):

    scaler = StandardScaler()

    scaler.fit(train)
    
    scaled_train = scaler.transform(train)
    scaled_test = scaler.transform(test)

    return scaled_train, scaled_test

def featureEngineeringData(df):
    df = df.drop('Método de obtención', axis=1)
    df = df.drop('Mes', axis=1)
    df = df.drop('Dia', axis=1)
    df = df.drop('Dia_week', axis=1)
    df = df.drop('Hora', axis=1)
    df = df.drop('Código universal de punto de suministro', axis=1)
    df = df.drop('Estacion', axis=1)
    df = df.drop('finde', axis=1)

    return df

def data(df):
    df = df.drop('Método de obtención', axis=1)
    df = df.drop('Mes_cos', axis=1).drop('Mes_sin', axis=1)
    # df = df.drop('hora_cos', axis=1).drop('hora_sin', axis=1)
    df = df.drop('Dia_cos', axis=1).drop('Dia_sin', axis=1)
    df = df.drop('Dia_week_cos', axis=1).drop('Dia_week_sin', axis=1)
    df = df.drop('hora_cos', axis=1).drop('hora_sin', axis=1)
    df = df.drop('Código universal de punto de suministro', axis=1)

    return df

def preProcessData(inputpath):
    df = pd.read_csv(inputpath)

    df = featureEngineeringData(df)

    targets = df.pop("Precio").values.reshape(-1, 1)
    print(targets.shape)

    df.to_csv('sample.csv', index=False)

    inputs = np.array(df.iloc[:, :-1].values)

    trainIndex = int(0.85* len(inputs))

    X_train = inputs[:trainIndex]
    X_test = inputs[trainIndex:]
    y_train = targets[:trainIndex]
    y_test = targets[trainIndex:]

    X_train, X_test = standarizeData(X_train, X_test)

    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)

    return X_train, X_test, y_train, y_test

#X_train, X_test, y_train, y_test = train_test_split(inputs, targets, test_size=0.2, random_state=42)

def linearModel(X_train, X_test, y_train, y_test):

    rf_regressor = LinearRegression()

    # Fit the model on the training data
    rf_regressor.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_regressor.predict(X_test)

    # Evaluate the performance of the model
    rmse =mean_squared_error(y_test, y_pred, squared=True)
    r2 = r2_score(y_pred, y_test)

    print(f'Root Mean Squared Error: {rmse}')
    print(f'R2-score: {r2}')

def randomForestModel(X_train, X_test, y_train, y_test):

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    # Fit the model on the training data
    rf_regressor.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_regressor.predict(X_test)

    # Evaluate the performance of the model
    rmse = mean_squared_error(y_test, y_pred, squared=True)
    r2 = r2_score(y_pred, y_test)

    print(f'Root Mean Squared Error: {rmse}')
    print(f'R2-score: {r2}')

def XGBoostModel(X_train, X_test, y_train, y_test):
    xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)

    xgb_model.fit(X_train, y_train)

    y_pred = xgb_model.predict(X_test)

    mse=mean_squared_error(y_pred, y_test)
    r2 = r2_score(y_pred, y_test)

    print(f'Mean Squared Error: {mse}')
    print(f'R2-score: {r2}')

    xgb.plot_importance(xgb_model)

# # Plot the original data and the regression line
# plt.scatter(X_test, y_test, color='black', label='Actual Data')
# plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Random Forest Regression')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.show()
    
if __name__ == '__main__':
    inputFile = "dataset/data_house_0.csv"
    # process_csv(electrodatos)

    # Ruta de la carpeta que quieres recorrer
    carpeta = './houses'

    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(carpeta)

    # Recorrer los archivos en la carpeta
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)

        print(f'{ruta_completa}')
        
        X_train, X_test, y_train, y_test = preProcessData(ruta_completa)

        linearModel(X_train, X_test, y_train, y_test)
        # Verificar si es un archivo (y no una subcarpeta)
        # if os.path.isfile(ruta_completa):
        #     print(f'Archivo: {ruta_completa}')

    #X_train, X_test, y_train, y_test = preProcessData(inputFile)

    #randomForestModel(X_train, X_test, y_train, y_test)
    #linearModel(X_train, X_test, y_train, y_test)
    #XGBoostModel(X_train, X_test, y_train, y_test)