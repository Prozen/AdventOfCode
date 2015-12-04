import sys
total = 0
move ={'v':(0,-1), '^':(0,1), '<':(1,0), '>':(-1,0) }
for line in sys.stdin:
    visited = set()
    start0 = (0,0)
    start1 = (0,0)
    visited.add(start0)
    for i in line.strip():
        v,h = move[i]
        v1,h1 = start0
        start0 =(v+v1,h+h1)
        visited.add(start0)
        start0, start1 = start1, start0
    print(len(visited))
