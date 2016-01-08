import heapq
hp = 'hp'
armor= 'armor'
damage = 'damage'
effects = 'effects'
spent = 'spent'
timer = 'timer'
states =  [(0, (50,500,0,[]), 71)]
def applyEffects(pl1, pl2Hp):
    neweffects =[]
    pl1Hp = pl1[0]
    pl1Armor = 0
    pl1Mana = pl1[1]
    inProcess = []
    for effect in pl1[3]:
        if effect[0] == 'Shield':
            pl1Armor = 7
        if effect[0] == 'Poison':
            pl2Hp -=3
        if effect[0] == 'Recharge':
            pl1Mana += 101
        if effect[1] > 1:
            inProcess.extend([effect[0]])
            neweffects += [(effect[0], effect[1] -1)]
    return (inProcess,(pl1Hp, pl1Mana, pl1Armor, neweffects), pl2Hp)
def boss(spent, pl1, pl2Hp):
    inProcess, (pl1Hp, pl1Mana, pl1Armor, neweffects), pl2Hp = applyEffects(pl1, pl2Hp)
    pl1Hp -= max(1, 10 -pl1Armor)
    if pl1Hp > 0 or pl2Hp < 1 :
        heapq.heappush(states,(spent, (pl1Hp, pl1Mana, pl1Armor, neweffects), pl2Hp))

def play(spent, pl1, pl2Hp):
    if pl2Hp < 1:
        return spent, pl1, pl2Hp
    if pl1[0] < 2: return None
    inProcess, (pl1Hp, pl1Mana, pl1Armor, neweffects), pl2Hp = applyEffects(pl1, pl2Hp)
    if pl2Hp < 1:
        heapq.heappush(states,(spent, (pl1Hp, pl1Mana, pl1Armor, neweffects), pl2Hp))
    pl1Hp -=1
    for spell in filter(lambda x : x not in inProcess, ['Shield', 'Poison', 'Recharge', 'Drain', 'Missile']):
        if spell == 'Shield' and pl1Mana >112:
            boss(spent+113,(pl1Hp, pl1Mana - 113, 0, neweffects + [('Shield', 6)]), pl2Hp)
        if spell == 'Poison' and pl1Mana >172:
            boss(spent +173,(pl1Hp, pl1Mana - 173, 0, neweffects + [('Poison', 6)]), pl2Hp)
        if spell == 'Recharge' and pl1Mana >228:
            boss(spent +229,(pl1Hp, pl1Mana-229, 0, neweffects + [('Recharge', 5)]), pl2Hp)
        if spell == 'Drain' and pl1Mana >72:
            boss(spent +73,(pl1Hp+2, pl1Mana -73, 0, neweffects), pl2Hp-2)
        if spell == 'Missile'and pl1Mana >52:
            boss(spent+53,(pl1Hp, pl1Mana-53, 0, neweffects), pl2Hp-4)
result =  None
while not result:
    result  = play(*heapq.heappop(states))
print(result)
