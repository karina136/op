# -- coding: utf-8 --
N=int(input("Введите натуральное число N = "))
i = 1
l = 0
def fun(a,b,c):
    while (b*2) <= a:
        b *= 2
        c += 1
    print("Показатель степени = ",c,"Наибольшая степень = ", b)
fun(N,i,l)