# -- coding: utf-8 --
from random import randint
n=int(input("Введите порядок матрицы n= "))
print("Исходная матрица:")
A=[]
for i in range (n):
    B=[]
    for j in range(n):
        B.append(j)
    A.append(B)


for i in range (n):
        for j in range(n):
            A[i][j]=randint(1,20)


for i in range (n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()


k=int(input("Введите число k="))
for n in range(0, len(A)):
    x=A[k][n] / A[k][k]
    print(A[k][n],'/',A[k][k], '=', x )