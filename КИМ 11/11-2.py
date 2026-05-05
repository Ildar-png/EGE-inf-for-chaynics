from math import *
n = 200
A = 10 + 2040
i = ceil(log2(A))
V = ceil((n * i)/8)
V1 = ceil((V * 98304)/1024)
print(V1)
