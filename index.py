from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import pandas as pd
import numpy as np
#import plotly.express as px
#import plotly
from datetime import date, datetime
#import datapackage
import csv
import requests
import matplotlib.pyplot as plt
#==============================================================================================================================
#Tasks:
#A
#change unix timestamp in dataFrame to a number based on date i.e. 08012019 instead of 1564704000000

#create new data frames
#2019 yearly and monthly dataFrames
#df_2019 = ?
#df_August_2019 = ?

#2020 dataFrame

#2021 dataFrame

#B
#Tensorflow idea

#C
#jupyter notebook in google colab

#D
#use matplotlib to make a graph in step 4
 
#==============================================================================================================================

#1. 
# Get data. https://datahub.io/cryptocurrency/bitcoin#pandas
#from datapackage import Package

#package = Package('https://datahub.io/cryptocurrency/bitcoin/datapackage.json')

# print list of all resources:
#pprint.pprint(package.resource_names)

# print processed tabular data (if exists any)
#for resource in package.resources:
   # if resource.descriptor['datahub']['type'] == 'derived/csv':
   #     pprint.pprint(resource.read())
 

#Use CoinCap API to request historical data
url = 'http://api.coincap.io/v2/assets/bitcoin/history?interval=d1'#&start=1592585794000&end=1613753794000' #can we use a variable for the unix time 1592585794000 ? 1613753794000

#payload = {}
#headers = {}

#response = requests.request("GET", url, headers=headers, data=payload)

#json_data = json.loads(response.text.encode('utf8'))
#bitcoin_data = json_data["data"]

#2
# create pandas dataframe
#df = pd.DataFrame(bitcoin_data)
#df.to_csv('bitcoin-data', index=False)

df = pd.read_csv('bitcoin-data')

print(df['date'])

#show sample of data
#print(df.sample)
#show data types
#print(df.dtypes)

#create new data frame, from August 2019 to July 2021
#df = pd.DataFrame(bitcoin_data, columns=['time', 'priceUSD'])
#convert priceUSD from type object to float
#df['priceUSD'] = pd.to_numeric(df['priceUSD'], errors='coerce').fillna(0, downcast='infer')
#show data types
#print(df.dtypes)

#print(df.info)


#3. 
# make separate file with the Euler game theory strategy. 

#4. 
# make graphs to visualize the price


#What we used:

#https://docs.coincap.io/
#https://www.youtube.com/watch?v=EoW4XFdh7gc

df2019 = df[df['date'].str.contains('2019')]
df2020 = df[df['date'].str.contains('2020')]
df2021 = df[df['date'].str.contains('2021')]