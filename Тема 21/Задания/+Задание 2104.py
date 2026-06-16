# Решение

def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 2, e, m - 1), game(s - 7, e, m - 1), game(s // 3, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print([s for s in range(20007, 100000) if not game(s, 20007, 2) and game(s, 20007, 4)])







answer = 60028

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(21, 2104, answer, '145ce83e87fd14eed2cea18ecfaf9758'))