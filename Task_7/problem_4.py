class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Team:
    def __init__(self):
        self.members = []

    def add_player(self, player_object):
        self.members.append(player_object)



p1 = Player("mo", 10)
p2 = Player("maher", 9)

t = Team()
t.add_player(p1)
t.add_player(p2)

for p in t.members:
    print(p.name, p.score)