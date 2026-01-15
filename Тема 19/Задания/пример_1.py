def game(s, m, to):
    if s <= 15:
        return m % 2 == to % 2
    if m == to:
        return 0
    h = []
    for i in range(2, 10):
        if s % i == 0:
            move = game(s - i, m + 1, to)
            h.append(move)
    if len(h) == 0:
        for i in range(2, 10):
            if (s - 1) % i == 0:
                move = game(s - 1 - i, m + 1, to)
                h.append(move)
    return any(h) if (m + 1) % 2 == to % 2 else all(h)


print('19) ', [s for s in range(16, 1000) if not game(s, 0, 1) and game(s, 0, 2)])
print('20) ', [s for s in range(16, 1000) if not game(s, 0, 1) and game(s, 0, 3)])
print('21) ', [s for s in range(16, 1000) if not game(s, 0, 2) and game(s, 0, 4)])