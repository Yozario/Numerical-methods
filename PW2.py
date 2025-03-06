def deriv(a):
    b = []
    for i in range(1, len(a)):
        b.append(a[i] * i)
    return b


def g(x0):
    return (x0**2 + 6) / 5


def func(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def nextx(x0):
    return x0 - func(x0, a) / func(x0, deriv(a)) * c


def Newton_Briden(x0, e):
    i = 0
    while i < 10000:
        s = (nextx(x0) - x0)/(1 - (nextx(x0) - x0) / (x0 - nextx(x0)))
        if abs(s) < e:
            print(f"Корень найден: {x0}, количество итераций: {i}")
            return x0
        i += 1
        x0 = nextx(x0)
    raise ValueError("Достигнуто максимальное количество итераций. Корень не найден.")


def Secant(x0, x1, e):
    for i in range(max_iter):
        f_x0 = func(x0, a)
        f_x1 = func(x1, a)
        if abs(f_x1) < e:
            print(f"Корень найден: {x1}, количество итераций: {i}")
            return x1
        x_n = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_n
    raise ValueError("Достигнуто максимальное количество итераций. Корень не найден.")

def Iter(x0, e, max_iter):
    for i in range(max_iter):
        x_n = g(x0)
        if abs(x_n - x0) < e:
            print(f"Корень найден: {x_n}, количество итераций: {i}")
            return x_n
        x0 = x_n
    raise ValueError("Достигнуто максимальное количество итераций. Корень не найден.")


a = [6, -5, 1]
x0 = 1
x1 = 1.25
e = 0.000000001
c = 0.7
max_iter = 1000
print(Newton_Briden(x0, e))
print(Secant(x0, x1, e))
print(Iter(x0, e, max_iter))