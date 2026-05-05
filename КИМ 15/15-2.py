def dell(n,m):
    return n % m == 0
z = []
for a in range(1,100000):
    for x in range(1,1000):
        if (dell(x,21) <= ((not dell(x,a)) <= (not dell(x,77)))) == False:
            break
    else:
        z.append(a)
print(max(z))