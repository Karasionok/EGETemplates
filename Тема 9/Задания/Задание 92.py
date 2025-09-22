# Решение
f = [x for x in open('92.csv')]
total = 0
for line in f:
    line = line.split(';')
    line[-1] = str(int(line[-1]))
    print(line)
    for i in line:
        k = 0
        summa = 0
        rep = 0
        if line.count(i) == 3:
            k += 1
            rep = int(i)
        if line.count(i) == 2:
            break
        elif line.count(i) == 1:
            summa += int(i)
        if k == 3 and rep > (summa / 3):
            total += 1
print(total)





answer = 24959

#

import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '18b8ea83d814103c4a8f379165ce9a62' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 92, 9, result)