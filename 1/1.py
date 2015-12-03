import sys
for line in sys.stdin:
    print(sum([{'(':1,')':-1}.get(x,0) for x in line]))
