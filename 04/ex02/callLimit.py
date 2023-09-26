from functools import wraps


def callLimit(limit: int):
    '''callLimit'''
    assert isinstance(limit, int), "limit must be an int"
    assert limit >= 0, "limit must be >= 0"
    count = 0

    def callLimiter(function):
        # function refers to the original function used with the decorator
        nonlocal limit, count
        '''callLimiter'''
        @wraps(function)
        def limit_function(*args, **kwds):
            nonlocal limit, count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called too many times")

        return limit_function

    return callLimiter
