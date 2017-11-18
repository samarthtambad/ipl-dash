import pandas as pd # data processing
import json

balls_df = pd.read_csv('../assets/data/csv_files/processed/ball_by_ball__modified.csv')
matches_df = pd.read_csv('../assets/data/csv_files/processed/matches_modified.csv')

# season = matches_df.groupby('season')
# print season

print matches_df.to_json()

for i in xrange(1,10):
    season = matches_df[matches_df['season'] == i]
    team_1 = season['team_1']
    team_1['val'] = 1
    atotal = team_1.groupby('team_1').sum()
    team_2 = season['team_2']
    team_2['val'] = 1
    btotal = team_2.groupby('team_2').sum()