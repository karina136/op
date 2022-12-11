# -- coding: utf-8 --
def f():
    n=int(input('Введите число: '))
    if n==0:
        return
    else:
        print(n)
        m=int(input('Введите число: '))
        if m==0:
            return 
        return f()

f()
