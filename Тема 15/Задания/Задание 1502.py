# Решение

p = range(19, 85)
q = range(4, 52)
f = True
for b in range(1000):
    for end in range(1001):
        for x in range(10000):
            a = range(b, end)
            if ((x in q) <= ((not (x in p)) <= (not ((x in q) and (not (x in a)))))) == 0:
                print(x)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1502, answer, '9bf31c7ff062936a96d3c8bd1f8f2ff3'))