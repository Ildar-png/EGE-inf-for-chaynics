'''p = list(range(3,19)) # Задаем отрезки из условия, помни, что конец пишется не включительно, значит нужно писать на 1 больше
q = list(range(11,25))
a = [] # Создаем пустой "отрезок"
for x in range(1,100): # Перебираем а
    if (((x in p) and (x in q)) <= (x in a)) == False: # Если условие не выполняется...
        a.append(x) # Добавляем значение на отрезок
print(a) # Итоговый полученный отрезок в форме списка с входящими туда значениями
print(max(a) - min(a)) # Длина отрезка, это максимальное минус минимальное
'''

'''p = list(range(16,60))
q = list(range(27,72))
a = []
for x in range(1,1000):
    if ((not(x in a)) <= ((x in p) <= (not(x in q)))) == False:
        a.append(x)
print(a)
print(max(a)-min(a))'''

'''p =list(range(13,34))
q =list(range(22,46))
a = []
for x in range(1,100):
    if ((not(x in a)) <= (((x in p) and (x in q)) <= (x in a))) == False:
        a.append(x)
print(a)
print(max(a) - min(a))'''

'''p =list(range(11,29))
q =list(range(21,42))
a = list(range(1,100)) # Нужен наибольший а, поэтому берем заполненный список, вместо пустого
for x in range(1,100):
    if (((x in p) <= (x in q)) <= (not(x in a))) == False:
        a.remove(x) # А здесь убираем значения, вместо того, чтобы добавлять
print(a) 
print(21 - 11) # Отрезок выбирается среди данных в условии чисел, тут мин - 11, макс - 20, но 20 нет, значит ответ 21 - 11 = 10
'''

p = list(range(13,33))
q = list(range(15,20))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(32 - 13)