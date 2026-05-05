from math import *
N = 14
A = 10 + 18*2
i = ceil(log2(A))
V1 = ceil((log2(1025))/8)
V = ceil((N * i)/8) + V1
print(V*80)
