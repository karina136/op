# -- coding: utf-8 --
N=int(input("Введите число N = "))
i = 1
def fun(x,y):
    while (y**2) <=x :
        print(y**2, end=' ')
        y += 1
fun(N,i)