# -- coding: utf-8 --
def S (chislo):
    for index in str(chislo):
        if index=="0" or chislo%int(index):
            return False
    return True
n=int(input("Введите натуральное число: "))
for i in range (1,n+1):
    if S (i):
        print(i)