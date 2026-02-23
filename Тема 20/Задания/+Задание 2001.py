# Решение


# Решение

def game(s, e, m, to):
    if s >= e:
        return m % 2 == to % 2
    if m == to:
        return 0

    h = [game(s + 2, e, m + 1, to), game(s + 3, e, m + 1, to), game(s * 2, e, m + 1, to)]
    return any(h) if (m + 1) % 2 == to % 2 else all(h)

print('19)', [s for s in range(1, 312 + 1) if not game(s, 313, 0, 1) and game(s, 313, 0, 3)])




answer1 = 78
answer2 = 154

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2001, f'{answer1} {answer2}', '7f19aee529865f43adbed8aeffe7ac33'))