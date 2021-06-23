from numpy.core.numeric import full
import pandas as pd
import urllib.request, json 
from urllib.request import urlopen
from pandas.io.json import json_normalize
#import sodapy import Socrata
#python -m pip install sodapy

#dev_data_url = 'https://openpaymentsdata.cms.gov/resource/ap6w-xznw.json'
#dev_data = pd.read_json(dev_data_url)
#dev_data.to_csv('Datasets.csv')

#Making a few changes to the above imported dataset to get the file names in a new column. Reading the modified dataset again 

dev_data = pd.read_csv("Datasets.csv")


File_Names = dev_data['File_Name'].tolist()
Api_Endpoints = dev_data['api_endpoint'].tolist()



#for x,y in zip(File_Names, Api_Endpoints):
#    globals()[name] = pd.read_json(y)

#G2013 = pd.read_json('https://openpaymentsdata.cms.gov/resource/gtwa-6ahd.json')
G2013 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2013_Reporting_Year.csv', nrows=1000)

#G2014 = pd.read_json('https://openpaymentsdata.cms.gov/resource/usfr-9d94.json')
G2014 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2014_Reporting_Year.csv', nrows=1000)

#G2015 = pd.read_json('https://openpaymentsdata.cms.gov/resource/wvg5-mk6b.json')
G2015 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2015_Reporting_Year.csv', nrows=1000)

#G2016 = pd.read_json('https://openpaymentsdata.cms.gov/resource/utn9-gvfr.json')
G2016 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2016_Reporting_Year.csv', nrows=1000)

#G2017 = pd.read_json('https://openpaymentsdata.cms.gov/resource/6e8i-9z2m.json')
G2017 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2017_Reporting_Year.csv', nrows=1000)

#G2018 = pd.read_json('https://openpaymentsdata.cms.gov/resource/neeg-3s2r.json')
G2018 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2018_Reporting_Year.csv', nrows=1000)

#G2019 = pd.read_json('https://openpaymentsdata.cms.gov/resource/svgu-ws3x.json')
G2019 = pd.read_csv('General_Payment_Data___Detailed_Dataset_2019_Reporting_Year.csv', nrows=1000)

G2013_Col = G2013.columns.tolist()
for x in range(len(G2013_Col)):
    G2013_Col[x] = G2013_Col[x].upper()

G2014_Col = G2014.columns.tolist()
for x in range(len(G2014_Col)):
    G2014_Col[x] = G2014_Col[x].upper()

G2015_Col = G2015.columns.tolist()
for x in range(len(G2015_Col)):
    G2015_Col[x] = G2015_Col[x].upper()

G2016_Col = G2016.columns.tolist()
for x in range(len(G2016_Col)):
    G2016_Col[x] = G2016_Col[x].upper()

G2017_Col = G2017.columns.tolist()
for x in range(len(G2017_Col)):
    G2017_Col[x] = G2017_Col[x].upper()

G2018_Col = G2018.columns.tolist()
for x in range(len(G2018_Col)):
    G2018_Col[x] = G2018_Col[x].upper()

G2019_Col = G2019.columns.tolist()
for x in range(len(G2019_Col)):
    G2019_Col[x] = G2019_Col[x].upper()

data_columns = pd.DataFrame({'G2013_Col': pd.Series(G2013_Col), 'G2014_Col': pd.Series(G2014_Col), 'G2015_Col': pd.Series(G2015_Col), 'G2016_Col': pd.Series(G2016_Col), 'G2017_Col': pd.Series(G2017_Col), 'G2018_Col': pd.Series(G2018_Col), 'G2019_Col': pd.Series(G2019_Col)})
data_columns.to_csv('data_columns.csv')

#Testing by combining 2 eneven dataframes
full_data = pd.concat([G2013,G2014,G2015,G2016,G2017,G2018,G2019])
full_data_Col = full_data.columns.tolist()
for x in range(len(full_data_Col)):
    full_data_Col[x] = full_data_Col[x].upper()
full_data.columns = full_data_Col
len(full_data)
full_data.to_csv('full_data.csv')