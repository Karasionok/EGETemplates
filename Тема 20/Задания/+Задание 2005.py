# Решение


def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 3, e, m - 1), game(s - 7, e, m - 1), game(s // 4, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print([s for s in range(16, 1000) if not game(s, 15, 1) and game(s, 15, 3)])






answer1 = 67
answer2 = 68

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2005, f'{answer1} {answer2}', 'baea15b2f826d9bc6604da84fd16f9cd'))