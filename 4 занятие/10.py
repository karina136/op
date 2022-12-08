# -- coding: utf-8 --
N = int(input("Введите колличество чисел: "))
K = int(input("Введите порядковый номер числа: "))
def fun(A,B):
  x = 0
  y = 1
  c = A+B
  for i in range (1, c+1):
    z = x + y
    x = y
    y = z
  print(z)
fun(N,K)