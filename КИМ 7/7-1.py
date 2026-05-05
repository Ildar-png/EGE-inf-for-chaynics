from math import * # Импорт библиотеки математика
for n in range(1,10000): # Перебор искомого значения
    N = 1280 * 720 # Переписывание условия
    i = ceil(log2(8192)) # Округленный в меньшую сторону до целого числа двоичный логарифм
    Vn = N * i * n # Объем n-ного кол-ва данных
    t = Vn/1474560 # Время передачи данных
    if t <= 280: # Условие
        print(n)

'''from math import *
for n in range(1,10000):
    N = 1920*1080
    i = ceil(log2(16384))
    Vn = N * i * n
    if (Vn/524288) <= 256:
        print(n)'''

'''from math import *
for i in range(1,10000):
    N = 1050*460
    Vn = N*i*64
    if (Vn/1474560)<=200:
        print(2**i)'''

'''from math import *
for i in range(1,10000):
    N = 1024*1024
    Vn = N*i*128
    if (Vn/524288)<=256:
        print(2**i)'''

'''from math import *
for n in range(1,10000):
    N = 1024 * 768
    i = ceil(log2(256))
    V = N * i * n * 0.15
    if (V/(750* 2**13)) <=  1:
        print(n)'''

'''from math import *
for i in range(1,10000):
    V = 2 * i * 48000 * 1 * 0.16
    if (V/(45 * 2**13))<=1:
        print(i)'''