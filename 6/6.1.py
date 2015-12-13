import sys
import itertools
start = [[0 for i in range(0,1000)] for j in range(0, 1000)]

def set_all(start, line, pos, val):
    foo  = line.split()
    fram = foo[pos].split(',')
    to =  foo[pos+2].split(',')
    r1 = range(int(fram[0]), int(to[0]) +1)
    r2 = range(int(fram[1]), int(to[1])+1)
    for (i,j) in itertools.product(r1, r2 ):
        start[i][j] = max(start[i][j] + val, 0)


def process(start, line):
    if(line.startswith("turn on")):
        set_all(start, line,2, 1)
    if(line.startswith("turn off")):
        set_all(start, line,2, -1)
    if(line.startswith("toggle")):
        set_all(start, line,1, 2)


for line in sys.stdin:
    process(start, line)
print(sum(map(sum, start)))
