import itertools

count = 0
glas = 'ОА'
sogl = 'РСМХ'
lst = list(itertools.product(glas, sogl, glas, sogl, glas, sogl, glas, sogl))
for i in lst:
    word = ''.join(i)
    if word.count('Р') == 1 and word.count('С') == 1 and word.count('М') == 1 and word.count('Х') == 1 and\
            word.count('О') == 2 and word.count('А') == 2:
        count += 1
lst = list(itertools.product(sogl, glas, sogl, glas, sogl, glas, sogl, glas))
for j in lst:
    word = ''.join(j)
    if word.count('Р') == 1 and word.count('С') == 1 and word.count('М') == 1 and word.count('Х') == 1 and\
            word.count('О') == 2 and word.count('А') == 2:
        count += 1
print(count)