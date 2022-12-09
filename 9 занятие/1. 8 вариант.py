# -- coding: utf-8 --
from random import randint
n=int(input("Введите порядок матрицы n= "))
print("Исходная матрица:")
A=[]
def fun(x,y):
    for i in range (x):
        B=[]
        for j in range(x):
            B.append(j)
        y.append(B)


    for i in range (x):
            for j in range(x):
                y[i][j]=randint(1,20)


    for i in range (x):
            for j in range(x):
                print(y[i][j], end=' ')
            print()
fun(n,A)

k=int(input("Введите число k="))
for n in range(0, len(A)):
    x=A[k][n] / A[k][k]
    print(A[k][n],'/',A[k][k], '=', x )