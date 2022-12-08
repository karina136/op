# -- coding: utf-8 --
from random import randint
def matrix(N,A):
    print("Начальная матрица:")
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=' ')
        print()

def trance(A):
    B=[[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            B[j][i]=A[i][j]
    return B

def matrix_T(N,x):
    #Транспонированная матрица
    mat = []
    for j in range(N):
        for i in range(N):
            mat.append(x[j][i])
    return mat

def write_in_file(l):
    with open("C:\\Users\\penki\\Documents\\GitHub\\op\\10 занятие\\2\\Пенкина Карина Константиновна_223_vivod.txt", "w") as f:
        for item in l:
            f.write("%s" % item)


N = int(input("Введите размер матрицы: "))
A=[[randint(1,9)for i in range(N)]for j in range(N)]

matrix(N,A)
x=trance(A)
Tmatrix = matrix_T(N,x)
print("Запись транспонированной матрицы в файл...")
write_in_file(Tmatrix)
print("Успешно!")



