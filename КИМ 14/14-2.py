a = []
for x in range(1,2031):
    s = 6**2030 + 6**100 - x
    c = 0
    while s > 0:
        if s % 6 == 0:
            c+=1
        s//=6
    a.append(c)
print(min(a))