from math import*
f = open('27-6-A.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
clusters = []
epsilon = 0.5
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1,p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)
        if len(clusters[-1]) <= 10:
            del clusters[-1]
bestcentroids = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    minsumdist = 10**10
    for p1 in clusters[i]:
        sumdist = 0
        for p2 in clusters[i]:
            sumdist += dist(p1,p2)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = p1
Px = sum([x for x,y in bestcentroids])/len(clusters)
Py = sum([y for x,y in bestcentroids])/len(clusters)
Ps = sum([len(cluster)/16 for cluster in clusters])
print((Px + Py)*10000,Ps*1000)

f = open('27-6-B.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
clusters = []
epsilon = 0.4
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1,p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)
        if len(clusters[-1]) <= 10:
            del clusters[-1]
bestcentroids = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    minsumdist = 10**10
    for p1 in clusters[i]:
        sumdist = 0
        for p2 in clusters[i]:
            sumdist += dist(p1,p2)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = p1
Px = sum([x for x,y in bestcentroids])/len(clusters)
Py = sum([y for x,y in bestcentroids])/len(clusters)
Ps = sum([len(cluster)/16 for cluster in clusters])
print((Px + Py)*10000,Ps*1000)


from turtle import*
k = 40
up()
tracer(0)
colors = ['red','green','blue','yellow']
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()

'''from math import*
f = open('27-5-A.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
clusters = []
epsilon = 0.5
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1,p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)
    if len(clusters[-1]) <= 10:
        del clusters[-1]
bestcentroids = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    minsumdist = 10**10
    for p1 in clusters[i]:
        sumdist = 0
        for p2 in clusters[i]:
            sumdist += dist(p1,p2)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = p1
Px = (sum([x for x,y in bestcentroids]) / len(clusters)) * 10000
Py = (sum([y for x,y in bestcentroids]) / len(clusters)) * 10000
Ps = [len(clusters)/9 for cluster in clusters]
print(Px,Py)

f = open('27-5-B.txt')
f.readline()
points = [list(map(float,s.replace(',','.').split())) for s in f]
clusters = []
epsilon = 0.5
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1,p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)
    if len(clusters[-1]) <= 10:
        del clusters[-1]
bestcentroids = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    minsumdist = 10**10
    for p1 in clusters[i]:
        sumdist = 0
        for p2 in clusters[i]:
            sumdist += dist(p1,p2)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = p1
Px = (sum([x for x,y in bestcentroids]) / len(clusters)) * 10000
Py = (sum([y for x,y in bestcentroids]) / len(clusters)) * 10000
Ps = [len(clusters)/9 for cluster in clusters]
print(Px,Py)

from turtle import*
k = 40
up()
tracer(0)
colors = ['green','blue','brown','red','yellow','pink','black']
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()'''

