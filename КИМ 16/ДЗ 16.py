'''def f(n):
    if n == 1:
        return 2
    if n > 1:
        return f(n-1)+3
print(f(3))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*2
print(f(4))'''

'''def f(n):
    if n == 0:
        return 5
    if n > 0:
        return f(n-1)+2
print(f(2))'''

'''def f(n):
    if n == 1:
        return 3
    if n > 1:
        return f(n-1)+(n-1)*n
print(f(18))'''

'''def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 4* f(n-1) + 2*n
print(f(8))'''

'''def f(n):
    if n < 4 :
        return 4 * n - 1
    if n % 2 == 0:
        return f(n - 2) + 2 * n
    else:
        return f(n-4) + 4*n + 5
print(f(62))'''

'''def f(n):
    if n == 0  :
        return 0
    if n > 0 and n % 3 == 0:
        return f(n - 1) + 3 * n
    if n > 0 and n % 3 > 0:
        return f(n - (n % 3)) + 8 * n - 2
print(f(30))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (3 * f(n - 1) - g(n - 1)) * 2

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - 3 * g(n - 1) + 1
print(f(7))'''

'''def f(n):
    if n > 10  :
        return n
    if n <= 10:
        return 2 * f(n + 1) + 2 * n
print(f(4))'''

def f(n):
    if n == 1  :
        return 4
    if n > 1:
        return 5 * f(n - 1) - 2 * n
print(f(6))

