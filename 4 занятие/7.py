# -- coding: utf-8 --
n=int(input("Введите натуральное число n= "))
s=0
x=1
for i in range(1,n+1):
    x *= i
    s += x
print(s)