def deriv(a):
    b = []
    for i in range(1, len(a)):
        b.append(a[i] * i)
    return b



def func(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def nextx(x0):
    return x0 - func(x0, a)/func(x0, deriv(a))


def simple_nextx(xc, x0):
    return xc - func(xc, a)/func(x0, deriv(a))


#
def bin(x1, x2, e):
    if func(x1, a) * func(x2, a) < 0:
        while abs(x1 - x2) > e:
            x_n = (x1 + x2) / 2
            if func(x1, a) * func(x_n, a) < 0:
                x2 = x_n
            elif func(x_n, a) * func(x2, a) < 0:
                x1 = x_n

            elif func(x1, a) * func(x_n, a) == 0:
                return x_n

        return (x1+x2) / 2

    else:
        x1 -= 50
        x2 += 50


def Newton(x0, e):
    s = (nextx(x0) - x0) / (1 - (nextx(x0) - x0) / (x0 - nextx(x0)))
    while abs(s) > e:
        s = (nextx(x0) - x0)/(1 - (nextx(x0) - x0)/(x0 - nextx(x0)))
        x0 = nextx(x0)
    return x0


def simple_Newton(xc, e):
    s = (nextx(xc) - xc) / (1 - (nextx(xc) - xc) / (xc - nextx(xc)))
    while abs(s) > e:
        s = (nextx(xc) - xc)/(1 - (nextx(xc) - xc)/(xc - nextx(xc)))
        xc = simple_nextx(xc, x0)
    return xc


a = [6, -5, 1]
x0 = 8
x1, x2 = 2.5, 4
e = 0.000000001
print(bin(x1, x2, e))
print(Newton(x0, e))
print(simple_Newton(x0, e))

