# Решение
line = open('-Задание 2401.txt').read()


right = 0
left = 0
max_len = 0
max_sq = ''


while right < len(line):
    c = line[right]
    if c not in '123456789-+':
        left = right + 1
    elif right > left and c in '-+' and line[right - 1] in '-+':
        left = right + 1
    else:
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            max_sq = line[left:right + 1]
    right += 1

print(max_sq, max_len)
print(-7+6+37+4+4+6-58+7+1-1)

answer = -1

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2401, answer, '0e65972dce68dad4d52d063967f0a705'))