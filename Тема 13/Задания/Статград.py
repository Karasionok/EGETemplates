from ipaddress import ip_address, ip_network

net = ip_network('220.151.212.184/255.255.192.0', False)
for ip in net:
    ip_2 = f'{ip:b}'
    if ip_2.count('1') % 4 == 0:
        print(ip_2)

print(int('11011100', 2))
print(int('10010111', 2))
print(int('11000000', 2))
print(int('00001111', 2))

2201511920