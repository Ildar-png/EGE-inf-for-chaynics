'''def Del(n,m):
    return n % m == 0

for a in range(1,10000):
    a_otwet = True
    for x in range(1,10000):
        if (Del(x,15) <= (not(Del(x,a)) <= (not(Del(x,3))))) == False:
            a_otwet = False
            break
    if a_otwet:
        print(a)'''

'''def Del(n,m):
    return n % m == 0

for a in range(1,10000):
    a_otwet = True
    for x in range(1,10000):
        if (Del(x,a) <= (Del(x,24) or (not(Del(x,3))))) == False:
            a_otwet = False
            break
    if a_otwet:
        print(a)
        break'''

'''for a in range(1,10000):
    for x in range(1,10000):
        if ((x & 15 != 0) or (x & 34 == 0) or (x & a != 0)) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,1000):
    for x in range(1,10000):
        if (((x & 46 == 0) or (x & 18 == 0)) <= ((x & 115 != 0) <= (x & a == 0))) == False:
            break
    else:
        print(a)'''

'''for a in range(1,10000):
    for x in range(1,10000):
        if ((x & 45 != 0) <= ((x & 23 == 0) <= (x & a != 0))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,10000):
    if all((((y + 10*x != 28) or (a > x - 1)) and (a < y + 50)) for x in range(0,1000) for y in range(0,1000)):
        print(a)
        break'''

'''for a in range(1,10000):
    if all(((15*x - y + 40 != 0) or (a < x) or (a < y)) for x in range(1,1000) for y in range(1,1000)):
        print(a)'''

'''c = 0
for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if (((x > 15) <= (x*y + 10*x >= a)) and ((y*x + y > a) <= (y >= 1))) == False:
                break
        if (((x > 15) <= (x*y + 10*x >= a)) and ((y*x + y > a) <= (y >= 1))) == False: # Можно вместо ввода новой переменной писать еще раз условие выхода из цикла
            break
    else:
        c += 1
print(c)'''

'''q = list(range(17,91))
p = list(range(10,47))
a = []
for x in range(1,100):
    if (((x in p) and (x in q)) <= (x in a)) == False:
        a.append(x)
print(a)
print(47-17)'''

'''q = list(range(12,30))
p = list(range(5,42))
a = []
for x in range(1,100):
    if (((x in a) and (x in p)) or (not(x in q))) == False:
        a.append(x)
print(a)
print(29-12)'''

'''q = list(range(8,17))
p = list(range(12,29))
a = list(range(1,100))
for x in range(1,100):
    if ((x in a) <= ((x in p) and (not(x in q))) )== False:
        a.remove(x)
print(a)
print(28-16)'''

'''q = list(range(12,23))
p = list(range(3,13))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(22-3)'''

'''q = list(range(37,84))
p = list(range(17,55))
a = []
for x in range(1,100):
    if (((x in p) and (x in q)) <= (x in a)) == False:
        a.append(x)
print(a)
print(54-37)'''

'''q = list(range(10,56))
p = list(range(4,20))
a = []
for x in range(1,100):
    if ((x in a) or ((not(x in p)) <= (not x in q))) == False:
        a.append(x)
print(a)
print(55-20)'''

'''q = list(range(33,88))
p = list(range(10,49))
a = list(range(1,100))
for x in range(1,100):
    if (((x in p) <= (not(x in q))) <= (not(x in a))) == False:
        a.remove(x)
print(a)
print(49-33)'''

'''q = list(range(18,33))
p = list(range(5,21))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(32-5)'''

'''for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if ((x + 5*y != 29) or ((a > x) and (a > y))) == False:
                break
        if ((x + 5 * y != 29) or ((a > x) and (a > y))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(0,1000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x + 5*y != 29) or ((a > x) and (a > y))) == False:
                break
        if ((x + 5 * y != 29) or ((a > x) and (a > y))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(0,200000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((178125 != y + 3*x) or (a > x) and (a > y)) == False:
                break
        if ((178125 != y + 3*x) or (a > x) and (a > y)) == False:
            break
    else:
        print(a)
        break'''

for a in range(1,1000000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((4*y < a) and (2*x < a) or (120000 < 6*y + 2*x)) == False:
                break
        if ((4 * y < a) and (2 * x < a) or (120000 < 6 * y + 2 * x)) == False:
            break
    else:
        print(a)
        break