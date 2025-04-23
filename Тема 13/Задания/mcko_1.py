from ipaddress import ip_network

net = ip_network('192.168.108.157/255.255.255.192', False)
print(net.network_address)
print(157 - 128)