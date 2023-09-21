from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("../life_expectancy_years.csv")
    fr_df = df[(df['country'] == 'France')]
    years = fr_df.columns[1:].astype(int)
    expectancy = fr_df.iloc[:, 1:].values.flatten()
    plt.plot(years, expectancy)
    plt.title('Life Expectancy Over the Years for France')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    main()
