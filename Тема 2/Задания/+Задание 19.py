# Решение

print('x y z w u')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    if (((x <= y) and (z == (not w))) <= (u ==(x or z))) == 0:
                        print(x, y, z, w, u)

        #wzyxu


answer = 'wzyxu'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 19, answer, 'b83215ff76ddd410e32571919b78d0eb'))