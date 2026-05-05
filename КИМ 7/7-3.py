a = []
for i in range(1,10000):
    N = 32*1024
    V = 28*1024*8
    P = 2**i
    if N*i<=V:
        a.append(P)
print(max(a))