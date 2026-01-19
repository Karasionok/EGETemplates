# Решение

from ipaddress import ip_network


for m in range(16, 33):
    net1 = ip_network(f'157.220.185.237/{m}', False)
    net2 = ip_network(f'157.220.184.230/{m}', False)
    if net1 == net2:
        count = 0
        for i in net1:
            i2 = f'{i:b}'
            if i2.count('1') == 15:
                count += 1
        print(count)




answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))