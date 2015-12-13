import sys
state = {}
def intOrLookup(n):
    try:
        state[n] = state[n]()
        return state[n]()
    except TypeError:
        return state[n]
    except KeyError:
        return int(n)

def ass(fr):
    return lambda : intOrLookup(fr)
def nott(fr):
    return lambda : (~intOrLookup(fr)+ 65536)
def andd(fr, fr1):
    return lambda : (intOrLookup(fr) & intOrLookup(fr1))
def orr(fr, fr1):
    return lambda : (intOrLookup(fr) | intOrLookup(fr1))
def lshift(fr, fr1):
    return lambda : (intOrLookup(fr) << int(fr1))
def rshift(fr, fr1):
    return lambda : (intOrLookup(fr) >> int(fr1))
for line in sys.stdin:
    a = line.split()
    if a[1] == '->': #assign
        state[a[2]] = ass(a[0])
    elif a[2] == '->': # not
        state[a[3]] = nott(a[1])
    elif a[1] == 'AND':
        state[a[4]] = andd(a[0], a[2])
    elif a[1] == 'OR':
        state[a[4]] = orr(a[0], a[2])
    elif a[1] == 'LSHIFT':
        state[a[4]] = lshift(a[0], a[2])
    elif a[1] == 'RSHIFT':
        state[a[4]] = rshift(a[0], a[2])
#print(state)
print(state['a']())
