import pandas as pd
import os
from glob import glob


def get_dir_dataframe(path, pattern="*.csv"):
    """
    This methods reads all files in the given directory. Reads the file and return a Pandas DataFrame
    concatenating all the files into a single df
    :return: Pandas DataFrame
    """
    files = sorted(glob(f"{path}/{pattern}"))
    df = pd.concat((pd.read_csv(file) for file in files), index=False)
    
    return df


def main():
    df = pd.read_csv("Tweets.csv")
    print(f"DataFrame shape, Rows :{df.shape[0]} Columns : {df.shape[1]}")


if __name__ == '__main__':
    main()
