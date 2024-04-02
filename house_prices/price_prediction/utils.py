import pickle
import json
import numpy as np

class HousePricePredictor:
    def __init__(self):
        self.__model = None
        self.__data_columns = None
        self.load_model_and_columns()  # Load model and columns in constructor

    def load_model_and_columns(self):
        print("Loading saved artifacts...")
        with open("D:/kishore/Django/Real_estate_AI_Model/house_prices/price_prediction/models/columns.json", "r") as f:
            self.__data_columns = json.load(f)['data_columns']
        with open("D:/kishore/Django/Real_estate_AI_Model/house_prices/price_prediction/models/bangalore_home_prices_model.pickle", "rb") as f:
            self.__model = pickle.load(f)
        print("Loading saved artifacts... done")

    # def get_location_names(self):
    #     return self.__data_columns[3:]  # Assuming locations start from index 3

    def predict_price(self, location, sqft, bhk, bath):
        try:
            loc_index = self.__data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(self.__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        return round(self.__model.predict([x])[0], 2)




    # return model,columns

# def predict_price(location,sqft,bath,bhk):
#     model , columns = load_model_and_columns()
#     print(f"Model loaded: {model is not None}")

#     x=np.zeros(len(columns)) 
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     loc_index = np.where(columns == location.lower())[0][0] 
#     if loc_index >= 0:
#         x[loc_index] = 1
#     return model.predict([x])[0]          