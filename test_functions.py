import numpy as np


def rastrigin_func(xx, a=10):
    f = a * len(xx) + sum([np.power(x, 2) - a * np.cos(2 * np.pi * x) for x in xx])
    return f


def bukin_f6_func(x):
    if len(x) != 2:
        raise Exception
    f = 100 * np.sqrt(np.fabs(x[1] - 0.01 * np.power(x[0], 2))) + 0.01 * np.fabs(x[0] + 10)
    return f


def wolfe_func(x):
    if len(x) != 3:
        raise Exception
    f = 4 / 3 * np.power(np.power(x[0], 2) + np.power(x[1], 2) - x[0] * x[1], 0.75) + x[2]
    return f


def easom_func(x):
    if len(x) != 2:
        raise Exception
    f = - np.cos(x[0]) * np.cos(x[1]) * np.exp(- np.power(x[0] - np.pi, 2) - np.power(x[1] - np.pi, 2))
    return f


def michalewicz_func(xx, m=10):
    f = - sum([np.sin(x) * np.power(np.sin(len(xx) * np.power(x, 2) / np.pi), 2 * m) for x in xx])
    return f


