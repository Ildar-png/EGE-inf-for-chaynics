from math import * # Импорт библиотеки математика
for N in range(1,10000): # Перебор искомого значения
    A = 10 + 52 + 1000 # Алфавит, состоящий из разных символов
    i = ceil(log2(A)) # Вес одного символа через целую степень двойки
    V1 = ceil((N * i)/8) # Объем 1 штуки в байтах
    V777 = (777 * V1)/1024 # Объем n штук
    if V777 <= 276: # Условие
        print(N) # Ответ

'''for N in range(1,10000):
    A = 10 + 26 + 232
    i = ceil(log2(A))
    V1 = ceil((N * i) / 8)
    V760 = (V1 * 760) / 1024
    if V760 > 140:
        print(N)
        break'''

'''for A in range(1,10000):
    N = 191
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 *131072)/(2**20)
    if V > 22:
        print(A)'''

'''for A in range(1,10000):
    N = 205
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 * 8192)/1024
    if V <= 899:
        print(A)'''

'''for N in range(1,10000):
    A = 10 + 52 + 980
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 * 385)/1024
    if V < 136:
        print(N)'''

'''for N in range(1,10000):
    A = 10 + 52 + 5000
    i = ceil(log2(A))
    V1 = (N*i)/8
    V = (V1*949)/1024
    if V > 727:
        print(N)
        break'''

'''for A in range(1,100000):
    N = 283
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (65536*V1)/(2**20)
    if V > 15:
        print(A)
        break'''