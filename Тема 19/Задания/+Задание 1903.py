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
        h = [game(s - 5, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)


print('19)', [s for s in range(20, 1000) if game(s, 19, 2)])





answer = 25

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1903, answer, '8e296a067a37563370ded05f5a3bf3ec'))