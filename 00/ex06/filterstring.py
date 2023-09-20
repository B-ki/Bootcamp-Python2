from ft_filter import ft_filter
import sys
import re


def is_even(x):
    """is_even function returns true if parameter is even, false if odd"""
    return x % 2 == 0


def is_vowel(x):
    """is_vowel function returns true if letter is vowel, false else"""
    if x in ["a", "e", "i", "o", "u", "y"]:
        return True
    return False


def is_string_normal(string):
    pattern = r'[^a-zA-Z0-9\s]'
    match = re.search(pattern, string)
    if match:
        return False
    else:
        return True


def main():
    print("\n#########   ARGUMENTS - filterstring  #########\n")
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    words = s.split(" ")
    if not is_string_normal(s):
        raise AssertionError("the arguments are bad")
    check_length = lambda string, size: len(string) > size
    print([word for word in words if check_length(word, n)])

    print("\n\n#########   TESTS - ft_filter   #########\n")
    print(filter.__doc__)
    numbers = {1, 2, 3, 4, 5}
    print(f"\nArguments : {numbers}, and function : {is_even.__doc__}")
    filter_numbers = ft_filter(is_even, numbers)
    print(f"Result : {filter_numbers}")
    letters = ("a", "b", "c", "d", "e", "f", "i", "o", "p", "q", "r", "s", "u")
    print(f"\nArguments : {letters}, and function : {is_vowel.__doc__}")
    filter_letters = ft_filter(is_vowel, letters)
    print(f"Result : {filter_letters}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{type(e).__name__}: {str(e)}")
