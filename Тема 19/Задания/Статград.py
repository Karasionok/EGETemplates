def game(s, m, to):
    if m == to:
        return 0
    if s >= 414:
        return m % 2 == to % 2
    h = [game(s + 2, m + 1, to), game(s + 3, m + 1, to), game(s * 3, m + 1, to)]
    return any(h)


print('19) ', [s for s in range(1, 414) if not game(s, 0, 1) and game(s, 0, 2)])
print('20) ', [s for s in range(1, 414) if not game(s, 0, 1) and game(s, 0, 3)])
print('21) ', [s for s in range(1, 414) if not game(s, 0, 2) and game(s, 0, 4)])
