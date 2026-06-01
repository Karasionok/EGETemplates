# Решение


for n in range(1000):
    n3 = ''
    x = n
    while n > 0:
        n3 += str(n % 3)
        n //= 3
    n3 = n3[::-1]
    if x % 3 == 0:
        n3 = '1' + n3 + '02'
    elif x % 3 != 0:
        y = (x % 3) * 4
        y3 = ''
        while y > 0:
            y3 += str(y % 3)
            y //= 3
        y3 = y3[::-1]
        n3 += y3
    r = int(n3, 3)
    if r <= 250:
        print(x, r)

answer = 26

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))