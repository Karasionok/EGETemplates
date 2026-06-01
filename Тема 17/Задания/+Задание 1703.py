# Решение
f = [int(a) for a in open('-Задание 1703.txt')]
lst = []
count = 0
total = []
for i in f:
    if str(i)[-2] == str(i)[-1]:
        lst.append(i)
minn = min(lst)
for i in range(len(f) - 1):
    if (str(f[i])[-1] == str(f[i + 1])[-2]) or (str(f[i])[-2] == str(f[i + 1])[-1]):
        if (f[i] % 13 == 0 and f[i + 1] % 13 != 0) or (f[i] % 13 != 0 and f[i + 1] % 13 == 0):
            if (f[i] ** 2 + f[i + 1] ** 2) <= minn ** 2:
                count += 1
                total.append(f[i] ** 2 + f[i + 1] ** 2)
print(count, max(total))



answer1 = 115
answer2 = 96944186

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1703, f'{answer1} {answer2}', '1b1a3f384b8b6bddea7c6e63fad46024'))