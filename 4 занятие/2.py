# -- coding: utf-8 --
A=int(input("Введите первое число: "))
B=int(input("Введите второе число: "))
def fun(x,y):
    if x<y:
        for i in range(x,y+1):
            print (i, end=";")
    elif x>=y:
        for i in range(x,y-1, -1):
            print (i, end=";")
fun(A,B)