# Решение
import sys

sys.setrecursionlimit(10 ** 6)
# lst = [0] * 10 ** 6
# for n in range(10 ** 6):
#     if n <= 10:
#         lst[n] = n
#     elif n > 10:
#         lst[n] = n - 7 + lst[n - 21]
# print((lst[185734] - lst[185650]) / lst[40])



def f(n):
    if n <= 10:
        return n
    if n > 10:
        return (n - 7 + f(n - 21))


print((f(185734) - f(185650)) / f(40))





answer = 17274

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1605, answer, 'ff413935bfae4f0e2d8dce0e0dacfdcd'))