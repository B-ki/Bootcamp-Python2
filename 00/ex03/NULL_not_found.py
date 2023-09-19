def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing : ", end="")
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
        print(f"Empty : ", end="")
        print(type(object))
        return 0
    elif object is False:
        print(f"Fake : {object} ", end="")
        print(type(object))
        return 0
    else:
        print("Type not Found")
        return 1

def main():
    """Printing objects types"""
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))

if __name__ == "__main__":
    main()
