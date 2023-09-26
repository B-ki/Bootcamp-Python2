def square(x: int | float) -> int | float:
    '''square'''
    assert isinstance(x, (int, float)), "x must be int or float"
    return x * x


def pow(x: int | float) -> int | float:
    '''pow'''
    assert isinstance(x, (int, float)), "x must be int or float"
    return x ** x


def outer(x: int | float, function) -> object:
    '''outer'''
    assert isinstance(x, (int, float)), "x must be int or float"
    count = 0

    def inner() -> float:
        '''inner'''
        nonlocal x, count
        x = function(x)
        count += 1
        return x

    return inner
