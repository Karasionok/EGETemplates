# Решение

f = [int(a) for a in open('Задание 1704.txt')]
lst_m = []
total = []
count = 0
for i in f:
    if i % 5 == 0 and len(str(i)) == 3:
        lst_m.append(i)
minn = min(lst_m)
print(minn)

for i in range(len(f) - 1):
    if (len(str(f[i])) == 3 and len(str(f[i + 1])) != 3) or (len(str(f[i])) != 3 and len(str(f[i + 1])) == 3):
        if (f[i] + f[i + 1]) % minn == 0:
            count += 1
            total.append(f[i] + f[i + 1])

print(count, min(total))


answer1 = 2
answer2 = 33120

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1704, f'{answer1} {answer2}', 'f3c45887478efcf9fcf722ab4708387d'))