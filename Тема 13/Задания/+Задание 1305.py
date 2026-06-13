# Решение


from ipaddress import ip_network


net = ip_network('191.128.66.83/255.192.0.0', False)


print(191 + 191 + 255 + 254)


answer = 191191255254

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1305, answer, 'e02030d89e606e5f68c55c7aed0a8e23'))