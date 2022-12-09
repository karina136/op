# -- coding: utf-8 --
s=input("Введите строку \n")
def fun(x):
    flag=0
    w=0
    string=""
    for i in range (len(x)):
        if x[i] != ' ' and flag == 0:
            w += 1
            flag = 1
        else:
            if x[i] == ' ':
                flag = 0
    print("Число слов в строке:", w)
fun(s)