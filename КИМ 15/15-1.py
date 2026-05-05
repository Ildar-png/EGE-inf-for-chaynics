'''def dell(n,m):
    return n % m == 0

for a in range(1,10000):
    for x in range(1,10000):
        if ((dell(x,a) and (not dell(x,36))) <= (not dell(x,12))) == False:
            break
    else:
        print(a)
        break'''

'''def dell(n,m):
    return n % m == 0

for a in range(1,10000):
    for x in range(1,10000):
        if (dell(x,a) <= ((not dell(x,28)) or dell(x,42))) == False:
            break
    else:
        print(a)
        break'''

def dell(n,m):
    return n % m == 0

for a in range(1,10000):
    for x in range(1,10000):
        if (dell(x,a) <= (dell(x,21) or dell(x,35))) == False:
            break
    else:
        print(a)
        break