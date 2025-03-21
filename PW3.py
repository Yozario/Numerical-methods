def func(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def nextx(x0, x1, a):
    funca = func(x0, a)
    res = x0 - ((x1 - x0)*funca/(func(x1, a) - funca)) * c
    return res


def Secant(x0, x1, e):
    for i in range(max_iter):
        f_x0 = func(x0, a)
        f_x1 = func(x1, a)
        x_n = x0 - f_x0 * (x1 - x0) / (f_x1 - f_x0)
        if func(x0, a) * func(x_n, a) < 0:
            x1 = x_n
        elif func(x_n, a) * func(x1, a) < 0:
            x0 = x_n
        elif func(x0, a) * func(x_n, a) == 0:
            return x_n
    return x_n

a = [1, -1, 0, 1]
x0 = -2
x1 = 1
e = 0.000000001
c = 0.7
max_iter = 10000
ans = Secant(x0, x1, e)
print('x через хорды:', ans)
print(f'При x = {ans}, y = {func(ans, a):.20f}')
print()


def R(fx):
    if fx[0] <= 0:
        return 'a0 должно быть > 0'
    temp = []
    flag = False
    for i in range(len(fx)):
        if fx[i] < 0 and flag==False:
            k = i
            flag = True
        elif fx[i] < 0:
            temp.append(-1 * fx[i])
    temp.append(-1*fx[k])
    temp.sort()
    return 1 + (temp[-1]/fx[0])**(1/k)

def R1(fx):
    fxn = fx[::-1]
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag==False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1*fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


def R2(fx):
    fxn = fx
    if len(fxn) % 2 == 0: t = 0
    else: t = 1
    for i in range(t, len(fxn), 2):
        fxn[i] *= (-1)
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag == False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1 * fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


def R3(fx):
    fxn = fx[::-1]
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag == False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1 * fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


fxs = [1, 2, -5, 8, -7, -3]
#print(R(fxs))
print(f'{1/R1(fxs)} <= x-полож <= {R(fxs)}')
print(f'{-1*R2(fxs)} <= x-отриц <= {-1/R3(fxs)}')