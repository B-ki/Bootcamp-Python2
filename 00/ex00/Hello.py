def main():
    """Learning differences from data structures : list, tuple, set and
    dictionnaires"""
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # List are mutable -> We can change their elements
    ft_list[-1] = "World!"
    # Tuples are immutable. We need to create a new tuple
    ft_tuple = ft_tuple[:-1] + ("France",)
    # Sets are mutable, but we can't access elements by index
    # Upon printing they might appear in different order because of the nature
    # of set
    ft_set.remove("tutu!")
    ft_set.add("Paris")
    # Dictionnaires are mutable, we can use keys to change values
    ft_dict["Hello"] = "42Paris"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
