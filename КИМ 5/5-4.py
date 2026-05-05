a = []
for n in range(1,10000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
       n2 += bin((n % 3) * 3)[2:]
    R = int(n2,2)
    if R == 134:
        a.append(n)
print(max(a))