from turtle import *
lt(90)
tracer(0)
screensize(5000,5000)
down()
k = 20

lt(180)
for i in range(3):
    rt(45)
    fd(12*k)
    rt(45)
lt(315)
fd(12*k)
for i in range(2):
    rt(90)
    fd(12*k)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done()