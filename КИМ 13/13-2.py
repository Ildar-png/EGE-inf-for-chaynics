from ipaddress import *
c = 0
net = ip_network('172.16.96.0/255.255.224.0',0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 == 0:
        c += 1
print(c)