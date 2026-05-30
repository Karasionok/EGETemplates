from itertools import product, repeat

# Решение
# alf = sorted('РОСМАХ')
# for a in alf:
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 for e in alf:
#                     for f in alf:
#                         for g in alf:
#                             for h in alf:
#                                 word = a + b + c + d + e + f + g + h
#                                 if word.count('О') == 2 and word.count('О') == 2 and word.count('О') == 2 and\
#                                         word.count('О') == 2 and word.count('О') == 2 and word.count('О') == 2


lst_g = 'ОА'
lst_s = 'РСМХ'
lst_1 = list(product(lst_g, lst_s, lst_g, lst_s, lst_g, lst_s, lst_g, lst_s))
lst_2 = list(product(lst_s, lst_g, lst_s, lst_g, lst_s, lst_g, lst_s, lst_g))
lst = lst_1 + lst_2
count = 0
for i in lst:
    if i.count('Р') == 1 and i.count('О') == 2 and i.count('С') == 1 and i.count('М') == 1 and i.count('Х') == 1 and\
        i.count('А') == 2:
            count += 1
print(count)

answer = 288

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))