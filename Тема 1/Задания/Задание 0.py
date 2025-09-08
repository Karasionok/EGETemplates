from itertools import permutations

table  = '16 17 23 24 26 32 34 42 43 45 54 57 61 62 67 71 75 76'
graph = 'АБ БА БВ ВБ ВГ ГВ ГД ДГ ДЕ ЕД ЕК КЕ АК КА ДВ ВД КБ БК'

for p in permutations(sorted('ДЕКАБВГ')):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)