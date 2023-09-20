def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """give_bmi function"""
    assert isinstance(height, list) and isinstance(weight, list), "height and\
             weight are not list"
    assert all([isinstance(i, (int, float)) for i in height + weight]), "heigh\
            t and weight are not list of int or float"
    assert len(height) == len(weight), "height and weight are not list of same\
             size"
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit function"""
    assert isinstance(bmi, list), "bmi is not list"
    assert all([isinstance(item, (int, float)) for item in bmi]), "bmi is not \
            list of int or float"
    assert isinstance(limit, int), "limit is not an int"
    return [value > limit for value in bmi]
