f = open('17.7.txt')
a = [int(s) for s in f]
sumpar = []
for i in range(len(a) - 1):
    x = -100000000
    y = -100000000
    if 999 < a[i] < 10000 and a[i] % 100 == 43:
        x = a[i]
    if 999 < a[i+1] < 10000 and a[i+1] % 100 == 43:
        y = a[i+1]
    if (999 < a[i] < 10000 or 999 < a[i+1] < 10000) and ((a[i] + a[i+1])**2 < (max(x,y))**2):
        sumpar.append((a[i] + a[i+1])**2)
print(len(sumpar), max(sumpar))