import sys
from operator import mul
from functools import reduce
total = 0
for line in sys.stdin:
    l = list(map(int,line.split("x")))
    sides = sorted(l)

    total += reduce(mul, l,1) + 2*sum(sides[:-1])
print(total)
