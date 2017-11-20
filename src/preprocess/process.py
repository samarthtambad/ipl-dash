import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

matches = pd.read_csv('../assets/data/matches_mod.csv')
# print matches.head()
# ------------------------------------------------------------------------------------

deliveries = pd.read_csv('../assets/data/deliveries_mod.csv')
# print deliveries.head()

# ------------------------------------------------------------------------------------
# Teams Match

matches_season = matches.groupby(['season', 'team1'])['toss_winner'].count().reset_index()
matches_team2 = matches.groupby(['season', 'team2'])['toss_winner'].count().reset_index()
matches_season["toss_winner"] = matches_season["toss_winner"] + matches_team2["toss_winner"] 
matches_season.columns = ["season", "team", "matches"]

matches_win = matches.groupby(['season', 'winner'])['toss_winner'].count().reset_index()
matches_win.columns = ['season', 'team', 'wins']
matches_season = matches_season.merge(matches_win, left_on=["season", "team"], 
                        right_on=["season", "team"], how="left")
matches_season["losses"] = matches_season["matches"] - matches_season["wins"]
matches_season["pts"] = matches_season['wins'] * 2  

toss_bat = np.where((matches['toss_decision'] == "bat"), 1, 0)
matches["toss_bat"] = toss_bat
toss_field = np.where((matches['toss_decision'] == "field"), 1, 0)
matches["toss_field"] = toss_field

matches_toss = matches.groupby(['season', 'toss_winner'])['team1'].count().reset_index()
matches_season['toss_wins'] = matches_toss["team1"]
matches_wtbf = matches.groupby(['season', 'toss_winner'])['toss_bat'].sum().reset_index()
matches_season['toss_win_bat_first'] = matches_wtbf["toss_bat"]
matches_wtff = matches.groupby(['season', 'toss_winner'])['toss_field'].sum().reset_index()
matches_season['toss_win_field_first'] = matches_wtff["toss_field"]

matches_bfwm = matches.groupby(['season', 'winner'])['toss_bat'].sum().reset_index()
matches_season['bat_first_win_match'] = matches_bfwm["toss_bat"]
matches_ffwm = matches.groupby(['season', 'winner'])['toss_field'].sum().reset_index()
matches_season['field_first_win_match'] = matches_ffwm["toss_field"]
matches_season =  matches_season.groupby('season').apply(pd.DataFrame.sort_values, 'pts', ascending=False)

matches_season['toss_win_bat_first'] = np.round((matches_season['toss_win_bat_first'] / matches_season['toss_wins']) * 100 , 2)
matches_season['toss_win_field_first'] = np.round((matches_season['toss_win_field_first'] / matches_season['toss_wins']) * 100 , 2)
matches_season['bat_first_win_match'] = np.round((matches_season['bat_first_win_match'] / matches_season['wins']) * 100 , 2)
matches_season['field_first_win_match'] = np.round((matches_season['field_first_win_match'] / matches_season['wins']) * 100 , 2)

# matches_season.to_csv("../assets/data/match_team_mod.csv", index=False)

# print matches_season.head()

# ------------------------------------------------------------------------------------
# Total Calculations

season_total = matches_season.groupby('season')['matches', 'wins', 'toss_wins', 'toss_win_bat_first', 'toss_win_field_first', 'bat_first_win_match', 'field_first_win_match'].sum()

season_total['toss_win_bat_first'] = np.round((season_total['toss_win_bat_first'] / 8) , 2)
season_total['toss_win_field_first'] = np.round((season_total['toss_win_field_first'] / 8) , 2)
season_total['bat_first_win_match'] = np.round((season_total['bat_first_win_match'] / 8) , 2)
season_total['field_first_win_match'] = np.round((season_total['field_first_win_match'] / 8) , 2)

# season_total.to_csv("../assets/data/season_total_mod.csv", index=True)

# print season_total.head()

# ------------------------------------------------------------------------------------
# Batsmen

batsman_grp = deliveries.groupby(["match_id", "inning", "batting_team", "batsman"])
batsmen = batsman_grp["batsman_runs"].sum().reset_index()

