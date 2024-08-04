def create_player(name, xp, team):
    return {
    "name": name,
    "xp": xp,
    "team": team
}

def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

kohi = create_player("kohi", 1000, "Team X")

introduct_player(1)

