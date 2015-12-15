import re
import itertools

data ="""Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46""".split('\n')
distances = dict(itertools.chain(*[[((x[0], x[1]), int(x[2])), ((x[1],x[0]), int(x[2]))] for x in [re.split(" to | = ", x) for x in data]]))

places = {x[0] for x in distances.keys()}
print(min(map(lambda x: sum([distances[y] for y in (zip(x, x[1:]))]),itertools.permutations(places))))
print(max(map(lambda x: sum([distances[y] for y in (zip(x, x[1:]))]),itertools.permutations(places))))
