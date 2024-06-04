import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filename):
    df = pd.read_csv(filename)

    #print(df.head)
    return df


def extract_pH(filename):
    df = pd.DataFrame(read_csv(filename))
    pH = df['pH']
    #print(pH.tail)
    pH.describe()
    pH = pH.cumsum()
    pH.plot()
    plt.show()
    return pH, pH.describe()


if __name__ == "__main__":

    filename = "ph_dataframe/data.csv"
    filename = 'data.csv'
    #read_csv(filename)
    print(extract_pH(filename))
