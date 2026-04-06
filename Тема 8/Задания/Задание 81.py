# Решение
alf = sorted('РОСМАХ')
for a in alf:
    for b in alf:
        for c in alf:
            for d in alf:
                for e in alf:
                    for f in alf:
                        for g in alf:
                            for h in alf:
                                word = a + b + c + d + e + f + g + h
                                if word.count('О') == 2 and word.count('О') == 2 and word.count('О') == 2 and\
                                        word.count('О') == 2 and word.count('О') == 2 and word.count('О') == 2

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))