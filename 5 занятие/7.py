# -- coding: utf-8 --
a=int(input())
b=int(input())
def fun(x,y):
    i=0
    while x !=0 and y !=0:
        if y>x:
            i += 1
            x=y
        else:
            x=y
        y=int(input())
    print("Количество элементов больше предыдущего: ",i)
fun(a,b)