from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pandas import DataFrame

data=playerid_lookup('bauer', 'trevor')

data1 = playerid_lookup(['mlb_played_first'])
print(data1)
