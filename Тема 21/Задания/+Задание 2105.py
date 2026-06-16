# Решение

def game(s, e, m):
    if s <= e:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [game(s - 3, e, m - 1), game(s - 7, e, m - 1), game(s // 4, e, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print([s for s in range(16, 1000) if not game(s, 15, 2) and game(s, 15, 4)])









answer = 70

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(21, 2105, answer, '7cbbc409ec990f19c78c75bd1e06f215'))