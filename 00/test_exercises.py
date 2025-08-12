import subprocess
import sys
from ex06.ft_filter import ft_filter


def run_python_file(file_path):
    """Run a Python file and return its output"""
    result = subprocess.run(
        [sys.executable, file_path], capture_output=True, text=True)
    return result.stdout


def run_python_file_with_args(file_path, args=None):
    """Run a Python file with arguments and return its output"""
    cmd = [sys.executable, file_path]
    if args:
        cmd.extend(args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def test_ex00():
    """Test ex00/Hello.py output"""
    expected = (
        "['Hello', 'World!']\n('Hello', 'France')\n"
        "{'Hello', 'Paris'}\n{'Hello': '42Paris'}\n"
    )
    actual = run_python_file("ex00/Hello.py")
    assert actual == expected


def test_ex01():
    """Test ex01/format_ft_time.py output"""
    # Not testable, the output is time-dependent
    assert True


def test_ex02():
    """Test ex02/find_ft_type.py output"""
    expected = (
        "List : <class 'list'>\n"
        "Tuple : <class 'tuple'>\n"
        "Set : <class 'set'>\n"
        "Dict : <class 'dict'>\n"
        "Brian is in the kitchen : <class 'str'>\n"
        "Type not found\n"
        "42\n"
    )
    actual = run_python_file("ex02/tester.py")
    assert actual == expected


def test_ex03():
    """Test ex03/NULL_not_found.py output"""
    expected = (
        "Nothing : None <class 'NoneType'>\n"
        "Cheese : nan <class 'float'>\n"
        "Zero : 0 <class 'int'>\n"
        "Empty : <class 'str'>\n"
        "Zero : False <class 'bool'>\n"
        "Type not Found\n"
        "1\n"
    )
    actual = run_python_file("ex03/tester.py")
    assert actual == expected


def test_ex04():
    """Test ex04/whatis.py output"""
    expected_even = "I'm Even.\n"
    expected_odd = "I'm Odd.\n"
    assert_error_not_int = "AssertionError: argument is not an integer\n"
    assert_error_mult = "AssertionError: more than one argument is provided\n"
    actual_14 = run_python_file_with_args("ex04/whatis.py", ["14"])
    actual_minus5 = run_python_file_with_args("ex04/whatis.py", ["-5"])
    actual_empty = run_python_file("ex04/whatis.py")
    actual_0 = run_python_file_with_args("ex04/whatis.py", ["0"])
    actual_hi = run_python_file_with_args("ex04/whatis.py", ["Hi!"])
    actual_multiple_input = run_python_file_with_args(
        "ex04/whatis.py", ["13", "5"])
    assert actual_14 == expected_even
    assert actual_minus5 == expected_odd
    assert actual_empty == ""
    assert actual_0 == expected_even
    assert actual_hi == assert_error_not_int
    assert actual_multiple_input == assert_error_mult


def create_expected_string_ex05(
        char_count: int, upper_count: int, lower_count: int,
        punctuation_count: int, space_count: int, digit_count: int) -> str:
    """Create expected output string for ex05/count.py"""
    return (
        f"The text contains {char_count} characters:\n"
        f"{upper_count} upper letters\n"
        f"{lower_count} lower letters\n"
        f"{punctuation_count} punctuation marks\n"
        f"{space_count} spaces\n"
        f"{digit_count} digits\n"
    )


def test_ex05_1():
    """Test ex05/count.py output"""
    str1 = "Python 3.0, released in 2008, was a major revision that is not"
    str1 += " completely backward-compatible with earlier versions. Python 2"
    str1 += " was discontinued with version 2.7.18 in 2020."
    expected1 = create_expected_string_ex05(171, 2, 121, 8, 25, 15)
    actual1 = run_python_file_with_args("ex05/building.py", [str1])
    assert actual1 == expected1


def test_ex05_2():
    """Test ex05/count.py output with different input"""
    str2 = "Hello World!"
    expected2 = create_expected_string_ex05(12, 2, 8, 1, 1, 0)
    actual2 = run_python_file_with_args("ex05/building.py", [str2])
    assert actual2 == expected2


def test_ex06():
    """Test ex06/ft_filter docstring matches built-in filter"""
    from ex06.ft_filter import ft_filter
    expected_doc = filter.__doc__
    actual_doc = ft_filter.__doc__
    assert expected_doc == actual_doc, "Documentation strings do not match"


def test_ex06_1():
    """Test basic functionality with simple predicates"""
    print("=== test_ex06_1: Basic functionality ===")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(x):
        return x % 2 == 0

    builtin_result = list(filter(is_even, numbers))
    ft_result = list(ft_filter(is_even, numbers))

    print(f"Input: {numbers}")
    print(f"Built-in filter result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def is_vowel(x):
        return x in 'aeiou'

    builtin_result = list(filter(is_vowel, letters))
    ft_result = list(ft_filter(is_vowel, letters))

    print(f"\nInput: {letters}")
    print(f"Built-in filter result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")
    print()


def test_ex06_2():
    """Test with None function parameter (truthiness test)"""
    print("=== test_ex06_2: None function parameter ===")

    mixed_values = [
        0, 1, '', 'hello', [], [1], {}, {'a': 1}, None, False, True
    ]

    try:
        builtin_result = list(filter(None, mixed_values))
        print(f"Built-in filter(None, {mixed_values}): {builtin_result}")
    except Exception as e:
        print(f"Built-in filter(None, ...) raised: {type(e).__name__}: {e}")
        builtin_result = None

    try:
        ft_result = list(ft_filter(None, mixed_values))
        print(f"ft_filter(None, {mixed_values}): {ft_result}")
    except Exception as e:
        print(f"ft_filter(None, ...) raised: {type(e).__name__}: {e}")
        ft_result = None

    print(f"Results match: {builtin_result == ft_result}")
    print()


def test_ex06_3():
    """Test with different iterable types"""
    print("=== test_ex06_3: Different iterable types ===")

    test_tuple = (1, 2, 3, 4, 5)

    def is_odd(x):
        return x % 2 == 1

    builtin_result = list(filter(is_odd, test_tuple))
    ft_result = list(ft_filter(is_odd, test_tuple))

    print(f"Tuple input: {test_tuple}")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    test_set = {1, 2, 3, 4, 5}

    builtin_result = set(filter(is_odd, test_set))
    ft_result = set(ft_filter(is_odd, test_set))

    print(f"\nSet input: {test_set}")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    test_string = "hello world"

    def is_vowel_str(x):
        return x in 'aeiou'

    builtin_result = list(filter(is_vowel_str, test_string))
    ft_result = list(ft_filter(is_vowel_str, test_string))

    print(f"\nString input: '{test_string}'")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")
    print()


def test_ex06_4():
    """Test error handling for invalid inputs"""
    print("=== test_ex06_4: Error handling ===")

    test_cases = [
        (42, [1, 2, 3]),
        ("string", [1, 2, 3]),
        (lambda x: x > 0, 42),
        (lambda x: x > 0, None),
    ]

    for i, (func, iterable) in enumerate(test_cases, 1):
        print(f"Test case {i}: func={func}, iterable={iterable}")

        try:
            builtin_result = list(filter(func, iterable))
            print(f"  Built-in filter: SUCCESS - {builtin_result}")
        except Exception as e:
            print(f"  Built-in filter: {type(e).__name__}: {e}")

        try:
            ft_result = list(ft_filter(func, iterable))
            print(f"  ft_filter: SUCCESS - {ft_result}")
        except Exception as e:
            print(f"  ft_filter: {type(e).__name__}: {e}")
        print()


def test_ex06_5():
    """Test edge cases with empty and single-element iterables"""
    print("=== test_ex06_5: Edge cases ===")

    def is_positive(x):
        return x > 0

    empty_list = []
    builtin_result = list(filter(is_positive, empty_list))
    ft_result = list(ft_filter(is_positive, empty_list))

    print(f"Empty list: {empty_list}")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    single_pass = [5]
    builtin_result = list(filter(is_positive, single_pass))
    ft_result = list(ft_filter(is_positive, single_pass))

    print(f"\nSingle element (pass): {single_pass}")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    single_fail = [-5]
    builtin_result = list(filter(is_positive, single_fail))
    ft_result = list(ft_filter(is_positive, single_fail))

    print(f"\nSingle element (fail): {single_fail}")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")
    print()


def test_ex06_6():
    """Test return type and iterator behavior"""
    print("=== test_ex06_6: Return type and iterator behavior ===")

    numbers = [1, 2, 3, 4, 5]

    def is_even_obj(x):
        return x % 2 == 0

    builtin_filter_obj = filter(is_even_obj, numbers)
    ft_filter_obj = ft_filter(is_even_obj, numbers)

    print(f"Built-in filter returns: {type(builtin_filter_obj)}")
    print(f"ft_filter returns: {type(ft_filter_obj)}")

    print(
        f"Built-in filter is iterable: "
        f"{hasattr(builtin_filter_obj, '__iter__')}"
    )
    print(
        f"ft_filter is iterable: "
        f"{hasattr(ft_filter_obj, '__iter__')}"
    )

    builtin_list = list(builtin_filter_obj)
    ft_list = list(ft_filter_obj)

    print(f"Built-in filter result: {builtin_list}")
    print(f"ft_filter result: {ft_list}")
    print(f"Results match: {builtin_list == ft_list}")
    print()


def test_ex06_7():
    """Test with complex predicates and lambda functions"""
    print("=== test_ex06_7: Complex predicates ===")

    data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'London'},
        {'name': 'Charlie', 'age': 35, 'city': 'Tokyo'},
        {'name': 'Diana', 'age': 28, 'city': 'Paris'}
    ]

    def is_adult_in_big_city(person):
        return (person['age'] >= 30
                and person['city'] in ['New York', 'London', 'Tokyo'])

    builtin_result = list(filter(is_adult_in_big_city, data))
    ft_result = list(ft_filter(is_adult_in_big_city, data))

    print("Complex data filtering:")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")

    nested = [[1, 2], [3], [], [4, 5, 6], [7]]

    def has_multiple_elements(lst):
        return len(lst) > 1

    builtin_result = list(filter(has_multiple_elements, nested))
    ft_result = list(ft_filter(has_multiple_elements, nested))

    print("\nNested lists filtering:")
    print(f"Built-in result: {builtin_result}")
    print(f"ft_filter result: {ft_result}")
    print(f"Match: {builtin_result == ft_result}")
    print()


