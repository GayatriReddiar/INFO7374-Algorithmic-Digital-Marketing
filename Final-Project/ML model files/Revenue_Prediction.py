import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import seaborn as sns
import joblib

def Revenuepredict():
    #prediction = joblib.load('Customer_Revenue_Prediction_Val')
    prediction_df = pd.read_csv('baseline_lgb.csv')
    forecast_df = prediction_df[['fullVisitorId','PredictedLogRevenue']]
    forecast_df.sort_values(by=['PredictedLogRevenue'], inplace=True, ascending=False)
    forecast_df1 = forecast_df.head(10)
    prediction_list = forecast_df1.to_dict("records")
    output = {}
    for data in prediction_list:
        userID = data["fullVisitorId"]
        output[userID] = data["PredictedLogRevenue"]
    return output

