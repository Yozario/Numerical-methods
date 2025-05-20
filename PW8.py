from sympy import symbols, expand

#Задание 1
def lagrange_polynomial(x_values, y_values):
    x = symbols('x')
    n = len(x_values)
    polynomial = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term

    return expand(polynomial)


x_values = [2, 3, 4, 5]
y_values = [7, 5, 8, 7]
x = 2.5

polynomial = lagrange_polynomial(x_values, y_values)

print("Задание 1.")
print("Многочлен Лагранжа:")
print(polynomial)

print(f"Значение многочлена Лагранжа в точке x = {x}: {polynomial.subs('x', x)}")

#Задание 2
def piecewise_lagrange_interpolation(x_values, y_values, x, window_size=2):
    n = len(x_values)

    # Находим индекс начала окна, содержащего x
    start_idx = 0
    for i in range(n - window_size + 1):
        if x_values[i] <= x <= x_values[i + window_size - 1]:
            start_idx = i
            break
    else:
        # Если x вне диапазона, используем последнее возможное окно
        start_idx = max(0, n - window_size)

    # Выбираем подмножество точек для окна
    window_x = x_values[start_idx:start_idx + window_size]
    window_y = y_values[start_idx:start_idx + window_size]

    return lagrange_interpolation(window_x, window_y, x)


def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


k = 2
print("\nЗадание 2.")
res = piecewise_lagrange_interpolation(x_values, y_values, x, window_size=k)
print(f"Интерполяция в x = {x} с окном k = {k}: {res}")


def newton_polynomial(x_values, y_values):
    x = symbols('x')
    n = len(x_values)

    div_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        div_diff[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x_values[i + j] - x_values[i])

    polynomial = div_diff[0][0]
    for j in range(1, n):
        term = div_diff[0][j]
        for k in range(j):
            term *= (x - x_values[k])
        polynomial += term

    return expand(polynomial)


print(f"\nЗадание 3.")
polynomial = newton_polynomial(x_values, y_values)
print("\nМногочлен Ньютона:")
print(polynomial)

print(f"\nЗначение многочлена Ньютона в точке x = {x}: {polynomial.subs('x', x)}")

print("\nТаблица разделенных разностей:")
n = len(x_values)
div_diff = [[0] * n for _ in range(n)]
for i in range(n):
    div_diff[i][0] = y_values[i]

for j in range(1, n):
    for i in range(n - j):
        div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x_values[i + j] - x_values[i])

for row in div_diff:
    print(row)


def piecewise_newton_interpolation(x_values, y_values, x, window_size=2):
    n = len(x_values)

    # Находим индекс начала окна, содержащего x
    start_idx = 0
    for i in range(n - window_size + 1):
        if x_values[i] <= x <= x_values[i + window_size - 1]:
            start_idx = i
            break
    else:
        # Если x вне диапазона, используем последнее возможное окно
        start_idx = max(0, n - window_size)

    # Выбираем подмножество точек для окна
    window_x = x_values[start_idx:start_idx + window_size]
    window_y = y_values[start_idx:start_idx + window_size]

    return newton_interpolation(window_x, window_y, x)


def newton_interpolation(x_values, y_values, x):
    n = len(x_values)

    div_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        div_diff[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x_values[i + j] - x_values[i])

    result = div_diff[0][0]
    for j in range(1, n):
        term = div_diff[0][j]
        for k in range(j):
            term *= (x - x_values[k])
        result += term

    return result


k = 3
print("\nЗадание 4.")
res = piecewise_newton_interpolation(x_values, y_values, x, window_size=k)
print(f"Интерполяция Ньютона в x = {x} с окном k = {k}: {res}")