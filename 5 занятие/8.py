# -- coding: utf-8 --
last=int(input())
first=int(input())
a=1
b=1
while first != 0:
    if first==last:
        a += 1
    else:
        a=1
    if a>b:
        b=a
    last,first=first,int(input())
print("количество равных элементов идущих подряд: ", b)