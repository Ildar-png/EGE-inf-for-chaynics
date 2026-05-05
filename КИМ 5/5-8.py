def dev(k):
    s = ''
    while k > 0:
        s += str(k % 9)
        k//=9
    return s[::-1]
a = []
for n in range(1,100000):
    n9 = dev(n)
    if n9[0] == '7':
        n9 = n9.replace('6', 'x')
        n9 = n9.replace('3', 'y')
        n9 = n9.replace('x', '3')
        n9 = n9.replace('y', '6')
        n9 = '34' + n9
    else:
        n9 += '45'
        n9 = '3' + n9[1:]
    r = int(n9,9)
    if r < 2876:
        a.append(r)
z = []
for n in range(1,100000):
    n9 = dev(n)
    if n9[0] == '7':
        n9 = n9.replace('6', 'x')
        n9 = n9.replace('3', 'y')
        n9 = n9.replace('x', '3')
        n9 = n9.replace('y', '6')
        n9 = '34' + n9
    else:
        n9 += '45'
        n9 = '3' + n9[1:]
    r = int(n9,9)
    if r == max(a):
        z.append(n)
print(max(z))
