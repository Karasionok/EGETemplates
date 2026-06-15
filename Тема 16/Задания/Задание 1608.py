# Решение
import sys

sys.setrecursionlimit(10 ** 6)


def f(n):
    return g(n - 1) + g(n - 3)


def g(n):
    if n <= 9:
        return 3 * n
    return g(n - 4) + 2


print(f(42999))


answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1608, answer, '0a44140fcbbf55d76a1dc8953ebecd1b'))