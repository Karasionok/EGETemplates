# Решение

f = open('Задание 2402.txt').read()
right = 1
left = 0
flag = True
count = 0
total = []
# while flag:
#     if right == len(f):
#         total.append(len(f[left:right - 1]))
#         flag = False
#         break
#     if f[right] == 'E' and f[right - 1] == 'D':
#         count += 1
#         right += 1
#     if count == 240:
#         total.append(len(f[left:right + 1]))
#         right += 2
#         left = right - 1
#         count = 0
#     else:
#         right += 1
# print(len(f))
# print(total)

print(len(f.split('DE')))
print(len(f))






answer = 970249

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2402, answer, '0bb01cf1951560939ce9d92c72dfd974'))