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
    def __init__(self, name, xp, team):
        self.name = name
        self.xp = xp
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

    def add_player(self, name, xp=0):
        new_player = Player(name, xp, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        self.players = [player for player in self.players if player.name != name]

    def total_xp(self):
        total_xp = sum(player.xp for player in self.players)
        print(f"Total XP of team {self.team_name}: {total_xp}")

team_x = Team("Team X")
team_z = Team("Team Z")

team_x.add_player("kohi", 1000)
team_x.add_player("sam", 500)
team_z.add_player("jack", 1200)

team_x.show_player()
"""
Hello! My name is kohi and I play for Team X
Hello! My name is sam and I play for Team X
"""
team_x.total_xp()
# Total XP of team Team X: 1500

team_x.remove_player("sam")
team_x.show_player()
# Hello! My name is kohi and I play for Team X