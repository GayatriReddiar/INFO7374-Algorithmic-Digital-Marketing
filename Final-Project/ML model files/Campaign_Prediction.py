import numpy as np
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.ensemble import RandomForestRegressor
from skopt import BayesSearchCV
from skopt.space import Integer, Real
import statsmodels.api as sm
import pandas as pd
import joblib

def Campaignpredict(budget, days, fb, insta, search, twitter):
    data = {'budget': [budget], 'days': [days], 'fb': [fb], 'insta':[insta], 'search':[search], 'twitter':[twitter]}
    df = pd.DataFrame(data, columns = ['budget','days','fb','insta','search','twitter'])
    X = df
    regression1 = joblib.load('impressions_model.pkl')
    #y1 = joblib.load('impressions_actuals.pkl')
    regression2 = joblib.load('purchases_model.pkl')
    #y2 = joblib.load('purchases_actuals.pkl')
    predictions1 = regression1.predict(X).astype(int)
    predictions2 = regression2.predict(X).astype(int)
    conversion = (predictions2/predictions1)*100
    predictions1_df = pd.DataFrame(predictions1,columns=['Impressions'])
    predictions2_df = pd.DataFrame(conversion,columns=['Conversion'])
    predictions_df1 = pd.concat([df, predictions1_df, predictions2_df], axis=1, ignore_index=True)
    predictions_df1.columns = ['Budget','Days','Facebook','Instagram','GoogleSearch','Twitter','Impressions','Conversion']
    prediction_list = predictions_df1.to_dict("records")
    output = {}
    for data in prediction_list:
        rate = data["Conversion"]
        output[rate] = data["Impressions"],data["Budget"],data["Days"],data["Facebook"],data["Instagram"],data["GoogleSearch"],data["Twitter"]
    return output