# Решение

for n in range(1, 100000):
    n2 = bin(n)[2:]
    lst = list(n2)
    for i in range(len(n2)):
        if lst[i] == '1':
            lst[i] = '0'
        elif lst[i] == '0':
            lst[i] = '1'
    ind = 0
    for j in range(len(lst)):
        if lst[j] == '1':
            ind = j
            break
    lst = lst[ind:]
    total = n - int(''.join(lst), 2)
    if total == 999:
        print(n)
        break




answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))