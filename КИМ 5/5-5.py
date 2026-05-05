q = []
for n in range(10000,100000):
    a = [int(x) for x in str(n)]
    s = sum(a)
    m = max(a) + min(a)
    l = a[0]
    r = a[-1]
    p1 = s - l
    p2 = m - r
    if p1>p2:
        z = str(p2) + str(p1)
    else:
        z = str(p2) + str(p1)
    if z == '222':
        q.append(n)
print(max(q))
