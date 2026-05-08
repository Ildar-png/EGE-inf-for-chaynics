'''import re
f = open('')
s = f.readline()
isok = re.findall(r'9?8?7?6?5?4?3?2?1?0?',s) #? после символа означает 0 или 1 повторение
print(max(isok, key = len))'''

'''import re
f = open('24-1_hometask1.txt')
s = f.readline()
isok = re.findall(r'(?:XYZ)+X?Y?',s)
print(len(max(isok,key = len)))'''

'''import re
f = open('24-1_hometask2.txt')
s = f.readline()
isok = re.findall(r'(?:[\d]+[-+*])+[\d]',s)
print(max(isok,key = len))
print(len(max(isok,key = len)))
'''

import re
f = open("24-1_hometask3.txt")
valid = []
for s in f:
    s = s.strip()
    if re.fullmatch(r'^\d+([-+*]\d+)*$', s):
        valid.append(s)
print(len(valid))
