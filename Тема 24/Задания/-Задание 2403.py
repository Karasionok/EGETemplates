# Решение


f = open('-Задание 2403.txt').read()
right = 0
left = 0
flag = False
total = []
count_s = 0
count_g = 0
maxx = 0
ans = 0
for i in range(len(f)):
    if right == len(f):
        break
    elif f[right] in '13579' and not flag:
        left = right
        right += 1
        flag = True
        count_s = 0
        count_g = 0
    elif flag and f[right] == f[left]:
        if count_s == count_g and count_s != 0:
            total.append(f[left:right + 1])
            if len(f[left:right + 1]) > maxx:
                maxx = len(f[left:right + 1])
                ans = left
        right = left + 1
        flag = False
    elif f[right] not in '13579' and not flag:
        right += 1
    elif f[right] not in '0123456789':

        if flag:
            if f[right] in 'AEIOUY':
                count_g += 1
            elif f[right] not in 'AEIOUY0123456789':
                count_s += 1
        right += 1
    elif f[right] in '0123456789' and flag:
        flag = False
        count_s = 0
        count_g = 0
        left = right - 1

print(total)
print(ans)

answer = 4625995

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2403, answer, '8f7d5fe843216dc768f4205b9c3867ed'))