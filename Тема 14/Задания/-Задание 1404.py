# Решение

lst = []
for x in range(37):
    for y in range(37):
        s = 1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5 + 6 * 37 ** 4 + 4 * 37 ** 3 + \
            3 * 37 ** 2 + y * 37 + 7
        umn = x * y
        if s % 36 == 0:
            lst.append(umn)
print(max(lst))





answer = 600

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1404, answer, '86109d400f0ed29e840b47ed72777c84'))