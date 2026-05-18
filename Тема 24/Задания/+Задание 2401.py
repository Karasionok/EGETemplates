# Решение
line = open('-Задание 2401.txt').read()


right = 0
left = 0
max_len = 0
max_sq = ''
lst = []


while right < len(line):
    count_d = 0
    c = line[right]
    if c not in 'D123456789-+':
        left = right + 1
    elif right > left and c in '-+' and line[right - 1] in '-+':
        left = right + 1
    else:
        current_len = right - left + 1
        if line[left:right + 1].count('D') == 1 and len(line[left:right + 1]) > 1 and line[left:right + 1][0] == 'D' and\
            line[left:right + 1][-1] not in '-+' and line[left:right + 1][1] not in '-+':
            max_sq = line[left:right + 1]
            lst.append(eval(max_sq[1:]))
    right += 1

print(max(lst))

answer = 198

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2401, answer, '0e65972dce68dad4d52d063967f0a705'))