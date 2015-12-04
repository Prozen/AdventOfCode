import sys
total = 0
for line in sys.stdin:
    l = list(map(int,line.split("x")))
    sides =  [l[0]*l[1], l[0]*l[2] ,l[1]*l[2]]
    total += min(sides) + 2*sum(sides)
print(total)
