'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (not w) and (y or (not z))
                if F == 1:
                    print(x,y,z,w,int(F))'''

'''print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x or y) <= (y == z)
            if F == 0:
                print(x,y,z,int(F))'''

print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (y or x) <= (z == y)
            if F == 0:
                print(x,y,z,int(F))