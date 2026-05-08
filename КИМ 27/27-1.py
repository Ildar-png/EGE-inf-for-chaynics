#Это п*****
#Решение номера начинается с переноса информации из файлов в таблицу, а затем построения графиков в Х и У и дальнейшего анализа
from math import* #Импорт библиотеки
f = open('27-2-A.txt') #Читаем файл как обычно
f.readline() #Первая строка обозначает столбцы Х и У, их нужно пропустить, прочитав строку и никуда ее не записав
k = 2 #Кол-во кластеров из графика
points = [list(map(float ,s.replace(',','.').split())) for s in f] #Составляем список, в котором будут содержаться координаты каждой точки в виде списков из 2 значений
clusters = [[] for _ in range(k)] #Нужно создать список с k кол-вом пустых списков, они будут играть роль кластеров, в них будем записывать точки
for x, y in points: #Это цикл определения кластера точки
    if y > 3: #По графику можно понять, что любая точка с y > 3 будет принадлежать отному кластеру
        clusters[0].append([x,y]) #Добавляем точку в 1й кластер
    else: #Все остальные точки относятся к другому кластеру...
        clusters[1].append([x,y]) #Записываем их в него
bestcentroids = [[] for _ in range(k)] #Создаем список с k кол-вом пустых списков, в них будем записывать координаты центроида каждого кластера
for i in range(k): #Перебираем все кластеры
    minsumdis = 10**10 #Вводим гигантское значение минимума расстояния, чтобы при сравнении записывать все меньшее число
    for c1 in clusters[i]:
        sumdist = 0 #Вводим переменную текущего значения
        for p1 in clusters[i]:
            sumdist += dist(c1,p1) #Находим рассстояние от текущей точки до остальных
        if sumdist < minsumdis: #Если оно меньше найденного на данный момент минимального...
            minsumdis = sumdist #Переписываем минимум
            bestcentroids[i] = c1 #Записываем координаты центроида i-ного кластера
Px = sum([x for x,y in bestcentroids]) / k #Px это среднее арифм всех х, находится как сумма х всех центроидов деленная на их кол-во
Py = sum([y for x,y in bestcentroids]) / k #Аналогично для у
print(int(Px*10000),int(Py*10000)) #Выводим значения, умноженные на 10000, как просят в задании. Это ответ для файла А
#Далее копируем прогу, изменяя несколько параметров под новые условия
from math import*
f = open('27-2-B.txt') #Файл В
f.readline()
k = 3 #Новое кол-во кластеров
points = [list(map(float ,s.replace(',','.').split())) for s in f]
clusters = [[] for _ in range(k)]
for x, y in points: #Новые условия деления на кластеры
    if x > 5:
        clusters[0].append([x,y])
    elif y > 4: #Обязательно это условие пишется через elif
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    minsumdis = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdis:
            minsumdis = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids]) / k
Py = sum([y for x,y in bestcentroids]) / k
print(int(Px*10000),int(Py*10000)) #Ответ для B
#В итоге прога выведет значения в нужном порядке

'''from math import *
f = open('')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f ]
clusters = [[],[]]
for x,y in points:
    if y > 2:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x, y])
bestcentroids = [[],[]]
for i in range(len(clusters)):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/len(clusters)
Py = sum([y for x,y in bestcentroids])/len(clusters)
print(int(Px * 10000),int(Py * 10000))

f = open('')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f ]
clusters = [[],[],[]]
for x,y in points:
    if y < 0:
        clusters[0].append([x,y])
    elif x < 2:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
bestcentroids = [[],[],[]]
for i in range(len(clusters)):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/len(clusters)
Py = sum([y for x,y in bestcentroids])/len(clusters)
print(int(Px * 10000),int(Py * 10000))'''

'''from math import *
f = open('')
f.readline()
k = 2
points = [list(map(float, s.replace(',','.').split())) for s in f ]
clusters = [[] for _ in range(k)]
for x,y in points:
    if y > 2:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/ k
Py = sum([y for x,y in bestcentroids])/ k
print(int(Px * 10000),int(Py * 10000))

from math import *
f = open('')
f.readline()
k = 3
points = [list(map(float, s.replace(',','.').split())) for s in f ]
clusters = [[] for _ in range(k)]
for x,y in points:
    if x > 21:
        clusters[0].append([x,y])
    elif  x > 10:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/ k
Py = sum([y for x,y in bestcentroids])/ k
print(int(Px * 10000),int(Py * 10000))
'''

'''from math import*
f = open('27-1-A.txt')
f.readline()
k = 2
points = [list(map(float, s.replace(',','.').split())) for s in f]
clusters = [[] for _ in range(k)]
for x,y in points:
    if x > 15:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/k
Py = sum([y for x,y in bestcentroids])/k
print(int(Px * 10000),int(Py * 10000))

from math import*
f = open('27-1-B.txt')
f.readline()
k = 3
points = [list(map(float, s.replace(',','.').split())) for s in f]
clusters = [[] for _ in range(k)]
for x,y in points:
    if x < 5:
        clusters[0].append([x,y])
    elif y > 10:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
bestcentroids = [[] for _ in range(k)]
for i in range(k):
    minsumdist = 10**10
    for c1 in clusters[i]:
        sumdist = 0
        for p1 in clusters[i]:
            sumdist += dist(c1,p1)
        if sumdist < minsumdist:
            minsumdist = sumdist
            bestcentroids[i] = c1
Px = sum([x for x,y in bestcentroids])/k
Py = sum([y for x,y in bestcentroids])/k
print(int(Px * 10000),int(Py * 10000))'''


