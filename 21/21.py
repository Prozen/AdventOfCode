import itertools
hp = 'hp'
armor= 'armor'
damage = 'damage'
input = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".splitlines()
def getData(s):
    return [tuple([int(y) for y in x.split()[-3:]])for x in s ]
def addTriple(x,y):
    return x[0] + y[0], x[1]+ y[1], x[2]+y[2]
def play(pl1, pl2):
    pl2[hp] = pl2[hp] - max(1, pl1[damage] -pl2[armor])
    if pl2[hp] < 1: return 1
    pl1[hp] = pl1[hp] - max(1, pl2[damage] -pl1[armor])
    if pl1[hp] < 1: return 2
    return play(pl1, pl2)
weap = getData(input[1:6])
arm = getData(input[8:13]) +[(0,0,0)]
ring = getData(input[15:]) +[(0,0,0) , (0,0,0)]
ringPairs = map(lambda x: addTriple(x[0], x[1]), itertools.combinations(ring,2))
weaponArmor =  map(lambda x: addTriple(x[0], x[1]),itertools.product(weap, arm))
equipMents = map(lambda x: addTriple(x[0], x[1]),itertools.product(weaponArmor,ringPairs))
#print(min(filter(lambda x:play({hp:100, armor:x[2], damage:x[1]},{hp:100, armor:2, damage:8}) ==1, equipMents)))
print(max(filter(lambda x:play({hp:100, armor:x[2], damage:x[1]},{hp:100, armor:2, damage:8}) ==2, equipMents)))
