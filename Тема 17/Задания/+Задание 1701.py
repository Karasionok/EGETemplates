# Решение

lst = []
count = 0
total = []
f = [int(a) for a in open('-Задание 1701.txt')]
for n in f:
    if n < 0 and len(str(n)) == 5 and n % 9 == 0:
        lst.append(n)
max_n = max(lst)
print(max_n)
for i in range(len(f) - 1):
    if ((f[i] < 0 and f[i + 1] >= 0) or (f[i + 1] < 0 and f[i] >= 0)) and (f[i] + f[i + 1]) > max_n:
        count += 1
        total.append(f[i] ** 2 + f[i + 1] ** 2)
print(count, min(total))




answer1 = 2627
answer2 = 504410

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1701, f'{answer1} {answer2}', 'b73de31c02e01cfc4508d15f2cf61e69'))