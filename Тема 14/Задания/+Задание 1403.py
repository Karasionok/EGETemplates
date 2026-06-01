# Решение

count = 0
s = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
while s > 0:
    if s % 25 == 0:
        count += 1
    s //= 25
print(count)




answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1403, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))