import sys
import itertools
start = [[False for i in range(0,1000)] for j in range(0, 1000)]

def set_all(start, line, val):
    foo  = line.split()
    fram = foo[2].split(',')
    to =  foo[4].split(',')
    r1 = range(int(fram[0]), int(to[0]) +1)
    r2 = range(int(fram[1]), int(to[1])+1)
    for (i,j) in itertools.product(r1, r2 ):
        start[i][j] = val


def process(start, line):
    if(line.startswith("turn on")):
        set_all(start, line, True)
    if(line.startswith("turn off")):
        set_all(start, line, False)
    if(line.startswith("toggle")):
        foo  = line.split()
        fram = foo[1].split(',')
        to =  foo[3].split(',')
        r1 = range(int(fram[0]), int(to[0]) +1)
        r2 = range(int(fram[1]), int(to[1])+1)
        for (i,j) in itertools.product(r1, r2 ):
            start[i][j] = not start[i][j]



for line in sys.stdin:
    process(start, line)
print(sum(map(sum, start)))
