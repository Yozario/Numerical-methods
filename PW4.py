def Gauss1(a):
    for i in range(0, len(a)-1):
        t = a[i][i]
        for g in range(len(a[0])):
            a[i][g] /= t
        for k in range(i, len(a)-1):
            t2 = a[k+1][i]
            for j in range(len(a)):
                a[k+1][j] -= a[i][j]*t2
    a.remove([0, 0, 0, 0])
    x3 = a[2][3]/a[2][2]
    x2 = (a[1][3] - a[1][2] * x3)/a[1][1]
    x1 = (a[0][3] - a[0][2] * x3 - a[0][1] * x2)/a[0][0]
    print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}')


def Gauss3(a):
    b = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    t = a[0][0]
    for g in range(len(a[0])):
        b[0][g] = a[0][g] / t
    for k in range(1, len(a)):
        for i in range(1-1+k, len(a)):
            for g in range(1-1+k, len(a[0])):
                if g == 0:
                    b[i][g] = 0
                if k == 2:
                    b[i][g] = b[i][g] - (b[i][0-1+k] * b[0-1+k][g]) / b[0-1+k][0-1+k]
                else:
                   b[i][g] = a[i][g] - (a[i][0-1+k] * a[0-1+k][g]) / a[0-1+k][0-1+k]
            t = b[i][k]
            if k != 2 and i < len(a)-1:
                for j in range(len(b[i])):
                    b[i][j]/=t
    x3 = b[2][3] / b[2][2]
    x2 = (b[1][3] - b[1][2] * x3) / b[1][1]
    x1 = (b[0][3] - b[0][2] * x3 - b[0][1] * x2) / b[0][0]
    print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}')


mat = [[5, 0, 1, 11],
      [2, 6, -2, 8],
      [-3, 2, 10, 6],
      [0, 0, 0, 0]]#массив нулей добавлен для корректной работы кода

mat2 = [[2, 1, 4, 16],
        [3, 2, 1, 10],
        [1, 3, 3, 16]]
Gauss1(mat)
Gauss3(mat2)

import numpy as np


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for k in range(i, n):
            sum_ = 0
            for j in range(i):
                sum_ += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum_
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum_ = 0
                for j in range(i):
                    sum_ += L[k][j] * U[j][i]
                L[k][i] = (A[k][i] - sum_) / U[i][i]
    return L, U


def solve_lu(A, b):
    L, U = lu_decomposition(A)
    n = len(A)
    y = np.zeros(n)
    for i in range(n):
        sum_ = 0
        for j in range(i):
            sum_ += L[i][j] * y[j]
        y[i] = b[i] - sum_
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ = 0
        for j in range(i + 1, n):
            sum_ += U[i][j] * x[j]
        x[i] = (y[i] - sum_) / U[i][i]

    return [x[0], x[1], x[2]]


A = np.array([
    [2, 1, 4],
    [3, 2, 1],
    [1, 3, 3]])

b = np.array([16, 10, 16])

x = solve_lu(A, b)
res = ""
for xi in range(len(x)):
    res +="x"+ str(xi) + " = " + str(x[xi])+", "
print(res)
