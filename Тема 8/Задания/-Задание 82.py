# Решение
from itertools import product

lst = list(product(sorted('СТРОКА'), repeat=5))
for i in range(len(lst) - 1, -1, -1):
    if i % 2 == 0 and lst[i][0] not in 'АСТ' and lst[i].count('О') == 0:
        print(i, lst[i])





answer = 5182

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))