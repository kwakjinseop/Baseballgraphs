import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

data = pd.read_csv('../data/pitch_movement.csv')


df = DataFrame(data, columns=['first_name','last_name', 'pitcher_break_z', 'pitcher_break_x'])

df_sort=df.sort_values(by='pitcher_break_z', ascending=False);
df_sort2=df.sort_values(by='pitcher_break_x', ascending=False);

aaa=df_sort.iloc[0:50];
aaa1=df_sort2.iloc[0:50];


print(aaa)
print(aaa1)


