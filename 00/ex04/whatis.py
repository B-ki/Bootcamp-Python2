import sys


def whois(s):
    try:
        i = int(s)
        if (i % 2):
            print("I'm Odd")
        elif not i:
            print("I'm Zero")
        else:
            print("I'm Even")
    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    """Printing NULL types"""
    try:
        assert len(sys.argv) == 2, "1 argument required, no more, no less"
    except AssertionError as msg:
        print(type(msg).__name__ + ": ", end="")
        print(msg)
        return

    arg1 = sys.argv[1]

    try:
        whois(arg1)
    except AssertionError as e:
        print(type(e).__name__ + ": ", end="")
        print(e)


if __name__ == "__main__":
    main()
