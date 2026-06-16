# Решение

def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 2, e, m - 1), game(s - 7, e, m - 1), game(s // 3, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print([s for s in range(20007, 1000000) if not game(s, 20007, 1) and game(s, 20007, 3)])




answer1 = 60026
answer2 = 60027

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2004, f'{answer1} {answer2}', '2d18a60f2dac95ca869006f0695ce088'))