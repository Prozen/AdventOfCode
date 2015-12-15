import sys
import re
count =0
for line in sys.stdin:
    count  += 2-len(line) + len(line.replace('\\', "\\\\").replace('\"',"\\\""))
print(count)
