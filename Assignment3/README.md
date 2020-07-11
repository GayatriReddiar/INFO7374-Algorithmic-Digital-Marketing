# INFO7374-Algorithmic-Digital-Marketing (Assignment 3 - Visual Similarity Search):sunglasses:

## Team Information
| Name        | NEU ID           | 
| ------------- |:-------------:| 
| Gayatri Reddiar      | 001058953 | 
| Rohan Kapadnis | 001342161      |   

## Claat Link
(*https://codelabs-preview.appspot.com/?file_id=1zO_z8iwZpmQ-d7FugY5c7bvaCRmJpKjuff8pT2OD4Cw#7*)

## Google Doc Link
(*https://docs.google.com/document/d/1zO_z8iwZpmQ-d7FugY5c7bvaCRmJpKjuff8pT2OD4Cw/edit?ts=5f07ea3c#*)

## Dataset
A total of 8 datasets form a basis of the DunnHumby data. Below are the different tables-
1. **train.bson** - Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format.
2. **train_example.bson** - Contains the first 100 records of train.bson for exploring the dataset before downloading the entire file.
3. **test.bson** - Contains a list of 1,768,182 products in the same format as train.bson, except there is no category_id included. The objective of the competition is to predict the correct category_id from the picture(s) of each product id (_id). The category_ids that are present in Private Test split are also all present in the Public Test split.

**Link to Datasets:** *https://www.kaggle.com/c/cdiscount-image-classification-challenge*

## Streamlit App
*https://similarity-search.herokuapp.com/*

![alt text](https://github.com/GayatriReddiar/INFO7374-Algorithmic-Digital-Marketing/blob/master/Assignment3/StreamlitApp2.png) 

![alt text](https://github.com/GayatriReddiar/INFO7374-Algorithmic-Digital-Marketing/blob/master/Assignment3/StreamlitApp1.png) 


