import numpy as np
from numpy import linalg

sz = int(input('Введите размерность квадратной матрицы больше 1 и меньше 31:'))
while (sz < 1) or (sz > 31):
    sz = int(input("\nВы ввели неверное число. \nВведите размерность квадратной матрицы больше 1 и меньше 31:"))

x = np.random.randint(5, size=(sz, sz))
rank = np.linalg.matrix_rank(x)
print("Матрица:\n", x)
print("Ранг матрицы:", rank)

t = int(input('\nВведите количество знаков после запятой в результате вычисления:'))

n, fact, znam, out = 1, 1, 1, 1
summa, fg = 0, 0
print(t ,' ',np.linalg.det(x))
while abs(out) > pow(0.1, t):
    fg += summa
    fact = n
    summa += (np.linalg.det(abs(x * fact))) / znam
    n += 1
    znam *= (n-1) * n
    out = abs(fg-summa)
    fg = 0
    print(n-1, ':', summa, ' ', out)

print("Сумма знакопеременного ряда: ",summa)

