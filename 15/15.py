from operator import mul
from functools import reduce
import re
data ="""Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8""".split("\n")

ingredients = [(int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])) for x in [ re.split(": capacity |, durability |, flavor |, texture |, calories ", x) for x in data]]
#print(ingredients)

shares = [(x,y,z, 100 -x-y-z)  for x in range(1,98)  for y in range(1,98 -x) for z in range(1,98-x-y)]

print(max([reduce(mul,[max(0,sum(y)) for y in x]) for x in[zip(*[(cap*s,d*s,f*s,t*s)for ((cap,d,f,t, cal), s) in recipe]) for recipe in [zip(ingredients, x) for x in shares]]]))
print(max([reduce(mul,x[:4]) for x in[[max(0,sum(y)) for y in x] for x in[zip(*[(cap*s,d*s,f*s,t*s, cal*s)for ((cap,d,f,t, cal), s) in recipe]) for recipe in [zip(ingredients, x) for x in shares]]] if x[4]== 500]))
