# -- coding: utf-8 --
n=int(input("Введите натуральное число n= "))
x=1
for i in range(1,n+1):
    x *=i
print("n!= ",x)