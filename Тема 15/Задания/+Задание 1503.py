# Решение


for a in range(1000):
    f = True
    for x in range(1000):
        for y in range(1000):
            if (((y < 20) <= (x > 70)) or (not ((x < a) <= (y > a)))) == 0:
                f = False

    if f:
        print(a)



answer = 71

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1503, answer, 'e2c420d928d4bf8ce0ff2ec19b371514'))