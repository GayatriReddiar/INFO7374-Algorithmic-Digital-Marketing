from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from SARmodel import SARconvert, SARpredict
from RBMmodel import RBMconvert, RBMpredict

app = FastAPI()


# routes


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/SARpredict")#, response_model=StockOut, status_code=200)
def get_prediction(userID : int):
    #userID = payload.userID

    prediction_list = SARpredict(userID)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"userID": userID, "forecast": SARconvert(prediction_list)}
    return response_object

@app.get("/RBMpredict")#, response_model=StockOut, status_code=200)
def get_prediction(userID : int):
  

    prediction_list = RBMpredict(userID)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="User not found.")

    response_object = {"userID": userID, "forecast": RBMconvert(prediction_list)}
    return response_object

