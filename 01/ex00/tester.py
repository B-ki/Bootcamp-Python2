from give_bmi import give_bmi, apply_limit


def main():
    height = [1.83, 1.60, 1.20, 2.50]
    weight = [80, 50, 110, 300]
    wrong = ["a", "b", "c", "d"]
    limit = 25
    print("TEST - Wrong values")
    try:
        give_bmi(height, wrong)
    except AssertionError as e:
        print(f"{type(e).__name__}: ", e)
    print(f"\nTEST - Correct values, limit = {limit}")
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))
    print("\nTEST SUBJECT")
    height2 = [2.71, 1.15]
    weight2 = [165.3, 38.4]
    bmi2 = give_bmi(height2, weight2)
    print(bmi2, type(bmi2))
    print(apply_limit(bmi2, 26))


if __name__ == "__main__":
    main()
