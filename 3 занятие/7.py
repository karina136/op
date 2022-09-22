# -- coding: utf-8 --
n=int(input("Номер года: "))
def add(n):
    return((n%4==0 and n%100 !=0) or  n%400==0)
if add(n):
    print("Да")
else:
    print("Нет")