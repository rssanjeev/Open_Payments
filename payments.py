import pandas as pd
import urllib.request, json 
from urllib.request import urlopen
from pandas.io.json import json_normalize

#dev_data_url = 'https://openpaymentsdata.cms.gov/resource/ap6w-xznw.json'
#dev_data = pd.read_json(dev_data_url)
#dev_data.to_csv('Datasets.csv')

#Making a few changes to the above imported dataset to get the file names in a new column. Reading the modified dataset again 

dev_data = pd.read_csv("Datasets.csv")


File_Names = dev_data['File_Name'].tolist()
Api_Endpoints = dev_data['api_endpoint'].tolist()



for x,y in zip(File_Names, Api_Endpoints):
    globals()[name] = pd.read_json(y)

General_Payment_Data_2013 = pd.read_json('https://openpaymentsdata.cms.gov/resource/gtwa-6ahd.json')
General_Payment_Data_2013.head()