# -- coding: utf-8 --
n=int(input("Введите длину массива: "))
a=[]
def fun(x,y):
    for i in range (x):
        print("Введите", i, "элемент: ")
        y.append(float(input()))
    print("Исходный массив: ", y)
    b=sum(y)/len(y)
    for i in range (x):
        if y[i] == 0:
            y[i]= b
    print("Полученный массив: ", y)
fun(n,a)