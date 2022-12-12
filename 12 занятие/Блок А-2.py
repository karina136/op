# -- coding: utf-8 --
def f(z,x):
    if (z-x)<0:
        return z
    elif (z-x)==0:
        return 0
    else:
        return f((z-x),x)

a = int(input('Введите a: '))
b = int(input('Введите b: '))
print("Остаток от деления a на b=",f(a,b))
