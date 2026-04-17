# Решение

def f(b, e):
    if b == e:
        return 1
    if b < e or b == 12 and b == 15:
        return 0
    if b % 2 == 0 and b % 3 == 0:
        return f(b - 1, e) + f(b // 2, e) + f(b // 3, e)
    elif b % 2 == 0:
        return f(b - 1, e) + f(b // 2, e)
    elif b % 3 == 0:
        return f(b - 1, e) + f(b // 3, e)
    else:
        return f(b - 1, e)


print(f(19, 1))





answer = 96

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2303, answer, '17e62166fc8586dfa4d1bc0e1742c08b'))