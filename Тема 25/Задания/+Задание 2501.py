# Решение
from fnmatch import fnmatch

# for i in range(0, 10 ** 10, 2026):
#     i = str(i)
#     m = fnmatch(str(i), '5?34?71*2')
#     if m and int(i[1]) % 2 == 1 and int(i[4]) % 2 == 1:
#         print(i)
#




answer = [553497122, 5134171692, 5134971962, 5734171592, 5734971862]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2501, answer, 'ac788180ab5a2f5b1ff54976b883276a'))