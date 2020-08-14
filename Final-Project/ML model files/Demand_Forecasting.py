import time
import seaborn as sns
import pandas as pd
import matplotlib as plt
import numpy as np

from fbprophet import Prophet
from sklearn.model_selection import KFold
from scipy import stats, optimize, interpolate

import statsmodels.api as sm

def Demandpredict(itemID, deptID):
    df = pd.read_csv('ProphetData.csv')
    holidays = pd.read_csv('ProphetHolidays.csv')
    df = df[(df['item'] == itemID) & (df['dept'] == deptID)]
    prediction_size = 30
    m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True, holidays=holidays)
    m.fit(df[['ds','y']]);
    future = m.make_future_dataframe(periods=prediction_size)
    forecast = m.predict(future)
    forecast_df = forecast.tail(30)
    forecast_df.to_csv("Prophet.csv")
    forecast_df = forecast[-30:-20]
    forecast_df1 = forecast_df[['ds','yhat','yhat_lower','yhat_upper']]
    forecast_df2 = forecast_df1.to_dict("records")
    output = {}
    for data in forecast_df2:
        date = data["ds"]
        output[date] = data["yhat"],data["yhat_lower"],data["yhat_upper"]
    return output
    