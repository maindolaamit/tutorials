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

def get_zero_var_cols(df):
    """
    Method to get all columns having zero variance
    """
    zero_var_columns = df.var()
    return zero_var_columns[zero_var_columns == 0].index.to_list()

def drop_zero_var_cols(df, threshold=0):
    """
    Method to drop all columns having zero variance
    """
    columns = get_zero_var_cols(df)
    print(f"Dropping columns : {columns}")
    return df.drop(get_zero_var_cols(df), axis=1)

def get_object_col_names(df):
    """
    Get all column names which are of object type
    """
    return df.select_dtypes(include='object').columns.to_list()

def get_uniq_label_counts(df):
    """
    Get all unique labels count
    """
    object_columns = get_object_col_names(df)
    return list(map(lambda x : (x, len(df[x].unique())), object_columns))

def get_col_top_labels(df, col, top=10):
    """
    Get top n labels for the given column
    """
    index = df[col].value_counts().head(top).index
    return index.to_list()

def top_one_hot_columns(df, top=None):
    """
    Returns a DataFrame of One Hot Encoded values of all Object columns
    """
    object_columns = get_object_col_names(df)
    one_hot_df = pd.DataFrame()
    for col in object_columns:
        # print(col, ':',  get_col_top_labels(df, col))
        for label in get_col_top_labels(df, col):
            one_hot_col = str(col + '_' + label)
            series = df[col]
            if one_hot_col not in one_hot_df.columns.to_list():
                one_hot_df[one_hot_col] = np.where(series == label, 1, 0)
                
    return one_hot_df

def main():
    df = pd.read_csv("Tweets.csv")
    print(f"DataFrame shape, Rows :{df.shape[0]} Columns : {df.shape[1]}")


if __name__ == '__main__':
    main()
