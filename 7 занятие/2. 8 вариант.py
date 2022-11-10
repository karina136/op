# -- coding: utf-8 --
n=int(input("Введите длину массива: "))
a=[]
for i in range (n):
    print("Введите", i, "элемент: ")
    a.append(float(input()))
print("Исходный массив: ", a)
b=sum(a)/len(a)
for i in range (n):
    if a[i] == 0:
        a[i]= b
print("Полученный массив: ", a)