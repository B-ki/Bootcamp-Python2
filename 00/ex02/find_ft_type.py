def all_thing_is_obj(object: any) -> int:
    # Get the type of the object
    obj_type = type(object).__name__

    # Map the object type to the desired output format
    if obj_type == "list":
        print(f"List : ", end="")
        print(type(object))
    elif obj_type == "tuple":
        print(f"Tuple : ", end="")
        print(type(object))
    elif obj_type == "set":
        print(f"Set : ", end="")
        print(type(object))
    elif obj_type == "dict":
        print(f"Dict : ", end="")
        print(type(object))
    elif obj_type == "str":
        print(f"{object} : ", end="")
        print(type(object))
    else:
        print("Type not found")
    return 42

def main():
    """Printing objects types"""
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    print(all_thing_is_obj(10))

if __name__ == "__main__":
    main()
