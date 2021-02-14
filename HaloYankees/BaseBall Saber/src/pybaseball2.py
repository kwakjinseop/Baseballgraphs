from pybaseball import salaries
from pybaseball import statcast_pitcher
data=salaries()
data.to_csv("salary.csv", mode='w')

