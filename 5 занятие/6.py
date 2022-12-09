# -- coding: utf-8 --
n=int(input())
def fun(C):
    i=0
    summa=0
    while C !=0:
        i += 1
        summa += C
        C=int(input())
    print("Среднее значение элементов последовательности: ",summa/i)
fun(n)