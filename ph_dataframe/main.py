import pandas as pd
import matplot as plt


def read_csv(filename):
    df = pd.read_csv(filename)

    #print(df.tail)
    return df


def extract_pH(filename):
    df = pd.DataFrame(read_csv(filename))
    pH = df['pH']
    pH.describe()
    pH = pH.cumsum()
    pH.plot()
    #print(pH.tail)
    return pH


if __name__ == "__main__":

    filename = "ph_dataframe/data.csv"
    filename = 'data.csv'
    #read_csv(filename)
    print(extract_pH(filename))
