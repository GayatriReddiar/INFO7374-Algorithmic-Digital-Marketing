import pandas as pd
import numpy as np
import joblib
#from xgboost import XGBClassifier

def Churnpredict():
    xgb_mdl = joblib.load('Best_Churn_Model')
    X_test = joblib.load('Churn_Data')
    y_pred = xgb_mdl.predict(X_test.values)
    cust = X_test['customer_id'].unique()
    cust_id = pd.DataFrame(cust, columns = ['customer_id'])
    churn = pd.DataFrame(y_pred, columns = ['Churn'])
    churn_df = pd.concat([cust_id, churn], axis=1)
    prediction_list = churn_df.to_dict("records")
    output = {}
    for data in prediction_list:
        customer = data["customer_id"]
        output[customer] = data["Churn"]
    return output