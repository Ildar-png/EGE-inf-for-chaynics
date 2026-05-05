'''from itertools import*
from string import*
a = 0
for i in product(printable[:5],repeat = 6):
    i = ''.join(i)
    if i[-1] != '3' and i[-1] != '4' and i[0] != '1' and i[0] != '0':
        a += 1
print(a)'''

'''ЭТОТ КОД НЕ РАБОТАЕТ
from itertools import*
a = 0
for i in product(sorted('мка'), repeat = 6):
    if i.count('м') == 1 and i.count('а') == 3 and i.count('к') == 2:
        if 'аа' not in i and 'кк' not in i:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('епсух'), repeat = 5):
    i = ''.join(i)
    if i[-1] == 'п' or i[-1] == 'с' or i[-1] == 'х':
        a += 1
    if i == 'успех':
        print(a)'''

'''a = 0
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            for w in range(0,101):
                if 1*x + 2*y + 5*z + 10*w == 100:
                    a +=1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('щэдср'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i == 'щдщд':
        print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('режимдно'), repeat = 6):
    i = ''.join(i)
    if len(i) == len(set(i)):
        i = i.replace('р','s')
        i = i.replace('е','g')
        i = i.replace('ж','s')
        i = i.replace('и','g')
        i = i.replace('м','s')
        i = i.replace('д','s')
        i = i.replace('н','s')
        i = i.replace('о','g')
        if i[0] == 's' and i[1] == 'g' and i[-1] == 'g':
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('инфа'), repeat = 6):
    i = ''.join(i)
    if i.count('ф') == 2:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('левиоса'), repeat = 7):
    i = ''.join(i)
    if len(i) == len(set(i)):
        i = i.replace('л','s')
        i = i.replace('е','g')
        i = i.replace('в','s')
        i = i.replace('и','g')
        i = i.replace('о','g')
        i = i.replace('с','s')
        i = i.replace('а','g')
        if i[0] != 'g' and i[3] != 's':
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('гафний'), repeat = 4):
    i = ''.join(i)
    if i[0] != 'й':
        i = i.replace('г','s')
        i = i.replace('а','g')
        i = i.replace('ф','s')
        i = i.replace('н','s')
        i = i.replace('и','g')
        i = i.replace('й','s')
        if i.count('g') >= 1:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('крот'), repeat = 6):
    i = ''.join(i)
    if i.count('о') == 1:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('марин'), repeat = 8):
    i = ''.join(i)
    a += 1
    if i == 'марианна':
        print(a)'''

'''from itertools import*
from string import*
a = 0
for i in product(printable[:8], repeat = 5):
    i = ''.join(i)
    if i.count('6') == 1 and i[0] != '0':
        for z in '1357':
            if f'{z}6' in i or f'6{z}' in i:
                break
        else:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('автор'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i == 'вата':
        print(a)'''

'''from itertools import*
a = 0
for i in product('геэ023', repeat = 7):
    i = ''.join(i)
    a += 1
    if i == 'егэ2023':
        x = a
    if i == '2023егэ':
        y = a
print(abs(x-y)-1)'''

from itertools import*
a = 0
for i in product(sorted('пятьдней'), repeat = 4):
    i = ''.join(i)
    a += 1
    if len(i) == len(set(i)):
        i = i.replace('п','s')
        i = i.replace('я','g')
        i = i.replace('т','s')
        i = i.replace('ь','s')
        i = i.replace('д','s')
        i = i.replace('н','s')
        i = i.replace('е','g')
        i = i.replace('й','s')
        if i.count('g') == 0:
            print(a,i)