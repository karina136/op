# -- coding: utf-8 --
n = int(input("Введите число: "))
def fun(x):
    if x<=9:
        for i in range(1, x + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()
fun(n)
    