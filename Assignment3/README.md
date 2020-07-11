# INFO7374-Algorithmic-Digital-Marketing (Assignment 3 - Visual Similarity Search):mag:

## Team Information
| Name        | NEU ID           | 
| ------------- |:-------------:| 
| Gayatri Reddiar      | 001058953 | 
| Rohan Kapadnis | 001342161      |   

## Introduction
Similarity search is the most general term used for a range of mechanisms which share the principle of searching (typically, very large) spaces of objects where the only available comparator is the similarity between any pair of objects. Nearest neighbor search and range queries are important subclasses of similarity search. The most general approach to similarity search relies upon the mathematical notion of metric space, which allows the construction of efficient index structures in order to achieve scalability in the search domain.
We will be implementing following three methods for similarity search of images-
1. **Cosine Similarity:** This algorithm contains both procedures and functions to calculate similarity between sets of data. The function is best used when calculating the similarity between small numbers of sets. The procedures parallelize the computation and are therefore more appropriate for computing similarities on bigger datasets. 
2. **Facebook Artificial Intelligence Similarity Search (FAISS):** A library that allows us to quickly search for multimedia documents that are similar to each other. Facebook has built nearest-neighbor search implementations for billion-scale data sets that are some 8.5x faster than the previous reported state-of-the-art, along with the fastest k-selection algorithm on the GPU known in the literature. 
3. **Spotify Annoy (Approximate Nearest Neighbors Oh Yeah):** Annoy is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data. Annoy has the ability to use static files as indexes which allows us to share indexes across processes.

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


