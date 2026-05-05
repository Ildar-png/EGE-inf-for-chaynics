'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(1,14))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)
print(f(2,56))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)+f(s**2,e)
print(f(4,93))'''

'''def f(s,e):
    if s > e or s == 27:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)
print(f(3,15)*f(15,72))'''

'''def f(s,e):
    if s > e or s == 44:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*3,e)
print(f(2,24)*f(24,144))'''

'''def f(s,e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s-1,e)+f(s//3,e)
print(f(49,11)*f(11,1))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s+10,e)
print(f(2,45))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)+f(s*2+1,e)
print(f(3,90))'''

def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*10+1,e)
print(f(1,928))