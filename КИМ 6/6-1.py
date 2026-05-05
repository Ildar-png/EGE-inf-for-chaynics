from turtle import * # Импорт библиотеки
lt(90)
down()
tracer(0)
screensize(5000,5000)
k = 20 # Коэффициент
# Строки 1 - 6 - шаблон, далее - переписывание условия, менять k для удобства
for i in range(2):
    fd(10*k) # Умножать на k при движении
    rt(90) # Углы поворота не умножать ни на что
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(7*k)
lt(90)
down()
for a in range(2):
    fd(10*k)
    rt(90)
    fd(7*k)
    rt(90)
#Шаблонный цикл рассталения точек
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done() # Конец