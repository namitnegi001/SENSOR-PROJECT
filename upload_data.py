

from pymongo.mongo_client import MongoClient # Changed 'Mongoclient' to 'MongoClient'
import pandas as pd
import json

uri="mongodb+srv://negiamit:28291999@cluster0.29pf7.mongodb.net/?retryWrites=true&w=majority&tls=true"

#create a new client and connect to the server
client=MongoClient(uri)

#create database name and collection name
DATABASE_NAME="amit_negi"
COLLECTION_NAME="waferfault"

df=pd.read_csv("D:\sensor project\notebooks\wafer_23012020_041211.csv")

df.head()

df=df.drop("Unnamed: 0",axis=1)

df

jason_record=list(json.loads(df.T.to_json()).values())

jason_record

type(jason_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(jason_record)