""" This utils file contains all the loaded saved artifacts 
like the saved model, and city columns which have been saved
in a json file. 
"""

import json
import pickle
import numpy as np

# Defining 3 global variables
__cities = None
__data_columns = None
__regressor = None


def predict_home_price(
        n_bedrooms,
        n_bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        yrs_since_last_renovation,
        basement,
        city
        ):
    
    if f"city_{city.lower()}" in __cities:
        city_index = __cities.index(f"city_{city.lower()}")
    else:
        city_index = __cities.index("city_others")
    
    x = np.zeros(len(__data_columns))
    x[0] = n_bedrooms
    x[1] = n_bathrooms
    x[2] = sqft_living
    x[3] = sqft_lot
    x[4] = floors
    x[5] = yrs_since_last_renovation
    if basement == "Yes" or basement == "yes":
        x[6] = 1
    x[city_index] = 1
        
    return int(__regressor.predict([x])[0])
    

def get_city_names():
    return __cities

def load_saved_artifacts():
    print("Loading of artifacts has begun...")
    
    global __cities
    global __data_columns
    global __regressor
    
    with open("C:/Users/admin/Desktop/PortfolioProjects/MachineLearning/house_price_prediction/model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __cities = __data_columns[7:]
        
    
    with open("C:/Users/admin/Desktop/PortfolioProjects/MachineLearning/house_price_prediction/model/house_price_prediction_model.pickle", "rb") as f:
        __regressor = pickle.load(f)
        
    print("Loading of artifacts has been completed!")
    
    
    
if __name__=="__main__":
    load_saved_artifacts()
    print(get_city_names())
    print(predict_home_price(3,1,1410,7200,2,123,'No','Seattle'))
    print(predict_home_price(4,1,2100,9288,1,56,'Yes','Renton'))
    print(predict_home_price(3,1,1090,8640,1,51,'No','Burien'))
