# Решение

for n in range(1000):
    n2 = bin(n)[2:]
    n2 += bin(n % 4)
    r = int(n2, 2)






answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 54, answer, '473b677ddfbedbb3d2e6d5e5980dc6e1'))