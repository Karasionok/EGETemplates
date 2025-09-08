from itertools import permutations

table  = '12 17 18 21 27 34 37 43 45 46 54 56 57 58 64 65 71 72 73 75 78 81 85 87'
graph = 'АБ БА БВ ВБ ВЕ ЕВ ЕК КЕ КИ ИК ИЖ ЖИ ЖГ ГЖ ГА АГ ГИ ИГ АИ ИА БИ ИБ БЕ ЕБ ЕИ ИЕ'

for i in range(1, 9):
    for j in range(1, 9):
        if i != j:
            new_road = str(i) + str(j)
            if new_road not in table:
                new_table = table + f' {new_road} {new_road[::-1]}'

                for p in permutations(sorted('АБВГЕЖИК')):
                    new_graph = new_table
                    for i in range(1, 9):
                        new_graph = new_graph.replace(str(i), p[i - 1])
                    if set(new_graph.split()) == set(graph.split()):
                        print(p)
                        print(new_road)
