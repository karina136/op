# -- coding: utf-8 --
a = 0
def fun (x):
    for i in range(int(input("Количество чисел N= "))):
        x += int(input("Введите числа: "))
    print(x)
fun(a)