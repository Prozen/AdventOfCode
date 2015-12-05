import re
import sys
def isnice(s):
    return all(map(lambda x: s.find(x) == -1,["ab","cd", "pq","xy"])) and re.search(r"(.)\1", s) and  (2 <len(re.findall(r"[aeiou]", s)))
count = 0
for line in sys.stdin:
    if isnice(line.strip()):
        count +=1
print count
