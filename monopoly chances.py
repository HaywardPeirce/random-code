import random

def roll():
    return random.randrange(1,7)

def turn():
    for player in players:
        temp = roll()
        if (players[player] + temp) > 40:
            players[player] = (players[player] + temp) - 40
        else: players[player]+= temp
        landing_counter[players[player]] += 1
        #print player + " " +str(players[player])

def print_count():
    for lot in landing_counter:
        print str(lot) + " " + str(landing_counter[lot])

def roll_percent():
    rolls = rounds * 4.0
    for plot in landing_counter:
        land_per.append(landing_counter[plot]/rolls)
        
rounds = 20
plot = {"Mediterranean Avenue":1, "Community Chest": 2, "Baltic Avenue":3, "Income Tax": 4, "Reading Railroad":5, "Oriental Avenue":6, "Chance": 7, "Vermont Avenue":8, "Connecticut Avenue":9, "Just Visiting": 10,"Saint Charles Place":11, "Electric Company":12, "States Avenue":13, "Virginia Avenue":14, "Pennsylvania Railroad":15, "Saint James Place":16, "Community Chest": 17,"Tennessee Avenue":18, "New York Avenue":19, "Free Parking": 20, "Kentucky Avenue":21, "Chance": 22, "Indiana Avenue":23, "Illinois Avenue":24, "B & O Railroad":25, "Atlantic Avenue":26, "Ventnor Avenue":27, "Water Works":28, "Marvin Gardens":29, "Go To Jail":30, "Pacific Avenue":31, "North Carolina Avenue":32, "Community Chest":33, "Pennsylvania Avenue":34, "Short Line Railroad":35, "Chance":36, "Park Place": 37, "Luxury Tax":38, "Boardwalk":39, "Go": 40}
players = {"player1":1, "player2":1, "player3":1, "player4":1}
landing_counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0,  21:0, 22:0, 23:0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 34:0, 35:0, 36:0, 37:0, 38:0, 39:0, 40:0}
land_per = []

for i in range(1, rounds):
    turn()
    
#print_count()
roll_percent()

print len(land_per)
print len(plot)
for item in plot:
    print item +" "+ str(land_per[plot[item]])
