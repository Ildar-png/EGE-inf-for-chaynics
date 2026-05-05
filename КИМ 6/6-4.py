from turtle import *
down()
lt(90)
tracer(0)
screensize(5000,5000)
k = 20
for i in range(2):
    fd(3*k)
    lt(90)
    back(10*k)
    lt(90)
up()
back(10*k)
rt(90)
fd(8*k)
lt(90)
down()
for i in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done()