from ft_filter import ft_filter
import sys
import re


def is_even(x: int) -> bool:
    """is_even function returns true if parameter is even, false if odd"""
    return x % 2 == 0


def is_vowel(x: str) -> bool:
    """is_vowel function returns true if letter is vowel, false else"""
    if x in ["a", "e", "i", "o", "u", "y"]:
        return True
    return False


def is_string_normal(string: str) -> bool:
    """checks if the string contains only alphanumeric characters and spaces"""
    pattern = r'[^a-zA-Z0-9\s]'
    match = re.search(pattern, string)
    if match:
        return False
    else:
        return True


def check_length(string: str, size: int) -> bool:
    """checks if the string length is greater than size"""
    return len(string) > size


def main():
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    s: str = sys.argv[1]
    if not is_string_normal(s):
        raise AssertionError("the arguments are bad")
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    words = [word.strip() for word in s.split(" ")]
    filter_words = ft_filter(lambda x: check_length(x, n), words)
    print(filter_words)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{type(e).__name__}: {str(e)}")
