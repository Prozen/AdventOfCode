import sys
import re
count =0
for line in sys.stdin:
    count  += len(line) - len(re.sub(r'\\x[0-9a-f][0-9a-f]','a',line.replace('\\\"', "\"").replace('\\\\',"\\")))+2
print(count)
