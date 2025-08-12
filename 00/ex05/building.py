import six
import string
import sys


def text_analyzer(s):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if not isinstance(s, six.string_types):
        print("ERROR, input must be a string")
        return
    countLow = 0
    countUpper = 0
    countSpace = 0
    countPunctuation = 0
    countDigit = 0
    for i in s:
        if i.islower():
            countLow += 1
        elif i.isupper():
            countUpper += 1
        elif i.isspace():
            countSpace += 1
        elif i in string.punctuation:
            countPunctuation += 1
        elif i.isdigit():
            countDigit += 1
    print("The text contains", len(s), "characters:")
    print(countUpper, "upper letters")
    print(countLow, "lower letters")
    print(countPunctuation, "punctuation marks")
    print(countSpace, "spaces")
    print(countDigit, "digits")


def main():
    if len(sys.argv) > 2:
        print("Need 0 or 1 argument only")
        sys.exit()
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        user_input = sys.stdin.readline()
        if not user_input:
            print("No input provided (Ctrl+D pressed)")
            sys.exit()
        text_analyzer(user_input)
    else:
        text_analyzer(sys.argv[1])


if __name__ == "__main__":
    main()
