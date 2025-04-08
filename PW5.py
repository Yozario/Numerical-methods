#импорт библиотеки нампай
import numpy as np

#функция, пытающаяся привести матрицу к диагонально доминирующему виду
def make_diagonally_dominant(A, b):
    n = len(A)
    new_A = np.zeros_like(A)
    new_b = np.zeros_like(b)
    remaining_rows = set(range(n))

    for col in range(n):
        max_row = -1
        max_val = -np.inf
        for row in remaining_rows:
            if abs(A[row, col]) > max_val:
                max_val = abs(A[row, col])
                max_row = row

        if max_row == -1:
            raise ValueError("Матрица не может быть приведена к диагонально доминирующему виду")
        new_A[col] = A[max_row]
        new_b[col] = b[max_row]
        remaining_rows.remove(max_row)

    for i in range(n):
        row_sum = np.sum(np.abs(new_A[i])) - np.abs(new_A[i, i])
        if np.abs(new_A[i, i]) <= row_sum:
            print("Не удалось достичь строгого диагонального преобладания")

    return new_A, new_b

#метод простых итераций
def simpiter_method(A, b, max_iter=1000, e=1e-10, ensure_dominance=True):
    if ensure_dominance:
        A, b = make_diagonally_dominant(A, b)

    n = len(b)
    x = np.zeros(n)
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x) < e:
            return x_new, k+1
        x = x_new.copy()
    print("Достигнуто максимальное число итераций.")
    return x

#метод Зейделя
def seidel_method(A, b, e=1e-10, max_iter=1000, ensure_dominance=True):
    if ensure_dominance:
        A, b = make_diagonally_dominant(A, b)

    n = len(A)
    x = np.zeros(n)
    for iteration in range(max_iter):
        x_prev = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]
        if np.linalg.norm(x - x_prev) < e:
            return x, iteration + 1

    print(f"Достигнуто максимальное число итераций ({max_iter})")
    return x, max_iter


A = np.array([[2, 2, 10],
              [10, 1, 1],
              [2, 10, 1]])
b = np.array([14, 12, 13])

print("Исходная матрица:")
print(A)
print("Вектор b:", b)

x, iterations = simpiter_method(A, b)
print("\nРешение методом простых итераций:", x)
print("Количество итераций:", iterations)
print(f"Проверка Ax - b: {np.dot(A, x) - b}")

x, iterations = seidel_method(A, b)

print("\nРешение методом Зейделя:", x)
print("Количество итераций:", iterations)
print("Проверка: A*x =", np.dot(A, x))