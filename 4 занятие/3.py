# -- coding: utf-8 --
A=int(input("A= "))
B=int(input("B= "))
def fun(x,y):
    for i in range(x,y-1,-1):
        if i%2 != 0:
            print(i, end= ";")
fun(A,B)
