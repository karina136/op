# -- coding: utf-8 --
s=input("Введите строку \n")
flag=0
w=0
string=""
for i in range (len(s)):
    if s[i] != ' ' and flag == 0:
        w += 1
        flag = 1
    else:
        if s[i] == ' ':
            flag = 0
print("Число слов в строке:", w)