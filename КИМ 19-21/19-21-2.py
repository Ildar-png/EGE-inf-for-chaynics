def f(s1,s2,m): #Две кучи
    if s1 + s2 >= 211: #Условие выигрыша
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1+1,s2,m-1), f(s1*2,s2,m-1),f(s1,s2+1,m-1), f(s1,s2*2,m-1)] #Список ходов для 2 куч
    return any(h) if m % 2 != 0 else all(h) #Если ход НЕУДАЧНЫЙ all меняется на any в рамках одного номера
print('19 - ', [s for s in range(2,194) if not f(17,s,1) and f(17,s,2)])
print('20 - ', [s for s in range(2,194) if not f(17,s,1) and f(17,s,3)])
print('21 - ', [s for s in range(2,194) if not f(17,s,2) and f(17,s,4)])
