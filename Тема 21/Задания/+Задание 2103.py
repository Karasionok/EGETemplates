# Решение



def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    if s % 2 == 0 and s % 3 == 0:
        h = [game(s - 5, e, m - 1), game(s // 2, e, m - 1), game(s // 3, e, m - 1)]
    elif s % 2 == 0:
        h = [game(s - 5, e, m - 1), game(s // 2, e, m - 1)]
    elif s % 3 == 0:
        h = [game(s - 5, e, m - 1), game(s // 3, e, m - 1)]
    else:
        h = [game(s - 5, e, m - 1), game(s + 1, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)


print('20)', [s for s in range(20, 1000) if not game(s, 19, 2) and game(s, 19, 4)])




answer = 60

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(21, 2103, answer, '072b030ba126b2f4b2374f342be9ed44'))