# -- coding: utf-8 --
def zam (X):
    tmp=X[0]
    X[0]=X[len(X)-1]
    X[len(X)-1]=tmp
A=[]
m=int(input("Введите длину массива: "))
for i in range (m):
    print("Введите",i,"элемент массива")
    A.append(int(input()))
print("Исходный массив", A)
zam(A)
print("Полученный массив", A)