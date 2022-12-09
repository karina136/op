# -- coding: utf-8 --
x = int(input("Введите x: "))
y = int(input("Введите y: "))
def fun(a,b):
    days = 1
    while a < b:
        a += (a*0.1)
        days += 1
    print(days)
fun(x,y)