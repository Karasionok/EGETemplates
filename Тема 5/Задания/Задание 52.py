# Решение

for n in range(100000000, 100000000000):
    n = 39
    n2 = bin(n)[2:]
    count0 = 0
    for i in range(0, len(n2), 2):
        if n2[i] == '0':
            count0 += 1
    count1 = 0
    for j in range(1, len(n2), 2):
        if n2[j] == '1':
            count1 += 1
    total = abs(count0 - count1)
    if total == 5:
        print(n)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))