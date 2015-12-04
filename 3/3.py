import sys
total = 0
move ={'v':(0,-1), '^':(0,1), '<':(1,0), '>':(-1,0) }
for line in sys.stdin:
    visited = set()
    start = (0,0)
    visited.add(start)
    for i in line.strip():
        v,h = move[i]
        v1,h1 = start
        start =(v+v1,h+h1)
        visited.add(start)
    print(len(visited))
