n, road = int(input()), input()
hasR, hasL = 'R' in road, 'L' in road
if hasR and hasL:
    s, t = road.find('R') + 1, road.find('L')
elif hasR:
    s, t = road.find('R') + 1, road.rfind('R') + 2
else:
    s, t = road.rfind('L') + 1, road.find('L')
print(s, t)