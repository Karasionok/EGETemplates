# Решение
import sys



def f(b, e, k):
    if b == e:
        return 1
    if b > e + 1:
        return 0

    if len(k) > 0 and k[-1] == 'A':
        return f(b + 3, e, k + 'B') + f(b * 2, e, k + 'C')
    else:
        return f(b - 1, e, k + 'A') + f(b + 3, e, k + 'B') + f(b * 2, e, k + 'C')

print(f(3, 12, ''))

answer = 53

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2304, answer, 'd82c8d1619ad8176d665453cfb2e55f0'))