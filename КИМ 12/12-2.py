comm = {
    (' ', 0): (' ',1,1),
    (' ', 1): ('0',1,2),
    ('0', 1): ('0',1,1),
    ('1', 1): ('1',1,1),
    (' ', 2): ('0',1,3),
    (' ', 3): (' ',2,3),
}

def mt(s):
    s = list(' ' + s + '          ')
    q = 0
    i = 0
    while True:
        cmd = comm[ (s[i] , q) ]
        s[i] = cmd[0]
        if cmd[1] == 2: break
        i += cmd[1]
        q = cmd[2]
    return ''.join(s)

x = bin(2028)[2:]
print(int(mt(x),2))
