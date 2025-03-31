from ipaddress import ip_network

host = '93.138.160.0'
ip = '93.138.161.49'
count = 0
for mask in range(33):
    net = ip_network(f"{ip}/{mask}", False)
    if str(net.network_address) == host:
        count += 1
print(count)