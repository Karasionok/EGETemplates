# Решение

maxx = 0
for a in range(1000):
    if all((y > a) or (152 != (2 * y + 3 * x)) or (a < x) for x in range(1000) for y in range(1000)):
        maxx = max(maxx, a)
print(maxx)




answer = 30

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 154, answer, '34173cb38f07f89ddbebc2ac9128303f'))