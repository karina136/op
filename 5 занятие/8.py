# -- coding: utf-8 --
last=int(input())
first=int(input())
def fun(x,y):
    a=1
    b=1
    while y != 0:
        if y==x:
            a += 1
        else:
            a=1
        if a>b:
            b=a
        x,y=y,int(input())
    print("количество равных элементов идущих подряд: ", b)
fun(last,first)