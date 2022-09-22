# -- coding: utf-8 --
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
def min(a,b,c):
        if a<b and a<c:
            print(a)
        if b<a and b<c:
            print(b)
        if c<a and c<b:
            print(c)
min(a,b,c)