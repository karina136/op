# -- coding: utf-8 --
n=int(input("Введите натуральное число n= "))
def fun(a):
    s=0
    x=1
    for i in range(1,a+1):
        x *= i
        s += x
    return(s)
print(fun(n))