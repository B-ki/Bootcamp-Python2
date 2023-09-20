import six
import string
import sys


def text_analyzer(s):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if not isinstance(s, six.string_types):
        print("ERROR, input must be a string")
        return
    elif not s:
        try:
            s = input("What is the text to analyze?: ")
        except EOFError as e:
            print(e)
    countLow = 0
    countUpper = 0
    countSpace = 0
    countPunctuation = 0
    for i in s:
        if i.islower():
            countLow += 1
        elif i.isupper():
            countUpper += 1
        elif i.isspace():
            countSpace += 1
        elif i in string.punctuation:
            countPunctuation += 1
    print("The text contains ", len(s), " character(s):")
    print("- ", countUpper, " upper letter(s)")
    print("- ", countLow, " lower letter(s)")
    print("- ", countPunctuation, " punctuation mark(s)")
    print("- ", countSpace, " space(s)")


def main():
    print("#########   ARGUMENTS   #########")
    if len(sys.argv) > 2:
        print("Need 0 or 1 argument only")
        sys.exit()
    elif len(sys.argv) == 1:
        text_analyzer(input("Please enter a phrase to analyze : "))
    else:
        text_analyzer(sys.argv[1])
    print("#########   TESTS   #########")
    str = "Python 3.0, released in 2008, was a major revision that is"
    str += "not completely backward-compatible with earlier versions. Python 2"
    str += " was discontinued with version 2.7.18 in 2020."
    print(f"Analyzing : {str}")
    text_analyzer(str)
    print("Analyzing Hello World!")
    text_analyzer("Hello World!")


if __name__ == "__main__":
    main()
