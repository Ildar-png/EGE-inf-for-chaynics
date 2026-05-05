def f(s,e):
    if s < e or s == 28:
        return 0
    if s == e:
        return 1
    return f(s-3,e) + f(s//3,e) + f(s//2,e)
print(f(46,20)*f(20,3))