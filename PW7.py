import numpy as np


def jacobi_eigen(A, eps=1e-10, max_iter=100):
    n = A.shape[0]

    # Проверяем на симметричность:
    if not np.allclose(A, A.T):
        print(ValueError("Матрица должна быть симметричной"))
        return -1

    # Матрица собственных векторов:
    V = np.eye(n)

    for _ in range(max_iter):

        # Максимальный по модулю недиагональный элемент:
        max_val = 0
        p, q = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j

        # Проверяем на достижение точности
        if max_val < eps:
            break

        # Вычисляем угол поворота
        if A[p, p] == A[q, q]:
            phi = np.pi / 4
        else:
            phi = 0.5 * np.arctan(2 * A[p, q] / (A[p, p] - A[q, q]))

        # Формируем матрицу вращения
        H = np.eye(n)
        c = np.cos(phi)
        s = np.sin(phi)
        H[p, p] = c
        H[q, q] = c
        H[p, q] = -s
        H[q, p] = s

        # Матричное перемножение
        A = H.T @ A @ H

        V = V @ H

    # Собственные значения - диагональные элементы
    eigenvalues = np.diag(A)
    # Собственные векторы - столбцы матрицы V
    eigenvectors = V

    return eigenvalues, eigenvectors

# Проверяем работу
A = np.array([[5, 1, 2],
              [1, 4, 1],
              [2, 1, 3]])

print("Исходная матрица:")
print(A)

eigenvalues, eigenvectors = jacobi_eigen(A)

print("\nСобственные значения:")
print(eigenvalues)

print("\nСобственные векторы (в столбцах):")
print(eigenvectors)