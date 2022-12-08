# -- coding: utf-8 --
A=int(input("Введите первое число: "))
B=int(input("Введите второе число: "))
def function(x,y):
    if x<=y:
        for i in range(x,y+1):
            print (i, end=";")
function(A,B)