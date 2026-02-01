# Решение

lst = []
for x in '0123456':
    for y in '0123456':
        n1 = int(y + x + '320', 7)
        n2 = int('1' + x + '3' + y + '3', 9)
        total = n1 + n2
        if total % 181 == 0:
            lst.append(total)
print(min(lst) / 181)





answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))