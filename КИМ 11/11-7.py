from math import*
for N in range(1,10000):
    A = 10 + 26 + 34
    i = ceil(log2(A))
    V = ceil((N * i)/8)
    V1 = V * 1142
    if V1 >= 305 * 1024:
        print(N)
        break
print(int('1000100000',2))