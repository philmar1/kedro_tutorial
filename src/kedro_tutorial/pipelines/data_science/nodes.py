"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.10
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor

from matplotlib import pyplot as plt 

import logging

logger = logging.getLogger(__name__)

class MyRegressor():
    def __init__(self, model_name: str, model_params: dict = {}) -> None:
        self.model_name = model_name
        self.model_params = model_params
        print(model_params)
        
        if model_name == 'linear_regression':
            self.model = LinearRegression(**model_params)
        if model_name == 'mlp':
            self.model = MLPRegressor(**model_params)
            
        logger.info(f'Initialized model {model_name} with additional params: {model_params}')
        
    def fit(self, X, y):
        return self.model.fit(X, y)
    
    
def split_train_test(df, test_size=0.2):
    train_cols = [x for x in df.columns if x != 'quality']
    X, y = df[train_cols], df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size)
    return X_train, X_test, y_train, y_test
    
    
def load_model(model_name: str, model_params: dict = {}):
    return MyRegressor(model_name, model_params) 

def train_model(regressor_model, X_train, y_train, training_params: dict = {}):
    logger.info(f'Training with additional params: {training_params}')
    regressor_model.model.fit(X_train, y_train, **training_params)
    return regressor_model 

def predict(regressor_model, X):
    return regressor_model.model.predict(X)


def plot_metrics(y_true, y_pred, which, model, save_dir=""):
    plt.scatter(y_true, y_pred)
    plt.xlabel('True')
    plt.ylabel('Pred')
    plt.savefig(save_dir + f'cm_{model.model_name}_{which}.png')
    
    
    