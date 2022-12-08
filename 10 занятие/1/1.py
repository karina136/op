# -- coding: utf-8 --
from random import randint
def mat_with_operation(n,k):
    A=[]
    result = list()
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
    for n in range(0, len(A)):
        x=A[k][n] / A[k][k]
        result.append(x)
        print(A[k][n],'/',A[k][k], '=', x )
    return result

def write_in_file(l):
    with open("C:\\Users\\penki\\Documents\\GitHub\\op\\10 занятие\\1\\Пенкина Карина Константиновна_223_vivod.txt", "w") as f:
        for item in l:
            f.write("%s\n" % item)

a=int(input("Введите порядок матрицы n= "))
b=int(input("Введите число k="))

res = mat_with_operation(a,b)
print(res)
write_in_file(res)#запись в файл результатов выполнения программы 




