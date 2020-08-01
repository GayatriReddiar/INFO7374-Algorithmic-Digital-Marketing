#IMPORT REQUIRED MODULES
import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import json, requests


#READ PRODUCT CSV
prodIDNames = pd.read_csv("ProductIdwithNames.csv")

#LHS METHOD SELECTION CODE
st.sidebar.markdown('**Welcome to the Snackfair!**')

add_selectbox = st.sidebar.selectbox(
    "Select the type of Recommendation Algorithm",
    ("RBM", "SAR")
)

st.markdown('<style>body{background-color: #B8E2F2;}</style>',unsafe_allow_html=True)


if add_selectbox == 'SAR' :
 st.title("**SnackFair's Recommendation System**")
 st.write("-------------------------------------------------------------------------------------------------")
 image = Image.open('reco.jpg')
 st.image(image, caption='',use_column_width=True)
 st.markdown("_Restricted Boltzmann Machine:_  ")
 

 st.subheader("Enter your User ID to get Snack Recommendations!")
 sentence = st.text_input('Input your User ID here:', value='1')
 
 number = int(sentence)


 if st.button('Recommend'):
        with st.spinner('Creating recommendations...'):
            time.sleep(3)
        st.success('Here are your recommended Snacks!')
        payload = json.dumps({
        "userID" : number
  })
        response = requests.get(f"http://127.0.0.1:8000/SARpredict?userID={number}")
        data_dict = response.json()
     
 #Merge with Product data
        b=data_dict['forecast']
        c= list(b.keys())
        d = pd.DataFrame(c)
        d.columns = ['Product_Id']
        d['Product_Id']=d['Product_Id'].astype(int)
        merged_inner = pd.merge(left=d, right=prodIDNames, left_on='Product_Id', right_on='Product_Id')
        merged_inner.columns = ['Product_Id','Snack_Name','Category']
        st.table(merged_inner[['Snack_Name','Category']])

        cats = merged_inner['Category'].unique()

        

elif add_selectbox == 'RBM':
 st.title("**SnackFair's Recommendation System**")
 st.write("-------------------------------------------------------------------------------------------------")
 image = Image.open('reco.jpg')
 st.image(image, caption='', use_column_width=True)
 st.markdown("_Simple Algorithm for Recommendation:_  ")

 st.subheader("Enter your User ID to get Snack Recommendations!")
 sentence = st.text_input('Input your User ID here:', value='1')
 number = int(sentence)
 if st.button('Recommend'):
    with st.spinner('Creating recommendations'):
        time.sleep(3)
    st.success('Here are your recommended Snacks!')
    payload = json.dumps({
    "userID" : number
 })
    response = requests.get(f"http://127.0.0.1:8000/RBMpredict?userID={number}")
    data_dict = response.json()
    #Merge with Product data
    b=data_dict['forecast']
    c= list(b.keys())
    d = pd.DataFrame(c)
    d.columns = ['Product_Id']
    d['Product_Id']=d['Product_Id'].astype(int)
    merged_inner = pd.merge(left=d, right=prodIDNames, left_on='Product_Id', right_on='Product_Id')
    merged_inner.columns = ['Product_Id','Snack_Name','Category']
    st.table(merged_inner[['Snack_Name','Category']])

    cats = merged_inner['Category'].unique()


