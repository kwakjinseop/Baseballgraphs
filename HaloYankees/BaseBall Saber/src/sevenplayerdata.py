import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data3 = pd.read_csv('../data/pitch_movement minimum250 19ver.csv');
data4=pd.read_csv('../data/pitch_movement minimum250.csv');
data2 = pd.read_csv('../data/seven.csv');


# data33 = data2.columns.values;
# df=pd.DataFrame(data33, columns=['text'])
# print(df)




diff_x = data4[data4['last_name'] == 'Scherzer']['diff_x'].value_counts()
diff_z = data4[data4['last_name'] == 'Scherzer']['diff_z'].value_counts()
avg_speed = data4[data4['last_name'] == 'Scherzer']['avg_speed'].value_counts()
tail = data4[data4['last_name'] == 'Scherzer']['tail'].value_counts()

data111=diff_x.cumsum(axis=0)
data222=diff_z.cumsum(axis=0)
data333=avg_speed.cumsum(axis=0)
data444=tail.cumsum(axis=0)

index = pd.date_range("2019", "2020")
wide_df = pd.DataFrame(data111, data222, data333, data444, index)
wide_df.head()
print(wide_df)

dataframe = pd.DataFrame(diff_x.cumsum(axis=0),diff_z.cumsum(axis=0),avg_speed.cumsum(axis=0),tail.cumsum(axis=0),
                         columns=["diff_x","diff_z","avg_speed", "tail"], index = pd.date_range("2019","2020"))

dataframe.plot()
plt.show()
# df = pd.DataFrame([diff_x, diff_z, avg_speed, tail])
# df.index=['2019','2020','2011','2601']
# print(df)
# df.plot(kind='bar')
# plt.show()