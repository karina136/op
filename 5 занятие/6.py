# -- coding: utf-8 --
n=int(input())
i=0
summa=0
while n !=0:
    i += 1
    summa += n
    n=int(input())
print("Среднее значение элементов последовательности: ",summa/i)