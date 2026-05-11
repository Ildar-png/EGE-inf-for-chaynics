'''from math import*
f = open('27-3-A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
k = 2
clusters = [[] for _ in range(k)]
for x,y in points:
    if y > -1:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    misterbist = 10**10
    for c1 in clusters[i]:
        sumbist = 0
        for p1 in clusters[i]:
            sumbist += dist(c1,p1)
        if sumbist < misterbist:
            misterbist = sumbist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids]) / k
Py = sum([y for x,y in bestcentroids]) / k
print('A - ', abs(int(Px*10000)),abs(int(Py*10000)))

f = open('27-3-B.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
k = 3
clusters = [[] for _ in range(k)]
for x,y in points:
    if y > 0:
        clusters[0].append([x,y])
    elif x < -1:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    misterbist = 10**10
    for c1 in clusters[i]:
        sumbist = 0
        for p1 in clusters[i]:
            sumbist += dist(c1,p1)
        if sumbist < misterbist:
            misterbist = sumbist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids]) / k
Py = sum([y for x,y in bestcentroids]) / k
print('B - ', abs(int(Px*10000)),abs(int(Py*10000)))'''

from math import*
f = open('27-4-A.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
k = 2
clusters = [[] for _ in range(k)]
for x,y in points:
    if y > 1:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    misterbist = 10**10
    for c1 in clusters[i]:
        sumbist = 0
        for p1 in clusters[i]:
            sumbist += dist(c1,p1)
        if sumbist < misterbist:
            misterbist = sumbist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids]) / k
Py = sum([y for x,y in bestcentroids]) / k
print('A - ', abs(int(Px*10000)),abs(int(Py*10000)))

f = open('27-4-B.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
k = 3
clusters = [[] for _ in range(k)]
for x,y in points:
    if y < -1:
        clusters[0].append([x,y])
    elif x < 0:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    misterbist = 10**10
    for c1 in clusters[i]:
        sumbist = 0
        for p1 in clusters[i]:
            sumbist += dist(c1,p1)
        if sumbist < misterbist:
            misterbist = sumbist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids]) / k
Py = sum([y for x,y in bestcentroids]) / k
print('B - ', abs(int(Px*10000)),abs(int(Py*10000)))