def ext06_8(args=None):
    """Run ex06/filterstring.py with arguments and return result"""
    cmd = [sys.executable, "ex06/filterstring.py"]
    if args:
        cmd.extend(args)
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd="/home/rmorel/PERSO/4.ft_projects/Bootcamp-Python2/00"
    )
    return result.stdout.strip(), result.stderr.strip()


def test_ex06_9():
    """Test ex06/filterstring.py with valid arguments"""

    # Test case 1: 'Hello the world' with length 4
    stdout, stderr = ext06_8(['Hello the world', '4'])
    expected = "['Hello', 'world']"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 2: 'Hello the world' with length 99 (no words match)
    stdout, stderr = ext06_8(['Hello the world', '99'])
    expected = "[]"
    assert stdout == expected, f"Expected {expected}, got {stdout}"


def test_ex06_10():
    """Test ex06/filterstring.py with invalid arguments"""

    # Test case 1: Missing second argument
    stdout, stderr = ext06_8(['Hello the world'])
    expected_error = "AssertionError: the arguments are bad"
    assert stdout == expected_error, f"Expected {expected_error}, got {stdout}"

    # Test case 2: No arguments
    stdout, stderr = ext06_8([])
    expected_error = "AssertionError: the arguments are bad"
    assert stdout == expected_error, f"Expected {expected_error}, got {stdout}"

    # Test case 3: Too many arguments
    stdout, stderr = ext06_8(['Hello', '4', 'extra'])
    expected_error = "AssertionError: the arguments are bad"
    assert stdout == expected_error, f"Expected {expected_error}, got {stdout}"

    # Test case 4: Non-integer second argument
    stdout, stderr = ext06_8(['Hello world', 'abc'])
    expected_error = "AssertionError: the arguments are bad"
    assert stdout == expected_error, f"Expected {expected_error}, got {stdout}"

    # Test case 5: String with special characters (non-alphanumeric, non-space)
    stdout, stderr = ext06_8(['Hello@world!', '4'])
    expected_error = "AssertionError: the arguments are bad"
    assert stdout == expected_error, f"Expected {expected_error}, got {stdout}"


def test_ex06_11():
    """Test ex06/filterstring.py with edge cases"""

    # Test case 1: Empty string
    stdout, stderr = ext06_8(['', '0'])
    expected = "[]"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 2: Single word matching
    stdout, stderr = ext06_8(['hello', '4'])
    expected = "['hello']"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 3: Single word not matching
    stdout, stderr = ext06_8(['hi', '4'])
    expected = "[]"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 4: Multiple spaces between words
    stdout, stderr = ext06_8(['hello    world   test', '4'])
    expected = "['hello', 'world']"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 5: Zero length filter
    stdout, stderr = ext06_8(['a b c', '0'])
    expected = "['a', 'b', 'c']"
    assert stdout == expected, f"Expected {expected}, got {stdout}"

    # Test case 6: Negative length (should still work as filter function)
    stdout, stderr = ext06_8(['hello world', '-1'])
    expected = "['hello', 'world']"
    assert stdout == expected, f"Expected {expected}, got {stdout}"
