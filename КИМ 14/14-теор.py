'''s = 16**16 + 8**8 + 32**4
print(bin(s)[2:].count('1'))'''

'''s = 4096**8 + 512**64 - 64**512
print(oct(s)[2:].count('7'))'''

'''s = 1234**1234+123**123-12**12
print(bin(s)[2:].count('1'))'''

'''s = 1111**111 + 111**11 - 11
print(bin(s)[2:].count('0'))'''

'''s = 234**123 + 32**12 - 32
a = []
while s > 0:
    a.append(s%4)
    s = s//4
print(a.count(3))'''

'''s = 125**27 * 625**81 + 25**9 - 5
a = []
while s > 0:
    a.append(s % 5)
    s = s // 5
print(a.count(4))'''

'''for x in range(3,37):
    if int('222', x) + int('17', 8) == int('238',9):
        print(x)
        break'''

for x in '0123456789ABCDEFGHI':
    if (int(f'11A{x}3', 19) + int(f'12{x}345', 19))%14==0:
        print(x,(int('11A'+ x + '3', 19) + int('12' + x + '345', 19))//14)

'''name = input()
print(f'Привет, {name}, как дела?')'''