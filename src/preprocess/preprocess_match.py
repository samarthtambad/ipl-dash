import pandas as pd # data processing
import json
from collections import defaultdict


temp = pd.read_csv('../assets/data/match_team_mod.csv')


# results = defaultdict(lambda: defaultdict(dict))
# grouped = temp.groupby('season').count()

# for t in grouped.itertuples():
#     for i, key in enumerate(t.Index):
#         if i == 0:
#             nested = results[key]
#         elif i == len(index) - 1:
#             nested[key] = value
#         else:
#             nested = nested[key]




# temp1 = temp.groupby('season').apply(lambda x: x.to_json("batsmen.json", orient='records'))
# print temp.groupby('season').apply(lambda x: x.to_json(orient='records'))

# temp1 = temp.groupby('season').apply()
temp.to_json('match_team.json', orient='records')
# with open('batsmen.json', 'w') as f:
#     f.write(str(temp1))