# Решение

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) or (z <= w)) and ((z == y) <= (w == x))) == 0:
                    print(x, y, z, w)


answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 21, answer, '1ed5bb3720986c091b8dc2704366e53d'))