# Решение


I = 60 * 25 * 1024
t = 1.5 * 1024 / 1.5
I1 = 2 * 32000 * 16 * t / 8 / 1024
print(I1 / I)



answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(7, 72, answer, 'f033ab37c30201f73f142449d037028d'))