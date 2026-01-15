print('x y z w')            #zxyw
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = (x or (not y)) == (z <= w)
                F2 = ((not x) == y) and (z <= w)
                if F2 == 0:
                    print(x, y, z, w)
