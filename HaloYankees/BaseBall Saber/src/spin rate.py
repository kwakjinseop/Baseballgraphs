import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import csv
import numpy as np

data = pd.read_csv('../data/savant_data.csv')
data1 = pd.read_csv('../data/Pitcher LeaderBoard.csv')
data2 = pd.read_csv('../data/Vertical Realease Z.csv')
data3 = pd.read_csv('../data/spinrate2019ver.csv')
data4 = pd.read_csv('../data/spinrate2020ver.csv')




df = DataFrame(data4, columns=['player_name', 'total_pitches', 'spin_rate'])
df_sort=df.sort_values(by='total_pitches', ascending=False);
firstaa= df_sort.iloc[0:10]
data2020= firstaa.sort_values(by='spin_rate', ascending=False);
aaa=data2020.iloc[0:10];

cleardata1 = DataFrame(aaa, columns=['player_name'])
# print(cleardata1['player_name'].values)




df2= DataFrame(data3, columns=['player_name', 'total_pitches', 'spin_rate'])
df_sort2=df2.sort_values(by='total_pitches', ascending=False);
firstbb = df_sort2.iloc[0:10]
data2019=firstbb.sort_values(by='spin_rate', ascending=False);
bbb=data2019.iloc[0:10];

cleardata2 = DataFrame(bbb, columns=['player_name'])

print(cleardata2)

result=[]
result2=[]
for player_name in cleardata1['player_name'].values:

    if not cleardata2[cleardata2['player_name']==player_name].empty:
        result.append(player_name)
    else:
        result2.append(player_name)



with open('player_yes.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(result)

with open('player_no.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(result2)
print(kkk)
print(result2)


print(aaa)
print("====================================================================")
print(bbb)


df_vertical = DataFrame(data2, columns=[])
print(aaa)


