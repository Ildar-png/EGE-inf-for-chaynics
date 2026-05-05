def f(s,e):
    if s < e or s == 48:
        return 0
    if s == e:
        return 1
    return f(s-1,e) + f(s//2,e) + f(s//3,e)
def d(s,e):
    if s < e or s == 61:
        return 0
    if s == e:
        return 1
    return d(s-1,e) + d(s//2,e) + d(s//3,e)
print(f(106,61)*f(61,6) + d(106,48)*d(48,6))