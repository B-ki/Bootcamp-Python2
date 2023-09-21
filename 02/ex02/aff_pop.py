from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("../population_total.csv")
    fr_df = df[(df['country'] == 'France')]
    be_df = df[(df['country'] == 'Belgium')]
    years = fr_df.columns[1:251].astype(int)
    pop_fr = fr_df.iloc[:, 1:251].values.flatten()
    pop_fr = [float(value.strip('M')) for value in pop_fr]
    pop_be = be_df.iloc[:, 1:251].values.flatten()
    pop_be = [float(value.strip('M')) for value in pop_be]
    plt.plot(years, pop_fr, label='France')
    plt.plot(years, pop_be, label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.show()


if __name__ == "__main__":
    main()
