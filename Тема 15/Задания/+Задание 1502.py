# Решение

# p = range(19, 85)
# q = range(4, 52)
# lst = []
# for b in range(1000):
#     for end in range(1001):
#         a = range(b, end)
#         if all(((x in q) <= ((not (x in p)) <= (not ((x in q) and (not (x in a))))))for x in range(1000)):
#             lst.append(len(a))
# print(min(lst))





answer = 15

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1502, answer, '9bf31c7ff062936a96d3c8bd1f8f2ff3'))