# Решение
count = 0
for f in open('Задание 9.csv'):
    row = [int(a) for a in f.split(';')]
    rep = [b for b in row if row.count(b) > 1]
    maxx = max(row)
    summa = 0
    for i in row:
        if i != maxx:
            summa += i
    if row.count(maxx) == 1 and len(rep) >= 2 and maxx > (summa / 5) * 3:
        count += 1
print(count)




answer = 95

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 9, answer, '812b4ba287f5ee0bc9d43bbf5bbe87fb'))