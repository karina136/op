# -- coding: utf-8 --
from random import randint
print("Исходный массив: ")
N=4
A=[[randint(1,9)for i in range(N)]for j in range(N)]

for i in range(N):
    for j in range(N):
        print(A[i][j], end=' ')
    print()

print("Транспонированный массив:")
def trance(A):
    B=[[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            B[j][i]=A[i][j]
    return B

x=trance(A)
for j in range(N):
    for i in range(N):
        print(x[j][i], end=" ")
    print()
