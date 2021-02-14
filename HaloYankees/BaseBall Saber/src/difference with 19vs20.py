import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import csv
import numpy as np
# def extract_firstname(value):
#     value.split()
    # print(value.split())
    # return value.split()[-1]
    # return 'a'



data=pd.read_csv('../data/player_no.csv')
data1=pd.read_csv('../data/spinrate2019ver.csv')
data2=pd.read_csv('../data/spinrate2020ver.csv')
data3 = pd.read_csv('../data/pitch_movement minimum250.csv')
data4 = pd.read_csv('../data/pitch_movement minimum250 19ver.csv')


# print(data.columns.values)
data33=data.columns.values
df=pd.DataFrame(data33, columns=['text'])
df['last_name'] = df.text.str.split(' ').str[1] #last_name만 따로 데이터에 담아두었음.
print(df['last_name'])
print("------------------------------------------------------------------------")

# print(df['last_name'].values)

last_names = df['last_name'].values
for lastname in last_names:
    tmp=data4[data4['last_name'] == lastname]
    tmp=tmp['rise']
# print('Bieber' in last_names)

    print(tmp)
# if df['last_name'][0]==data4['last_name']:
print("===============================================================")
for lastname in last_names:
    tmp2=data3[data3['last_name']==lastname]
    tmp2=tmp2['rise']

    print(tmp2)


# data=data[data['player_name']=='Corbin Burnes']
# data1['player_name']=data1['player_name'].apply(extract_firstname)
# print(data1['player_name'])

