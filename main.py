# kohi = {
#     "name": "kohi",
#     "xp": 1000,
#     "team": "Team X"
# }

# jack = {
#     "name": "jack",
#     "xp": 2000,
#     "team": "Team Z"
# }

# def introduct_player(player):
#     name = player["name"]
#     team = player["team"]
#     print(f"Hello! My name is {name} and I play for {team}")

# introduct_player(kohi)
# # Hello! My name is kohi and I play for Team X

# introduct_player(1)

class Player:
    def __init__(self, name, team):
        self.name = name
        # self.xp = xp
        self.team = team

    def introduce(self):
        print(f"Hello! My name is {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    
    def show_player(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

team_x = Team("Team X")
team_z = Team("Team Z")

team_x.add_player("kohi")
team_z.add_player("jack")

team_x.show_player()