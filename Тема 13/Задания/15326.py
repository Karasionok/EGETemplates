from ipaddress import ip_network

net = ip_network('105.224.200.224/255.255.255.224', False)
count = 0
for ip in net:
    if f'{ip:b}'.count('1') % 4 ==0:
        count += 1
print(count)