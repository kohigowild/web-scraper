player = {
    'name' : 'kohi',
    'age': 10,
    'fav_food': ['🍣', '🥐']
}

print(player.get('age'))
# result: 10

player.pop('age')
print(player)
# result: {'name': 'kohi', 'fav_food': ['🍣', '🥐']}

player['xp'] = 1500
print(player)
# result: {'name': 'kohi', 'fav_food': ['🍣', '🥐'], 'xp': 1500}

player['fav_food'].append("🌮")
print(player)
# result: {'name': 'kohi', 'fav_food': ['🍣', '🥐', '🌮'], 'xp': 1500}