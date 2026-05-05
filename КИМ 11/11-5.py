from math import *
for i in range(1,100000):
    N = 256
    V = ceil((N * i)/8)
    V1 = 32768 * V
    if V1 > 8*1024*1024:
        print(2**(i-1)+1)
        break