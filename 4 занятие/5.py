# -- coding: utf-8 --
n=int(input("Введите натуральное число: "))
summa=0
def fun(x,y):
    for i in range (1,x+1):
        y += i**3
    print(y)
fun(n,summa)
