# INFO7374-Algorithmic-Digital-Marketing (Assignment 3 - Visual Similarity Search)

## Team Information
| Name        | NEU ID           | 
| ------------- |:-------------:| 
| Gayatri Reddiar      | 001058953 | 
| Rohan Kapadnis | 001342161      |   

## Claat Link
()

## Google Doc Link
()

## Dataset
A total of 8 datasets form a basis of the DunnHumby data. Below are the different tables-
1. train.bson - Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format.
2. train_example.bson - Contains the first 100 records of train.bson for exploring the dataset before downloading the entire file.
3. test.bson - Contains a list of 1,768,182 products in the same format as train.bson, except there is no category_id included. The objective of the competition is to predict the correct category_id from the picture(s) of each product id (_id). The category_ids that are present in Private Test split are also all present in the Public Test split.

## Streamlit App
https://similarity-search.herokuapp.com/

https://github.com/GayatriReddiar/INFO7374-Algorithmic-Digital-Marketing/blob/master/Assignment3/StreamlitApp1.png

