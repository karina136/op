# -- coding: utf-8 --
import math
x=float(input("Введите переменную x: "))
y=float(input("Введите переменную y: "))
z=float(input("Введите переменную Z: "))
s=(math.sqrt(10*(math.pow(x,1/3)+math.pow(x,y+2))))*(math.asin(z)*math.asin(z)-abs(x-y))
print("s={0:.4f}".format(s))