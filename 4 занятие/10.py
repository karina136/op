# -- coding: utf-8 --
N = int(input("Введите колличество чисел: "))
K = int(input("Введите порядковый номер числа: "))
x = 0
y = 1
c = K+N
for i in range (1, c+1):
  z = x + y
  x = y
  y = z
print(z)