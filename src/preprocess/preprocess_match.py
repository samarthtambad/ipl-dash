import csv
matchFile = open('../assets/data/Match.csv')
matchReader = csv.reader(matchFile)
matchData = list(matchReader)
# print matchData

bbbFile = open('../assets/data/Ball_by_Ball.csv')
bbbReader = csv.reader(bbbFile)
bbbData = list(bbbReader)
print bbbData

matchDict = {}
matchArr = []
firstMatch = matchData[0]
for match in matchData:
    if match.size:
        matchDict.push()
        


