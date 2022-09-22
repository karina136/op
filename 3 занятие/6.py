# -- coding: utf-8 --
a=int(input("Номер столбца первого квадрата: "))
b=int(input("Номер строки первого квадрата: "))
c=int(input("Номер столбца второго квадрата: "))
d=int(input("Номер строки второго квадрата: "))
def add(a,b):
    return((a+b)%2)
def add(c,d):
    return((c+d)%2)
if (add(a,b)==add(c,d)):
    print("Да")
else:
    print("Нет")
