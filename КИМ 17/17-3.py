'''f = open('17-9.txt')
a = [int(s) for s in f]
sumpar = []
sr = sum(a)/len(a)
for i in range(len(a) - 1):
    if ((a[i] > sr) or (a[i+1] > sr)) and ((a[i] % 7 == 0) or (a[i + 1] % 7 == 0)):
        sumpar.append(a[i] * a[i+1])
print(len(a), max(sumpar))'''

f = open('17-11.txt')
a = [int(s) for s in f]
sumpar = []
sr = max([z for z in a if (999<z<10000 and z % 100 == 43)])
for i in range(len(a) - 1):
    if (999<abs(a[i])<10000 or 999<abs(a[i+1])<10000) and ((a[i] + a[i+1])**2 < sr**2):
        sumpar.append((a[i] + a[i+1])**2)
print(len(sumpar), max(sumpar))