# -- coding: utf-8 --
N=int(input("Введите количество чисел ряда N = "))
def fun(n):
    a = 1
    b = 0
    sum = 0
    for i in range(1, n + 1):
        x = a
        a = x + b
        b = x
        sum += x
    print("Сумма чисел = ", sum)
fun(N)
