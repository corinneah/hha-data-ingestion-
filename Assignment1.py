# SECTION 1 
# import packages
from unittest import result
import pandas as pd
import xlrd
# Downloaded xls dataset with two+ tabs
# to read xls file df = 
df = pd.read_excel('/Users/corinne/Documents/GitHub/hha-data-ingestion-/Data/dataset3.xls')
df 
# to read tabs in dataset, used the command
xls = xlrd.open_workbook('/Users/corinne/Documents/GitHub/hha-data-ingestion-/Data/dataset3.xls', on_demand=True)
xls.sheet_names()
# define tab 1 and tab 2
tab1 = pd.read_excel('/Users/corinne/Documents/GitHub/hha-data-ingestion-/Data/dataset3.xls', sheet_name='dataset')
tab2 = pd.read_excel('/Users/corinne/Documents/GitHub/hha-data-ingestion-/Data/dataset3.xls', sheet_name='dataset2')

# SECTION 2
# import packages 
import json
import requests
# set 'data' to the online CMS api data link 
data=requests.get('https://data.cms.gov/data-api/v1/dataset/b9d03601-1187-4c25-aca6-5754e88ba0cf/data')
data=data.json()

#SECTION 3
#import packages
from google.cloud import bigquery
# connect variable to key 
client = bigquery.Client.from_service_account_json('/Users/corinne/Documents/Github/hha-data-ingestion-/adroit-producer-361019-747cf9ceb67a.json')
# query public dataset 1 
query_job = client.query("SELECT * FROM `bigquery-public-data.google_ads.geotargets` LIMIT 100")
# For results 
results = query_job.result()
bigquery1 = pd.DataFrame(results.to_dataframe())
# query public dataset 2 
client = bigquery.Client.from_service_account_json('/Users/corinne/Documents/Github/hha-data-ingestion-/adroit-producer-361019-747cf9ceb67a.json')
query_job = client.query("SELECT * FROM `bigquery-public-data.austin_waste.waste_and_diversion` LIMIT 100")
results = query_job.result()
bigquery2 = pd.DataFrame(results.to_dataframe())