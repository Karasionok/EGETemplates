s = range(212, 314)
t = range(287, 411)
min_len = 500
for begin in range(500):
    for end in range(500):
         a = range(begin, end)
         if all((not (x in a)) <= ((x in t) == (x in s)) for x in range(500)):
                min_len = min(min_len, end - begin)
print(min_len)