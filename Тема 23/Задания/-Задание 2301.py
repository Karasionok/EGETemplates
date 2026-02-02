# Решение

def f(b, e, inc):
    if b == e:
        return 1
    if b > e or b == inc:
        return 0
    return f(b + 1, e, inc) + f(b * 2, e, inc) + f(b * 3, e, inc)


print(f(9, 24, 27) * f(24, 81, 27) * f(9, 27, 24) * f(27, 81, 24))





answer = 960

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2301,  answer, 'a8baa56554f96369ab93e4f3bb068c22'))