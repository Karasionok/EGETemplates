# Решение

# alf = '012345678'
# total = 0
# for a in alf:
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 for e in alf:
#                     for f in alf:
#                         for g in alf:
#                             for h in alf:
#                                 for i in alf:
#                                     for j in alf:
#                                         for l in alf:
#                                             number = a + b + c + d + e + f + g + h + i + j + l
#                                             count = 0
#                                             for cifra in range(len(number) - 1):
#                                                 if (int(number[cifra]) % 2 == 0 and int(number[cifra]) % 2 == 1) or\
#                                                     (int(number[cifra]) % 2 == 1 and int(number[cifra]) % 2 == 0) and\
#                                                         number.count(number[cifra]) <= 4:
#                                                     count += 1
#                                             if count == 10 and number.count('0') == 0:
#                                                 total += 1

from itertools import product

# alf = '12345678'
# total = 0
# alf1= '2468'
# alf2 = '1357'
# lst = list(product(alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1))
# for number in lst:
#     for cifra in range(len(number)):
#         if number.count(cifra) <= 4:
#             total += 1
# lst = list(product(alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2))
# for number in lst:
#     for cifra in range(len(number)):
#         if number.count(cifra) <= 4:
#             total += 1
# print(total)

answer = 92274688

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))