'''from re import*
f = open('')
s = f.readline()
res = findall(r'[1-9A-J]*', s)
print(len(max(res, key = len)))'''

'''from re import*
f = open('')
s = f.readline()
res = findall(r'[\dAB]*[02468A]',s)
print(max(res, key = len))
print(len(max(res, key = len)))
'''

'''from re import*
f = open('')
s = f.readline()
res = findall(r'[\dAB]*[06]',s)
print(max(res,key = len))
print(len(max(res,key = len)))'''

'''from re import*
f = open('')
s = f.readline()
res = findall((r'[123][0123]*(?:[+*][123][0123]*)*'))
print(max(res,key = len))
print(len(max(res,key = len)))'''

'''from re import*
f = open('')
s = f.readline()
res = findall(r'[456][0456]*(?:[*+][456][0456]*)*',s)
print(max(res,key = len))
print(len(max(res,key = len)))'''

'''from re import*
f= open('')
s = f.readline()
res = findall(r'[345][0345]*(?:[*][345][0345]*)*',s)
print(max(res,key = eval))
print(eval(max(res,key = eval)))'''

'''from re import*
f= open('')
s = f.readline()
res = findall(r'[789][0789]*(?:[*][789][0789]*)*',s)
print(max(res,key = eval))
print(eval(max(res,key = eval)))'''

'''from re import*
f = open('')
s = f.readline()
res = findall(r'(?:0|[+-]?[1234][01234]*)(?:[+-](?:0|[+-]?[1234][01234]*))*',s)
print(max(res,key = len))
print(len(max(res,key = len)))'''

from re import*
f = open('')
s = f.readline()
res = findall(r'(?:0|[1-9][0-9]*)(?:[-*](?:0|[1-9][0-9]*))*',s)
print(max(res,key = len))
print(len(max(res,key = len)))