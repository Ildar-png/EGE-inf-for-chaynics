'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(2,4))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)
print(f(1,5))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(1,16))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*3,e)+f(s**2,e)
print(f(3,77))'''

'''def f(s,e):
    if s > e or s == 30:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)
print(f(3,20)*f(20,80))'''

'''def f(s,e):
    if s > e or s == 19:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(2,10)*f(10,29))'''

'''def f(s,e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s-1,e)+f(s//3,e)
print(f(33,7)*f(7,2))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s+10,e)
print(f(12,27))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)+f(s*2+1,e)
print(f(1,24))'''

def f(s,e):
    if s > e or s == 50:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*4,e)
print(f(1,12)*f(12,118))