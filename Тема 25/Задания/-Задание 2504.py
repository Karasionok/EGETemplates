# Решение

def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def deliteli(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d


def p_deliteli(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if isprime(i):
                d.add(i)
            if isprime(n // i) and (n // i) != n:
                d.add(n // i)
    return d


# for n in range(4555706, 10 ** 10):
#     if str(n)[-1] != 3:
#         s = sum(deliteli(n))
#         k = len(p_deliteli(n))
#         if str(n - s - k)[-2:] == '23':
#             print(n)

# Ответ в виде списка чисел []
answer = [4555780, 4555903, 4556079, 4556110, 4556120]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2504, answer, '4f6cb100db828c27d436322ae3bffeef'))