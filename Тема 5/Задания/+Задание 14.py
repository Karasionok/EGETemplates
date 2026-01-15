# Решение

lst = [0] * 10000000
array = []
for n in range(1, 100000):
    n2 = bin(n)[2:]
    n2 += bin(n % 4)[2:]
    r = int(n2, 2)
    lst[r] = 1
for i in range(1, 100000 - 49):
    array.append(lst[i:i+49].count(1))
print(max(array))





answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))