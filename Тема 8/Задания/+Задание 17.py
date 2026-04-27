# Решение


# from itertools import product
#
# alf = '12345678'
# total = 0
# alf1= '2468'
# alf2 = '1357'
# lst = list(product(alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1))
# for number in lst:
#     f = True
#     for cifra in number:
#         if number.count(cifra) > 4:
#             f = False
#     if f:
#         total += 1
# lst = list(product(alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2, alf1, alf2))
# for number in lst:
#     f = True
#     for cifra in number:
#         if number.count(cifra) > 4:
#             f = False
#     if f:
#         total += 1
# print(total)

answer = 8200800

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))