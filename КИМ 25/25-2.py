#Задачи на делители
#Они сложные только из-за дурацких формулировок, нужно внимательно читать что дано в задании и что нужно найти
for n in range(123456,123487+1): #В условии дан диапазон, переписываем его, добавляя 1 к концу, чтобы значение включилось в перебор
    deliteli = []
    for i in range(1,n+1): #Перебираем числа от 1 до самого числа включительно
        if n % i == 0: #Если число без остатка делится на i...
            deliteli.append(i) #То это делитель, записываем его в список
    if len(deliteli) == 6: #Если у числа нашлось 6 делителей...
        print(deliteli) #Выводим их, как просят в задании

'''for n in range(15545,15844 +1):
    deli = []
    for i in range(2,n): #Иногда нужно перебирать делители не включая 1 и само число, поэтому начинаем перебор с 2 и не добавляем 1 к числу
        if n % i == 0:
            deli.append(i)
    if len(deli) == 5:
        print(n,max(deli))'''

'''c = 0
for n in range(950001,950001+1000): #Когда просят перебрать числа больше н-ного, перебираем 1000 чисел после него, не включая само число
    F = 0 #Значение дополнительной переменной поясняется в задании
    for i in range(2,n):
        if n % i == 0:
            F = n//i - i #Тут F = разница между мин и макс делителями числа. Находим сначала мин делитель, делин число на него, получаем максимальный
            break
    if F != 0 and F % 13 == 0:
        print(n,F)
        c += 1
    if c == 5: #Нам нужно только первые 5 подходящих случаев, вводим обычный счетчик
        break'''

'''def isprime(x): #Для упрощения некоторых задач лучше отдельно написать ф-цию. Эта проверяет число на простоту
    for i in range(2,x): #Перебираем числа, не включая 1 и само число
        if x % i == 0: #Если нашелся делитель...
            return 0 #Число не простое
    return 1 #Если ничего не нашлось, значит простое
c= 0
for n in range(1000001,1000001+1000):
    for i in range(2,n):
        if n % i == 0:
            if isprime(n//i):
                print(n,n//i)
                c+=1
            break #Break должен стоять именно тут, это важно
    if c == 5:
        break'''

'''c = 0
for n in range(800001, 800000+1000):
    for i in range(111,n,100): #Если делитель должен кончаться на определенные цифры, нужно делать такой перебор с шагом. Тут для числа 11
        if n % i == 0:
            print(n,i)
            c += 1
            break
    if c == 5:
        break'''

'''c = 0
for n in range(800001,800001 + 1000):
    deli = []
    for i in range(2,n):
        if n % i == 0:
            deli.append(i)
    F = 0
    if len(deli) > 1:
        F = deli[0] * deli[-2]
    if F != 0 and F % sum(deli[:2]) == 0:
        print(n,F)
        c += 1
    if c == 5:
        break'''

'''for n in range(200123,200150+1):
    deli = []
    for i in range(1,n+1):
        if n % i == 0:
            deli.append(i)
    if len(deli) == 4:
        print(n,sum(deli)/4)'''

'''for n in range(14620,15000+1):
    deli = []
    for i in range(2,n):
        if n % i == 0:
            deli.append(i)
    if len(deli) == 3:
        print(n,min(deli))'''

'''c = 0
for n in range(700001,700001+1000):
    F = 0
    for i in range(2,n):
        if n % i == 0:
            F = n//i - i
            break
    if F != 0 and F % 9 == 0:
        print(n,F)
        c += 1
    if c == 5:
        break'''

'''c = 0
for n in range(600001,600001+1000):
    for i in range(17,n,10):
        if n % i == 0:
            print(n,i)
            c += 1
            break
    if c == 5:
        break'''

c = 0
def isprost(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
for n in range(610001,610001+1000):
    for i in range(2,n):
        if n % i == 0:
            if isprost(n//i):
                print(n,n//i)
                c += 1
            break
    if c == 6:
        break
