import re
import sys
known="""children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')
info =[s.split(": ") for s in known]
suedata = {}
for line in sys.stdin:
    l = re.split(": |, ", line.strip())
    keys = l[1::2]
    values = l[2::2]
    suedata[l[0]]= dict(zip(keys, [int(i) for i in values]))
for i in info:
    for sue in list(suedata.keys()):
        if(i[0] in ['cats', 'trees']):
            if i[0] in suedata[sue] and suedata[sue][i[0]] <= int(i[1]):
                del suedata[sue]
        elif(i[0] in ['pomeranians', 'goldfish']):
            if i[0] in suedata[sue] and suedata[sue][i[0]] >= int(i[1]):
                del suedata[sue]
        else:
            if i[0] in suedata[sue] and suedata[sue][i[0]] != int(i[1]):
                del suedata[sue]
print(suedata)
