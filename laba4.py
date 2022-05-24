import random
import time
import os

def print_matrix(M):
    for i in M:
        for j in i:
            print("%3d" % j, end=' ')
        print()
    print()

def submatrix(M):
    for i in range(size):
        M.append([0] * size)

try:
    K = int(input("Введите число К="))
    row_q = int(input("Введите чётное количество строк (столбцов) квадратной матрицы >5:"))
    while row_q < 5 or row_q % 2 != 0:
        row_q = int(input("Введите чётное!!! количество строк (столбцов) квадратной матрицы >5!!!:"))

    start = time.time()
    print("\n-----Результат работы программы-----\n -----Локальное время", time.ctime(), "-----")

    A, F, AF, AT, S = [], [], [], [], []  # Задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)
        S.append([0] * row_q)

    for i in range(row_q):
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    print("A")
    print_matrix(A)

    for i in range(row_q):
        for j in range(row_q):
            F[i][j] = A[i][j]

    C = []  # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):  # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size + row_q % 2 + i][size + row_q % 2 + j]
    print("C")
    print_matrix(C)

    kolv = 0
    poloj = 0
    for i in range(size):  # обработка матрицы C
        for j in range(size):
            if C[i][j] > 0 and i < j and i > size - j - 1 and i % 2 == 1:   #2
                poloj += 1
            elif C[i][j] < 0 and j % 2 == 0 and i > j and i > size - j -1:  #4
                kolv += 1

    print("кол-во положительных = ", poloj)
    print("кол-во отрицательных чисел = ", kolv)

    if poloj > kolv:
        print("меняем в С симметрично области 1 и 3 местами")
        for i in range(size + row_q % 2 + 1, row_q, 1):
            for j in range(size + row_q % 2 + 1, row_q, 1):
                if (i - size - row_q % 2) > (j - size - row_q % 2) and (i - size - row_q % 2) > size - (j - size - row_q % 2) - 1:
                    buffer = F[i][j]
                    F[i][j] = F[size - i - 1][j]
                    F[size - i - 1][j] = buffer
    else:
        print("меняем С и Е местами")
        for j in range(row_q // 2):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j] = F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j], F[i][j]
    print("\nИзмененная F")
    print_matrix(F)

    #(F + A) * AT – K * F
    for i in range(row_q):  # F + A
        for j in range(row_q):
            S[i][j] = F[i][j] + A[i][j]
    print("F + A")
    print_matrix(S)

    for i in range(row_q):  # AT
        for j in range(row_q):
            AT[i][j] = A[j][i]
    print("AT")
    print_matrix(AT)

    for i in range(row_q):
        for j in range(row_q):
            S[i][j] = S[i][j] * AT[i][j]
    print("(F + A) * AT")
    print_matrix(S)

    for i in range(row_q):  # K * F
        for j in range(row_q):
            F[i][j] = K * F[i][j]
    print("K * F")
    print_matrix(F)

    for i in range(row_q):
        for j in range(row_q):
            F[i][j] = S[i][j] - F[i][j]
    print("(F + A) * AT – K * F")
    print_matrix(F)

    finish = time.time()
    result = finish - start
    print("\nProgram time: " + str(result) + " seconds.")
    print("Program size: " + str(os.path.getsize('laba4.py')) + " bytes.")

except ValueError:
    print("\nВведенн(ый/ые) символ(/ы) не явля(ется/ются) числом")

except FileNotFoundError:
    print("\nФайл для определения размера не найден")