print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) and (z <= y) and (not w)) or ((z == w) and (x or y <= w))
                if F == 1:
                    print(x,y,z,w,int(F))