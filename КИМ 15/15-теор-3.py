'''for a in range(1,10000): # Перебор значений. а можно брать большой, а вот х и у лучше брать поменьше
    a_otw = True # Ввод специальной переменной
    for x in range(1,1000):
        for y in range(1,1000):
            if ((17*x - 3*y + 17 != 0) or (a < x) or (a < y)) == False:
                a_otw = False
                break
        if a_otw == False: # Нужно выходить из двух циклов, проверяя специальную переменную
            break
    if a_otw == True:
        print(a)'''

'''for a in range(1,10000):
    a_otw = True
    for x in range(1,1000):
        for y in range(1,1000):
            if (((x >= 17) or (3*x < y)) or (y*x < a)) == False:
                a_otw = False
                break
        if a_otw == False:
            break
    if a_otw == True:
        print(a)
        break'''

'''for a in range(1,10000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((y - 13*x < a) or (x > 88) or (y > 77)) == False:
                break
        if ((y - 13*x < a) or (x > 88) or (y > 77)) == False: # Можно вместо ввода новой переменной писать еще раз условие выхода из цикла
            break
    else:
        print(a)
        break'''

'''for a in range(1,10000):
    if all((((y + 7*x != 36) or (a > x - 2)) or (a < y + 27)) for x in range(1,1000) for y in range(1,1000)): # Проверка условия, записанная в одну строку с генератором х и у
        print(a)
        break'''
