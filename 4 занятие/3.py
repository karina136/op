# -- coding: utf-8 --
A=int(input("A= "))
B=int(input("B= "))
for i in range(A,B-1,-1):
    if i%2 != 0:
        print(i, end= ";")
