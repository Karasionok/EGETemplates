# Решение

alf = sorted('ГЕПАРД')
count = 0
for a in alf:
    for b in alf:
        for c in alf:
            for d in alf:
                for e in alf:
                    word = a + b + c + d + e
                    if word.count('Г') == 1 and word[0] != 'А' and word[-1] != "Е":
                        count += 1
print(count)

answer = 2200

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 8, answer, '5249ee8e0cff02ad6b4cc0ee0e50b7d1'))