# Решение
from itertools import product

lst = list(product(sorted('БЦКФ'), repeat=5))
print(lst[238])





answer = 'БЦФЦФ'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 83, answer, 'f0a551e113a7af86f780ae14e74c3ac7'))