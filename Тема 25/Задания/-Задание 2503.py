# Решение

# def delitel(n):
#     d = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n // i)
#     return sorted(d)
#
# for j in range(1000000000, 100000000, -1):
#     deliteli = delitel(j)
#     num = j - len(deliteli)
#     if num % 23 == 0:
#         print(j, len(deliteli), num)





answer = [999999961, 999999789, 999999740, 999999731, 999999690]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2503, answer, 'c867bc32545e94925e8d2198ad7333d9'))