# Решение
from re import *


f = open('Задание 2401.txt').readline()
parts = sub(r'[*ABC]+', ' ', f).split()
lst = []
for i in parts:
    if len(i) != 1 and i[0] == 'D' and i[1] in '0123456789':
        if i[-1] in 'D+-':
            i = i[:-1]
        lst.append(i)
print(lst)



answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2401, answer, '0e65972dce68dad4d52d063967f0a705'))