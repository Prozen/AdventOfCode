import sys
for line in sys.stdin:
    print(sum([1 if x == '(' else -1 if x== ')' else 0 for x in line]))
