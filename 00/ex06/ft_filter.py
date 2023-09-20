def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if not callable(function):
        raise TypeError("function must be callable")
    if not iter(iterable):
        raise TypeError("iterable must be iterable")
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    return result
