# Решение

# count = 0
# for n in range(10000000, 50000000):
#     n2 = bin(n)[2:]
#     ost1 = bin(n % 3)[2:]
#     if len(ost1) == 2:
#         n2 += ost1
#     else:
#         n2 += '0' + ost1
#     ost2 = bin(n % 5)[2:]
#     if len(ost2) == 3:
#         n2 += ost2
#     elif len(ost2) == 2:
#         n2 += '0' + ost2
#     else:
#         n2 += '00' + ost2
#     total = int(n2, 2)
#     if total in range(1111111110, 1444444416):
#         count += 1
# print(count)


answer = 10416665

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))