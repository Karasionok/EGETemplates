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


print('20)', [s for s in range(20, 1000) if not game(s, 19, 1) and game(s, 19, 3)])




answer1 = 40
answer2 = 46

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2003, f'{answer1} {answer2}', '593697ada77fb63ca3472e9b465e09a6'))