# -- coding: utf-8 --
n = int(input("Введите число: "))
i = 2
def fun(x,y):
    while x % y != 0:
        y += 1
    print("Наименьший натуральный делитель:", y)
fun(n,i)