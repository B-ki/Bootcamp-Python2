def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None ", end="")
        print(type(object))
        return 0
    elif isinstance(object, float) and str(object).lower() == "nan":
        print(f"Cheese : {object} ", end="")
        print(type(object))
        return 0
    elif object == 0:
        print(f"Zero : {object} ", end="")
        print(type(object))
        return 0
    elif object == "":
        print("Empty : ", end="")
        print(type(object))
        return 0
    elif object is False:
        print(f"Fake : {object} ", end="")
        print(type(object))
        return 0
    else:
        print("Type not Found")
        return 1
