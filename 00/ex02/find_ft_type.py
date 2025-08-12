def all_thing_is_obj(object: any) -> int:
    '''Function to print the type of the object passed as argument.'''
    obj_type = type(object).__name__

    if obj_type == "list":
        print("List : ", end="")
        print(type(object))
    elif obj_type == "tuple":
        print("Tuple : ", end="")
        print(type(object))
    elif obj_type == "set":
        print("Set : ", end="")
        print(type(object))
    elif obj_type == "dict":
        print("Dict : ", end="")
        print(type(object))
    elif obj_type == "str":
        print("Brian is in the kitchen : ", end="")
        print(type(object))
    else:
        print("Type not found")
    return 42
