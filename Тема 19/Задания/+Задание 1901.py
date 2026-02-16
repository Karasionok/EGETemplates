# Решение

def game(s, e, m, to):
    if s >= e:
        return m % 2 == to % 2
    if m == to:
        return 0

    h = [game(s + 2, e, m + 1, to), game(s + 3, e, m + 1, to), game(s * 2, e, m + 1, to)]
    return any(h) if (m + 1) % 2 == to % 2 else all(h)

print('19)', [s for s in range(1, 312 + 1) if not game(s, 313, 0, 1) and game(s, 313, 0, 2)])



answer = 311

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1901, answer, '9dfcd5e558dfa04aaf37f137a1d9d3e5'))