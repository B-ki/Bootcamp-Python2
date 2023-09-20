from array2D import slice_me


def main():
    print("TEST SUBJECT")
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print("\nTEST - Wrong values")
    try:
        print(slice_me(family, 7, 8))
    except AssertionError as e:
        print(f"{type(e).__name__}: ", e)
    print("\nTEST - Limit values")
    print(slice_me(family, 4, 4))


if __name__ == "__main__":
    main()
