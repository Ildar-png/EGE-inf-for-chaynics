'''s = 64**13 + 32**6 - 16**2
print(bin(s)[2:].count('1'))'''

'''s = 4096**3125 - 512**625 + 64**125 - 8**25
print(oct(s)[2:].count('7'))'''

'''s = 1024**789 + 256**678 - 64**567
a = []
while s > 0:
    a.append(s % 5)
    s = s // 5
print(a.count(4))'''

'''s = 1296**625 * 216**125 + 36**25 - 6**5
a = []
while s > 0:
    a.append(s % 6)
    s = s // 6
print(a.count(5))'''

'''for x in range(7,36):
    if int('165',x) + int('18',9) == int('416', 7):
        print(x)'''

for x in '0123456789abcdefgh':
    if (int(f'ab5{x}3', 18) + int(f'ef{x}13',18)) % 17 == 0:
        print((int(f'ab5{x}3', 18) + int(f'ef{x}13',18)) // 17)