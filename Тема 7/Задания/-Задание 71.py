# Решение

i = 24
I1 = 1920 * 1080 * 24 / 8 / 1024
I1_new = 0.2 * I1
I = I1_new * 600 / 1024
print(38 * 1024 / 600)


answer = 64

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(7, 71, answer, 'fc490ca45c00b1249bbe3554a4fdf6fb'))