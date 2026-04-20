# Решение


count = 0
lst = [0] * 10 ** 9
for n in range(10 ** 9):
    if n == 0:
        lst[0] = 0
    elif n % 2 != 0:
        lst[n] = lst[n - 1] + 1
    elif n > 0 and n % 2 == 0:
        lst[n] = lst[n // 2]
    if lst[n] == 2:
        count += 1
print(count)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1602, answer, 'ddb30680a691d157187ee1cf9e896d03'))