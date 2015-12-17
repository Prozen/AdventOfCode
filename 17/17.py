import itertools
import collections
data="""43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38""".split("\n")
print(len([x for x in (itertools.chain.from_iterable( itertools.combinations((int(x) for x in data),n) for n in range(len(data)+1) )) if sum(x)==150]))
print(collections.Counter((len(x) for x in (x for x in (itertools.chain.from_iterable( itertools.combinations((int(x) for x in data),n) for n in range(len(data)+1) )) if sum(x)==150))))
