from os.path import join
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
from os import path, mkdir

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

def predict_model(data, username):

    model_path = f'../users/{username}/model.joblib'
    
    model = load(model_path)

    cost = model.predict(data)

    return cost