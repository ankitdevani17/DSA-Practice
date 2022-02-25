import itertools
combs = []
STR='ABC'
for l in range(1, len(STR)+1):
    combs.append(list(itertools.combinations(STR, l)))

    for c in combs:
        for t in c:
            print (''.join(t), end =' ')