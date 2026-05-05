from math import *
for N in range(1,10000):
    A = 10 + 26*2 + 8164
    i = ceil(log2(A))
    v = ceil((N * i)/8)
    v1 = v * 835
    if v1 > 156 * 1024:
        print(N)
        break
