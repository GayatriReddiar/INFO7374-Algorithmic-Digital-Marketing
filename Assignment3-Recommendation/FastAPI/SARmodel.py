#load libraries

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from pathlib import Path

# set the environment path to find Recommenders
import sys
sys.path.append("../../")

import logging
import numpy as np
import pandas as pd
#import papermill as pm

from reco_utils.dataset.python_splitters import python_stratified_split
from reco_utils.evaluation.python_evaluation import map_at_k, ndcg_at_k, precision_at_k, recall_at_k
from reco_utils.recommender.sar.sar_singlenode import SARSingleNode

import pickle
import joblib

#Read Product Data
#pdt_df = pd.read_csv('ProductData.csv')

def SARtrain():
    data = pd.read_csv("SnacksData100.csv")
    data.loc[:, 'Ratings'] = data['Ratings'].astype(np.float32)
    header = {
    "col_user": "userId",
    "col_item": "Product_Id",
    "col_rating": "Ratings",
    "col_timestamp": "timestamp",
    }
    train, test = python_stratified_split(data, ratio=0.75, col_user=header["col_user"], col_item=header["col_item"], seed=42)
    joblib.dump(test, 'testdata')
    logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)-8s %(message)s')
    model = SARSingleNode(
    similarity_type="jaccard", 
    time_decay_coefficient=30, 
    time_now=None, 
    timedecay_formula=True, 
    **header
    )
    model.fit(train)
    joblib.dump(model, 'SARDump')
    #pickle.dump(model, open(algo, 'wb'))
    
def SARpredict(userID):
    loaded_model = joblib.load('SARDump')
    test = joblib.load('testdata')
    top_k = loaded_model.recommend_k_items(test, remove_seen=True)
    df1 = top_k[top_k['userId'] == userID]
    df2=df1.sort_values(by=['prediction'], ascending=False).head(10)
    df3=pd.DataFrame(df2)
    #merge_df = pd.merge(df3,pdt_df,how='inner',on=['Product_Id'])
    sar_df = df3[['Product_Id','prediction']]
    
    return sar_df.to_dict("records")

def SARconvert(prediction_list):
    output = {}
    for data in prediction_list:
        user = data["Product_Id"]
        output[user] = data["prediction"]
    return output