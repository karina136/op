# -- coding: utf-8 --
n=int(input("Введите натуральное число n= "))
x=1
def fun(a,b):
    for i in range(1,a+1):
        b *=i
    print("n!= ",b)
fun(n,x)