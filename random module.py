import random
class human:
    def __init__(self, name):
        self.name = name


class footbalist(human):
    def __init__(self, name):
        self.name = name
    def str(self):
        return f"Name: {self.name}"
     
players = []    
num_player = int(input("Enter even number: "))        
for x in range(num_player):
    player = input("Enter player name: ")
    for y in (player):
        players.append(y)

random.shuffle(players)

team_a = []
team_b = []

for i in range(len(players)):
    if i < len(players) // 2:
        team_a.append(footbalist(players[i]))
    else:
        team_b.append(footbalist(players[i]))


for players in team_a:
    print(players.name +"-"+ "A" )


for players in team_b:
    print(players.name +"-"+ "B")