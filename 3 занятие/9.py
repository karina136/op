# -- coding: utf-8 --
n=int(input("ширина шоколадки: "))
m=int(input("Длина шоколадки: "))
k=int(input("Кол-во долек отломленной части: "))
def add(n,m,k):
    return((k%n==0 and k//n<m) or (k%m==0 and k//m<n))
if (add(n,m,k)):
    print("Да")
else:
    print("Нет")
