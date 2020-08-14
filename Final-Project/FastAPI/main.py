from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

from Demand_Forecasting import Demandpredict
from Churn_Prediction import Churnpredict
from Campaign_Prediction import Campaignpredict
from Revenue_Prediction import Revenuepredict

app = FastAPI()


# routes


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/DemandForecasting")
def get_prediction(itemID : int, deptID : int):
    start = time.time()
    prediction_list = Demandpredict(itemID, deptID)
    end = time.time()-start
    print('Predict Time: ',end)
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    start = time.time()
    response_object = {"itemID": itemID, "deptID": deptID, "forecast": prediction_list}
    end = time.time()-start
    print('Response Time: ',end)
    return response_object

@app.get("/ChurnPrediction")
def get_prediction():

    prediction_list = Churnpredict()

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"forecast": prediction_list}
    return response_object

@app.get("/CampaignPrediction")
def get_prediction(budget: int, days: int, fb: int, insta: int, search: int, twitter: int):

    prediction_list = Campaignpredict(budget, days, fb, insta, search, twitter)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"forecast": prediction_list}
    return response_object

@app.get("/RevenuePrediction")
def get_prediction():

    prediction_list = Revenuepredict()

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"forecast": prediction_list}
    return response_object



