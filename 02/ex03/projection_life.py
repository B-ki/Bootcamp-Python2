from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    df_l = load("../life_expectancy_years.csv")
    df_g = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_l = df_l[['country', '1900']]
    df_g = df_g[['country', '1900']]
    merged_df = df_g.merge(df_l, on='country', suffixes=('_life_expectancy', '_income'))
    print(merged_df)
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['1900_life_expectancy'], merged_df['1900_income'])
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    x_values = [300, 1000, 10000]
    plt.xticks(x_values, labels=['300', '1000', '10000'])
    plt.ylabel('Life Expectancy')
    plt.show()
    correlation = np.corrcoef(merged_df['1900_life_expectancy'], merged_df['1900_income'])[0, 1]
    print(f'Correlation between Life Expectancy and Income (1900): {correlation:.2f}')



if __name__ == "__main__":
    main()
