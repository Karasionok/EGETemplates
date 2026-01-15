p = range(17, 54)
q = range(37, 83)
min_len = 1000
for begin in range(100):
    for end in range(100):
        a = range(begin, end)
        if all((x in p) <= (((x in q) and (not(x in a))) <= (not(x in p))) for x in range(100)):
            min_len = min(min_len, end - begin)
print(min_len)