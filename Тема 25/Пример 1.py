from fnmatch import fnmatch

for n in range(0, 10 ** 10, 2026):
    n = str(n)
    if fnmatch(n, '7?23?64*8') and int(n[1]) % 2 == 0 and int(n[4]) % 2 == 0:
        print(n)


