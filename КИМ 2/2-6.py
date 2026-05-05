print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = ((x <= w) == (z <= y))
                F2 = ((x <= w) and ((not y) == z))
                if F1 == 0 and F2 == 1:
                    print(x,y,z,w,int(F1),int(F2))