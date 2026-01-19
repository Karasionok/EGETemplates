from ipaddress import ip_network, ip_address

for mask in range(33):
    net = ip_network(f'117.191.208.37/{mask}', False)
    if net.network_address == ip_address('117.191.192.0'):
        print(net.netmask)