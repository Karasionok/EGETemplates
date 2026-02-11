# Решение

f = [int(a) for a in open('Задание 1702.txt')]
count = 0
lst = []
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if (f[i] - f[j]) % 60 == 0 and (f[i] % 15 == 0 or f[j] % 15 == 0):
            count += 1
            lst.append(f[i] - f[j])
print(count, max(lst))




answer1 = 63517
answer2 = 9960

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))