# Решение


# for a in range(1000):
#     f = True
#     for x in range(1000):
#         for y in range(1000):
#             if ((y > a) or (152 != (2 * y + 3 * x)) or (a < x)) == 0:
#                 f = False
#
#     if f:
#         print(a)
#



answer = 30

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1504, answer, '34173cb38f07f89ddbebc2ac9128303f'))