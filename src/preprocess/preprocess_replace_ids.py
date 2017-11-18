import csv

def readCSV(path):
    f = open(path)
    f_reader = csv.reader(f)
    f_list = list(f_reader)
    f.close()
    return f_list

def writeCSV(name, mylist):
    with open(name, 'wb') as myfile:
        for row in mylist:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(row)

# -------------------------Load Unprocessed CSV-------------------------
ball_by_ball = readCSV('../assets/data/csv_files/Ball_by_Ball.csv')
player_match = readCSV('../assets/data/csv_files/Player_Match.csv')
players = readCSV('../assets/data/csv_files/Player.csv')
seasons = readCSV('../assets/data/csv_files/Season.csv')
matches = readCSV('../assets/data/csv_files/Match.csv')
teams = readCSV('../assets/data/csv_files/Team.csv')
# ----------------------------------------------------------------------

# For Matches
col = ['match', 'date', 'team_1', 'team_2', 'season', 'venue', 'toss_winner', 'toss_decision', 'is_superover', 'is_result', 'is_duckworthlewis', 'win_type', 'won_by', 'winner', 'mom', 'first_umpire', 'second_empire', 'city', 'host_country']
match_mod = []
num_match = 1
match_mod.append(col)
for match in matches[1:]:
    match[0] = num_match
    num_match = num_match + 1
    for team in teams[1:]:
        #team name
        if match[2] == team[0]:
            match[2] = team[1]
        #opponent name
        if match[3] == team[0]:
            match[3] = team[1]
        #toss winner
        if match[6] == team[0]:
            match[6] = team[1]
        #match winner
        if match[13] == team[0]:
            match[13] = team[1]
    for player in players:
        #mom
        if match[14] == player[0]:
            match[14] = player[1]
        #1st Umpire
        if match[15] == player[0]:
            match[15] = player[1]
        #2nd Umpire
        if match[16] == player[0]:
            match[16] = player[1]
    match_mod.append(match)
writeCSV("matches_modified.csv", match_mod)

# For Ball By Ball
col = ['match', 'innings', 'over', 'ball', 'team_batting', 'team_bowling', 'striker', 'striker_position', 'non_striker', 'bowler', 'batsman_scored', 'extra_type', 'extra_runs', 'player_dismissed', 'dismissal_type', 'fielder']
ball_by_ball_modified = []
num_match = 1
ball_by_ball_modified.append(col)
for ball in ball_by_ball[1:]:
    ball[0] = num_match
    num_match = num_match + 1
    for team in teams[1:]:
        #batting team name
        if ball[4] == team[0]:
            ball[4] = team[1]
        #bowling team name
        if ball[5] == team[0]:
            ball[5] = team[1]
    for player in players:
        #striker name
        if ball[6] == player[0]:
            ball[6] = player[1]
        #Non-striker name
        if ball[8] == player[0]:
            ball[8] = player[1]
        #Bowler
        if ball[9] == player[0]:
            ball[9] = player[1]
        #Player Dismissed
        if ball[13] == player[0]:
            ball[13] = player[1]
        #Fielder name
        if ball[15] == player[0]:
            ball[15] = player[1]
    ball_by_ball_modified.append(ball)
writeCSV("ball_by_ball__modified.csv", ball_by_ball_modified)

