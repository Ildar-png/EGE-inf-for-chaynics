def f(n): # Создание ф-ции
    if n < 2: # Условие
        return 1
    return f(n-1)*(n+5) # Другое условие
print(f(2))

'''def f(n):
    if n == 1:
        return 3
    return 4 * f(n-1) - 3 * n
print(f(5))'''

'''def f(n):
    if n > 15:
        return n * 2
    return 2 * f(n + 2) + 4 * n
print(f(7))'''

'''def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n-1) + 7
    else:
        return f(n-2) + 4 * n
print(f(100))
'''

'''def f(n):
    if n <= 4:
        return 0
    if n > 4 and n % 4 == 0:
        return f(n-1) + 3 * n
    else:
        return f(n-(n%4)) + 8 * n - 2
print(f(43))'''

'''def f(n):
    if n == 2:
        return 1
    if n > 2 :
        return 3*f(n - 1) + 4*g(n - 1) - n*2 + 4


def g(n):
    if n == 2 :
        return 1
    if n > 2:
        return 4*f(n-1)+3*g(n-1)+6

print(f(8)+g(8))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1 :
        return g(n - 1) + 3*f(n - 1) - n*5 + 1'''


'''def g(n):
    if n == 1 :
        return 1
    if n > 1:
        return 2*f(n-1)-g(n-1)+4*n-2

print(g(12))'''
