#load libraries

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from pathlib import Path

# set the environment path to find Recommenders
import sys
sys.path.append("../../")

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

import papermill as pm

from reco_utils.recommender.rbm.rbm import RBM
from reco_utils.dataset.python_splitters import numpy_stratified_split
from reco_utils.dataset.sparse import AffinityMatrix


from reco_utils.dataset import movielens
from reco_utils.evaluation.python_evaluation import map_at_k, ndcg_at_k, precision_at_k, recall_at_k
#import pickle
import joblib

#For interactive mode only
#%load_ext autoreload
#%autoreload 2

#Read Product Data
#pdt_df = pd.read_csv('ProductData.csv')

def RBMtrain():
    data = pd.read_csv("SnacksData100.csv")
    header = {
        "col_user": "userId",
        "col_item": "Product_Id",
        "col_rating": "Ratings",
    }
    am = AffinityMatrix(DF = data, **header)
    X = am.gen_affinity_matrix()
    Xtr, Xtst = numpy_stratified_split(X)
    model = RBM(hidden_units= 600, training_epoch = 30, minibatch_size= 60, keep_prob=0.9,with_metrics =True)
    model.fit(Xtr, Xtst)
    top_k, test_time =  model.recommend_k_items(Xtst)
    top_k_df = am.map_back_sparse(top_k, kind = 'prediction')
    test_df = am.map_back_sparse(Xtst, kind = 'ratings')
    joblib.dump(top_k_df, 'testdata')
    
def RBMpredict(userID):
    test = joblib.load('testdata')
    df1 = test[test['userId'] == userID]
    df2=df1.sort_values(by=['prediction'], ascending=False).head(10)
    df3=pd.DataFrame(df2)
    #merge_df = pd.merge(df3,pdt_df,how='inner',on=['Product_Id'])
    rbm_df = df3[['Product_Id','prediction']]
    return rbm_df.to_dict("records")

def RBMconvert(prediction_list):
    output = {}
    for data in prediction_list:
        user = data["Product_Id"]
        output[user] = data["prediction"]
    return output