'''from fnmatch import*
for x in range(0,10**8,31):
    if fnmatch(str(x),'123*578'):
        print(x,x//31)'''

'''from fnmatch import*
for x in range(0,10**10,5943):
    if fnmatch(str(x),'73*?859?'):
        print(x,x//5943)
'''
'''for x in range(200123,200150+1):
    deliteli = []
    for d in range(1, x+1):
        if x % d == 0:
            deliteli.append(d)
    if len(deliteli) == 4:
        print(x,deliteli)'''

'''for x in range(23456,78954+1):
    deli = []
    if ((x**0.5) % 1) == 0:
        for d in range(2,x):
            if x % d == 0:
                deli.append(d)
        if len(deli) == 3:
            print(x,max(deli))'''

'''for x in range(800001,800001 + 100):
    deli = []
    for d in range(17,x,10):
        if x % d == 0:
            print(x,d)
            break'''

'''def isprime(x):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            return False
    return True

for x in range(7800001,7800001+1000000):
    deliprime = []
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d):
                deliprime.append(d)
            if isprime(x//d):
                deliprime.append(x//d)
    if len(deliprime) != 0:
        M = max(deliprime)+min(deliprime)
        if M > 100000 and str(M) == str(M)[::-1]:
            print(x,M)'''

'''def isprime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return str(x).count('4') == 1

for x in range(5555221,5555221+1000):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d) and isprime(x//d):
                print(x, x // d)
                break
'''

'''def isprime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return str(x).count('3') or str(x).count('6')

for x in range(3646001,3646001+1000):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d) and isprime(x//d):
                print(x, x // d)
                break'''

'''a = []
for y in range(1,10000,2):
    for z in range(1,13):
        x = 105 * y + 3**z
        if len(str(x)) == 6 and str(x).count('3') == 0:
            a.append([x,z])
a.sort()
print(a[:5])'''

'''a = []
for y in range(1,10000,2):
    for z in range(1,13):
        x = 125 * y + 3**z
        if len(str(x)) == 6 and str(x).count('3') == 0:
            a.append([x,z])
a.sort()
print(a[:5])'''

'''def isprime(n):
    for d in range(2,int(n**0.5)+1):
        if x % d == 0:
            return 0
    return 1
from fnmatch import*
for x in range(311,10**8,311):
    if fnmatch(str(x),'17?4*3??') and isprime(x // 311):
        print(x,x//311)'''

def isprime(n):
    for d in range(2,int(n**0.5)+1):
        if x % d == 0:
            return 0
    return 1
from fnmatch import*
for x in range(1597,10**8,1597):
    if fnmatch(str(x),'132?5*5??') and isprime(x // 1597):
        print(x,x//1597)