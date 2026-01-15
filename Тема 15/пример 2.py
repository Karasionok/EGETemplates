def del_f(n, m):
    if n % m == 0:
        return True
    return False


min_len = 100
for a in range(100):
    if all((del_f(144, x) <= (not del_f(x, y))) or ((x + y) > 100) or (a - x > y)
           for x in range(1, 100) for y in range(1, 100)):
        min_len = min(min_len, a)
print(min_len)