# Решение
from matplotlib.pyplot import ylabel

lst = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        s1 = int('8' + x + '78' + y, 13)
        s2 = int('79' + x + y + '7', 18)
        total = s1 + s2
        if total % 9 == 0:
            lst.append((total, x, y))
print(lst[0][0] / 9)
# print((int(lst[0][1], 13) + int(lst[0][2], 13)) / 2 / 9)



answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))