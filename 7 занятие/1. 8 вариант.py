# -- coding: utf-8 --
from math import prod
n=int(input("Введите длину списка: "))
x=[int(input()) for i in range(n)]
print(x)
b=sum(x)
print("сумма чисел из списка: ", b)
c=prod(x)
print("произведение чисел из списка: ", c)