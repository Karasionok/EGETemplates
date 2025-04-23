from ipaddress import ip_network, ip_address

for mask in range(33):
    net = ip_network(f'130.140.241.137/{mask}', False)
    if net.network_address == ip_address('130.140.240.0'):
        print(mask)