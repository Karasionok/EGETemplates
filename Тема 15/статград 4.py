def dell(n, m):
    if n % m == 0:
        return True
    return False

b = range(120, 210)
for a in range(1, 1000):
    f = True
    for x in range(1, 1000):
        if (dell(x, a) or ((x in b) <= ((not dell(x, 36)) or ((x + a) <= 272)))) == 0:
            f = False
    if f:
        print(a)