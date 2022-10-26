# -- coding: utf-8 --
x = int(input("Введите x: "))
y = int(input("Введите y: "))
days = 1
while x < y:
    x += (x*0.1)
    days += 1
print(days)