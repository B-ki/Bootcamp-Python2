from load_csv import load


def main():
    print(load("../life_expectancy_years.csv"))
    print(load("../population_total.csv"))
    try:
        load("nimp")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