# Ignore the wide balls.
balls_faced = deliveries[deliveries["wide_runs"] == 0]
balls_faced = balls_faced.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
balls_faced.columns = ["match_id", "inning", "batsman", "balls_faced"]
batsmen = batsmen.merge(balls_faced, left_on=["match_id", "inning", "batsman"], 
                        right_on=["match_id", "inning", "batsman"], how="left")

fours = deliveries[ deliveries["batsman_runs"] == 4]
sixes = deliveries[ deliveries["batsman_runs"] == 6]

fours_per_batsman = fours.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()
sixes_per_batsman = sixes.groupby(["match_id", "inning", "batsman"])["batsman_runs"].count().reset_index()

fours_per_batsman.columns = ["match_id", "inning", "batsman", "4s"]
sixes_per_batsman.columns = ["match_id", "inning", "batsman", "6s"]

batsmen = batsmen.merge(fours_per_batsman, left_on=["match_id", "inning", "batsman"], 
                        right_on=["match_id", "inning", "batsman"], how="left")
batsmen = batsmen.merge(sixes_per_batsman, left_on=["match_id", "inning", "batsman"], 
                        right_on=["match_id", "inning", "batsman"], how="left")
batsmen['SR'] = np.round(batsmen['batsman_runs'] / batsmen['balls_faced'] * 100, 2)

for col in ["batsman_runs", "4s", "6s", "balls_faced", "SR"]:
    batsmen[col] = batsmen[col].fillna(0)

dismissals = deliveries[ pd.notnull(deliveries["player_dismissed"])]
dismissals = dismissals[["match_id", "inning", "player_dismissed", "dismissal_kind", "fielder"]]
dismissals.rename(columns={"player_dismissed": "batsman"}, inplace=True)
batsmen = batsmen.merge(dismissals, left_on=["match_id", "inning", "batsman"], 
                        right_on=["match_id", "inning", "batsman"], how="left")

batsmen = matches[['id','season']].merge(batsmen, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
# print batsmen.head(5)

batsmen_season = batsmen.groupby(["season", "batsman"])["batsman_runs"].count().reset_index()
batsmen_season.columns = ["season", "batsman", "matches"]
batsmen_balls = batsmen.groupby(["season", "batsman"])["balls_faced"].sum().reset_index()
batsmen_season= batsmen_season.merge(batsmen_balls, left_on=["season", "batsman"], 
                        right_on=["season", "batsman"], how="left")
batsmen_runs = batsmen.groupby(["season", "batsman"])["batsman_runs"].sum().reset_index()
batsmen_season= batsmen_season.merge(batsmen_runs, left_on=["season", "batsman"], 
                        right_on=["season", "batsman"], how="left")
batsmen_4s = batsmen.groupby(["season", "batsman"])["4s"].sum().reset_index()
batsmen_season= batsmen_season.merge(batsmen_4s, left_on=["season", "batsman"], 
                        right_on=["season", "batsman"], how="left")   
batsmen_6s = batsmen.groupby(["season", "batsman"])["6s"].sum().reset_index()
batsmen_season= batsmen_season.merge(batsmen_6s, left_on=["season", "batsman"], 
                        right_on=["season", "batsman"], how="left")  
 
batsmen_season['Avg'] = np.round(batsmen_season['batsman_runs'] / batsmen_season['matches'] , 2)                        
batsmen_season['SR'] = np.round(batsmen_season['batsman_runs'] / batsmen_season['balls_faced'] * 100, 2)    
for col in ["matches", "balls_faced", "batsman_runs", "4s", "6s", "Avg", "SR"]:
    batsmen_season[col] = batsmen_season[col].fillna(0)
batsmen_season =  batsmen_season.groupby('season').apply(pd.DataFrame.sort_values, 'batsman_runs', ascending=False)
batsmen_season =   batsmen_season.groupby("season").head(10)
# batsmen_season.to_csv("../assets/data/batsmen_mod.csv", index=False)

# print batsmen_season
# ------------------------------------------------------------------------------------
# Bowlers

bowler_grp = deliveries.groupby(["match_id", "inning", "bowling_team", "bowler", "over"])
bowlers = bowler_grp["total_runs", "wide_runs", "bye_runs", "legbye_runs", "noball_runs"].sum().reset_index()

bowlers["runs"] = bowlers["total_runs"] - (bowlers["bye_runs"] + bowlers["legbye_runs"])
bowlers["extras"] = bowlers["wide_runs"] + bowlers["noball_runs"]

del( bowlers["bye_runs"])
del( bowlers["legbye_runs"])
del( bowlers["total_runs"])

dismissal_kinds_for_bowler = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]
dismissals = deliveries[deliveries["dismissal_kind"].isin(dismissal_kinds_for_bowler)]
dismissals = dismissals.groupby(["match_id", "inning", "bowling_team", "bowler", "over"])["dismissal_kind"].count().reset_index()
dismissals.rename(columns={"dismissal_kind": "wickets"}, inplace=True)

