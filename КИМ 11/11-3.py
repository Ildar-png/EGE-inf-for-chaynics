from math import *
n = 116
A = 113
i = ceil(log2(A))
V = ceil((n * i)/8)
V1 = ceil((V * 301504)/(1024*1024))
print(V1)