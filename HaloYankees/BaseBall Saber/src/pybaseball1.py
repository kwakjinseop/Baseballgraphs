from pybaseball import statcast



data = statcast(start_dt='2020-09-24', end_dt='2020-09-30')
data.head(2)
data.to_csv("statcast.csv", mode='w')


