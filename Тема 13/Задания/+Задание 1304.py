# Решение

from ipaddress import ip_network

net = ip_network('127.204.113.250/255.255.254.0', False)
for i in net:
    print(i)

print(127+204+112+1)



answer = 444

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1304, answer, '550a141f12de6341fba65b0ad0433500'))