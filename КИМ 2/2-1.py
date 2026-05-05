print('x y z w F') # Первая строка таблицы для удобства
for x in range(2): # Перебор значений
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= z) == y) <= x # Ф-ция из условия
                if F == 0: # Значение ф-ции
                    print(x,y,z,w,int(F)) # Вывод в той же последовательности