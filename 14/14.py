import re
import itertools
from collections import Counter
data ="""Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.""".split("\n")
reindeers =  [(x[0], int(x[1]), int(x[2]), int(x[3])) for x in [re.split(r" can fly | km/s for | seconds, but then must rest for | seconds\.", x) for x in data]]
def reindistance(time, deer):
    return (time//(deer[3]+ deer[2])*deer[2] +min(time%(deer[3]+ deer[2]), deer[2]))*deer[1]
print(max([reindistance(2503,x) for x in reindeers]))

print(Counter(itertools.chain(*[[x[1] for x in sorted([(reindistance(time,x),x[0]) for x in reindeers]) if x[0]== sorted([(reindistance(time,x),x[0]) for x in reindeers])[-1][0]] for time in range(1,2504)])))