bowlers = bowlers.merge(dismissals, left_on=["match_id", "inning", "bowling_team", "bowler", "over"], 
                        right_on=["match_id", "inning", "bowling_team", "bowler", "over"], how="left")
bowlers["wickets"] = bowlers["wickets"].fillna(0)

bowlers_over = bowlers.groupby(['match_id', 'inning', 'bowling_team', 'bowler'])['over'].count().reset_index()
bowlers = bowlers.groupby(['match_id', 'inning', 'bowling_team', 'bowler']).sum().reset_index().drop('over', 1)
bowlers = bowlers_over.merge(bowlers, on=["match_id", "inning", "bowling_team", "bowler"], how = 'left')
bowlers['Econ'] = np.round(bowlers['runs'] / bowlers['over'] , 2)
bowlers = matches[['id','season']].merge(bowlers, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
bowlers["matches"] = 1

bowlers_season = bowlers.groupby(['season', 'bowler'])['matches'].count().reset_index()
bowlers_overs = bowlers.groupby(['season', 'bowler'])['over'].sum().reset_index()
bowlers_season = bowlers_season.merge(bowlers_overs, left_on=["season", "bowler"], 
                        right_on=["season", "bowler"], how="left")
bowlers_runs = bowlers.groupby(['season', 'bowler'])['runs'].sum().reset_index()
bowlers_season = bowlers_season.merge(bowlers_runs, left_on=["season", "bowler"], 
                        right_on=["season", "bowler"], how="left")
bowlers_wickets = bowlers.groupby(['season', 'bowler'])['wickets'].sum().reset_index()
bowlers_season = bowlers_season.merge(bowlers_wickets, left_on=["season", "bowler"], 
                        right_on=["season", "bowler"], how="left")
bowlers_econ = bowlers.groupby(['season', 'bowler'])['Econ'].sum().reset_index()
bowlers_season = bowlers_season.merge(bowlers_econ, left_on=["season", "bowler"], 
                        right_on=["season", "bowler"], how="left")

bowlers_season['Econ'] = np.round(bowlers_season['Econ'] / bowlers_season['matches'] , 2)
bowlers_season['Avg'] = np.round(bowlers_season['runs'] / bowlers_season['wickets'] ,decimals=3)
bowlers_season = bowlers_season[bowlers_season["wickets"] != 0]

for col in ["matches", "over", "runs", "wickets", "Econ", "Avg"]:
    bowlers_season[col] = bowlers_season[col].fillna(0)

bowlers_season =  bowlers_season.groupby('season').apply(pd.DataFrame.sort_values, 'wickets', ascending=False)
bowlers_season =   bowlers_season.groupby("season").head(10)
# bowlers_season.to_csv("../assets/data/bowlers_mod.csv", index=False)

# print bowlers_season
# ------------------------------------------------------------------------------------

batsman_runsperseason = batsmen.groupby(['season', 'batting_team', 'batsman'])['batsman_runs'].sum().reset_index()
batsman_runsperseason = batsman_runsperseason.groupby(['season', 'batsman'])['batsman_runs'].sum().unstack().T
batsman_runsperseason['Total'] = batsman_runsperseason.sum(axis=1) #add total column to find batsman with the highest runs
batsman_runsperseason = batsman_runsperseason.sort_values(by = 'Total', ascending = False).drop('Total', 1)
# print batsman_runsperseason