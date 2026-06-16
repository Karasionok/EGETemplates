# Решение

def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 3, e, m - 1), game(s - 7, e, m - 1), game(s // 4, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print([s for s in range(16, 1000) if game(s, 15, 2)])







answer = 64

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1905, answer, 'ea5d2f1c4608232e07d3aa3d998e5135'))