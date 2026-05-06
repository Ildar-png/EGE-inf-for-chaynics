#Тут появляются регулярки. Это шаблон, по которому прога ищет подходящие значения
import re #Импорт библиотеки
f = open('24reg_hometask1.txt')
s = f.readline()
isok = re.findall(r'[A-Z]+',s) #В список заносятся все значения по шаблону. В данном случае в строке s ищет максимальное кол-во (+) подряд идущих заглавных латинских букв от A до Z ([A-Z])
print(len(max(isok, key = len))) #Ответ - длина максимального по длине элемента списка найденных значений

#Пример регулярки - номер телефона. Он строится по шаблону, поэтому можно явно сказать что является номером, а что нет
#Шаблон выглядит так - +(7 или 8)-(ХХХ)-ХХХ-ХХ-ХХ
#Регулярка - r'\+[78]-\(\d\d\d\)-\d\d\d-\d\d-\d\d'

'''import re
f = open('24reg_hometask2.txt')
s = f.readline()
isok = re.findall(r'[0-9+\-/*=()]+',s) #Регулярки сложновато писать. Некоторые символы являются в них служебными (+-*), поэтому чтобы обозначить их именно как обычный символ, нужно отделить их знаком \
print(len(max(isok,key = len)))'''

'''import re
f = open('24reg_hometask3.txt')
s = f.readline()
isok = re.findall(r'[1-9A-G]+',s) #Так обозначается список символов от 1 до 0 и от A до G, что входит в 17-ричную сист. счис. по заданию
print(len(max(isok,key = len)))'''

'''import re
f = open('')
s = f.readline()
isok = re.findall(r'[a-z]+',s)
print(len(max(isok,key = len)))'''

'''import re
f = open('')
s = f.readline()
isdig = re.findall(r'[0-9]+',s)
isop = re.findall(r'[-+/*]+',s)
print(len(max(isdig,key = len)))
print(len(max(isop,key = len)))'''

'''import re
f = open('')
c = 0
for s in f:
    tel = re.findall(r'\+[78]-\(\d{3}\)-\d{3}-\d{2}-\d{2}',s)
    if tel:
        c += 1
print(c)'''

'''import re
f = open('')
isok = []
for s in f:
    ismail = re.findall(r'\w+@\w\.\w+')
    if ismail:
        isok.append()
print(len(min(isok,key = len)))
print(len(max(isok,key = len)))'''


