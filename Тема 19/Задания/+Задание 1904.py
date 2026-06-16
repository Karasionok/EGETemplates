# Решение

def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 2, e, m - 1), game(s - 7, e, m - 1), game(s // 3, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)


print([s for s in range(20007, 1000000) if game(s, 20007, 2)])





answer = 60025

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1904, answer, '543a84894716c6c0ed6cabe60aac9945'))