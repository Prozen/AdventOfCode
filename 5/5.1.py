import re
import sys
def isnice(s):
    return re.search(r"(..).*\1", s) and  re.search(r"(.).\1",s)
count = 0
for line in sys.stdin:
    if isnice(line.strip()):
        count +=1
print count
