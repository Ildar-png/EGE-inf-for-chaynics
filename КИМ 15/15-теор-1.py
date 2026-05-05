def Del(n,m): #Создание ф-ции ДЕЛ
    return n % m == 0 #Если остаток деления n на m равен 0, выводит True

for a in range(1,1000): #Перебор значений А
    a_otwet = True #Ввод новой переменной
    for x in range(1,10000): #Перебор всех возможных иксов
        if ((Del(x,a) and Del(x,24)) <= Del(x,36)) == False: #Если условие не выполнилось
            a_otwet = False #Переменная принимает значение лжи и цик запускается заново
            break
    if a_otwet == True: #Если переменная не поменялась(то есть при любых х выполняется условие)
        print(a) #То выводит подходящуу под ответ А
        break #Все переборы идут с наименьшего, значит первый подходящий А будет ответом и можно остановить цикл
#Ответ в этом номере - наименьшее выведенное значение (9)

'''def Del(n,m):
    return n % m == 0

for a in range(1,1000):
    a_otwet = True
    for x in range(1,10000):
        if ((Del(x,64) and (not(Del(x,24)))) <= (not(Del(x,a)))) == False:
            a_otwet = False
            break
    if a_otwet == True:
        print(a)
        break'''

'''def Del(n,m):
    return n % m == 0

for a in range(1,10000):
    a_otwet = True
    for x in range(1,10000):
        if ((not(Del(x,a))) <= ((Del(x,45)) <= (not(Del(x,75))))) == False:
            a_otwet = False
            break
    if a_otwet:
        print(a)'''