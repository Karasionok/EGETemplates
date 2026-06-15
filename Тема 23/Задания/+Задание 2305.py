# Решение

def f(b, e):
    if b > e or b == 8:
        return 0
    if b == e:
        return 1
    else:
        return f(b + 1, e) + f(b + 2, e) + f(b * 2, e)

print(f(3, 14) * f(14, 18))



answer = 360

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2305, answer, 'e7b24b112a44fdd9ee93bdf998c6ca0e'))