from turtle import *
screensize(5000,5000)
tracer(0)
lt(90)
down()
k = 30

for i in range(3):
    fd(2*k)
    rt(90)
    fd(3*k)
    lt(90)
rt(180)
fd(6*k)
rt(90)
fd(9*k)
up()
back(3*k)
rt(90)
down()
for i in range(2):
    fd(1*k)
    rt(90)
    fd(2*k)
    lt(90)
rt(180)
fd(3*k)
rt(90)
fd(4*k)
rt(90)
fd(1*k)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')

done()