import numpy as np
import math as math


def mean(x):
    '''mean'''
    return np.sum(x) / len(x)


def median(x):
    '''median'''
    x.sort()
    if len(x) % 2:
        return x[int(len(x)/2)]
    else:
        return x[int(len(x)/2 - 1)]


def quartile_rank(i_inf, x):
    '''quartile i_inf'''
    x.sort()
    if i_inf == int(i_inf):
        return x[int(i_inf)]
    elif (i_inf * 10) % 10 == 2:
        return (x[int(i_inf)] * 3 + x[int(i_inf) + 1]) / 4
    elif (i_inf * 10) % 10 == 5:
        return (x[int(i_inf)] + x[int(i_inf) + 1]) / 2
    else:
        return (x[int(i_inf)] * 3 + x[int(i_inf) + 1]) / 4


def quartile(x):
    '''quartile'''
    i_f1 = (len(x) + 3)/4
    i_f3 = int(len(x) * 3 + 1) / 4
    return [quartile_rank(i_f1 - 1, x), quartile_rank(i_f3 - 1, x)]


def var(x):
    '''var'''
    m = mean(x)
    x_cpy = list(np.multiply(x, x))
    return np.sum(x_cpy)/len(x) - m * m


def std(x):
    '''std'''
    return math.sqrt(var(x))


def ft_statistics(*args, **kwargs) -> None:
    '''ft_statistics'''
    array = []
    for arg in args:
        assert isinstance(arg, (int, float)), "args must be float or int"
        array.append(arg)
    for key, value in kwargs.items():
        array = np.array(args)
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            print(f'mean : {mean(array)}')
        elif value == "median":
            print(f'median : {median(array)}')
        elif value == "quartile":
            print(f'quartile : {quartile(array)}')
        elif value == "std":
            print(f'std : {std(array)}')
        elif value == "var":
            print(f'var : {var(array)}')
