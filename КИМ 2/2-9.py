a = []
for t in range(1,1000000):
    n = 2
    nu = 48000
    i = 24
    V1 = t * n * nu * i
    V = 20 * 1024 * 1024 * 8
    if (V1*1.4)<= V:
        a.append(t)
print(max(a))
