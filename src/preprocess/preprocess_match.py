import pandas as pd # data processing
import json

balls_df = pd.read_csv('../assets/data/processed/ball_by_ball__modified.csv')
matches_df = pd.read_csv('../assets/data/processed/matches_modified.csv')

# season = matches_df.groupby('season')
# print season

# for i in xrange(1,10):
#     season = matches_df[matches_df['season'] == i]
#     team_1 = season['team_1']
#     team_1['val'] = 1
#     atotal = team_1.groupby('team_1').sum()
#     team_2 = season['team_2']
#     team_2['val'] = 1
#     btotal = team_2.groupby('team_2').sum()

df = matches_df
del df['date']
del df['venue']
del df['is_superover']
del df['is_duckworthlewis']
del df['first_umpire']
del df['second_empire']
del df['city']
del df['host_country']
df.set_index('match')
# print df.head(13)

matches = df['team_1'].groupby(df['season'])
df2 =  matches.count().reset_index(name = 'count')
print df2

df1 = df[df['season']==1]
# print df1

df1 = df.groupby(['season','team_1']).count()

# df = df1.iloc[:,0:1]
# print df.head()
# df1 = df[['season', 'team_1', 'match']]
