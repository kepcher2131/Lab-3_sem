import numpy as np
from numpy import linalg

sz = int(input('Введите размерность квадратной матрицы больше 1 и меньше 31:'))
while (sz < 1) or (sz > 31):
    sz = int(input("\nВы ввели неверное число. \nВведите размерность квадратной матрицы больше 1 и меньше 31:"))
x = np.random.randint(5, size=(sz, sz))
r = np.linalg.matrix_rank(x)
print("Матрица:\n", x)
print("Ранг матрицы:", r)
t = int(input('\nВведите количество знаков после запятой в результате вычисления:'))
t = 0.1 ** t
n = 1
znam = 1
summa = 0
fg = 0
out = 1
print()
while abs(out) > t:
    fg += summa
    summa += (np.linalg.det(abs(x * znam))) / znam
    n += 1
    znam = np.math.factorial(n)
    out = abs(fg-summa)
    fg = 0
    print(n-1, ':', summa, ' ', out)
print('Сумма знакопеременного ряда:', summa)


