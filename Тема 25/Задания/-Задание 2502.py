# Решение
#
# def deliteli(n):
#     d = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0 and isprime(i):
#             d.add(i)
#             if isprime(n // i):
#                 d.add(n // i)
#     return sorted(d)
#
#
# def isprime(n):
#     delitel = deliteli(n)
#     if len(delitel) == 0:
#         return True
#     return False
#
#
# for n in range(1324999, -1, -1):
#     deli = deliteli(n)
#     s = sum(deli)
#     if s <= 30000 and s % 5 == 0 and s != 0:
#         print(n, deli)


answer = [1324998, 1324995, 1324994, 1324992, 1324991]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2502, answer, 'a4962eab53c004fe8f3ffaca3207d0fa'))