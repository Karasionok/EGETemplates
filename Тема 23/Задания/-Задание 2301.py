# Решение

def f(b, e, inc):
    if b > e or b == inc:
        return 0
    if b == e:
        return 1

    return f(b + 1, e, inc) + f(b * 2, e, inc) + f(b * 3, e, inc)


print(f(9, 24, 0) * f(24, 27, 0) * f(27, 81, 0))





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2301,  answer, 'a8baa56554f96369ab93e4f3bb068c22'))