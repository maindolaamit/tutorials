from glob import glob

import numpy as np
import pandas as pd


def get_dir_dataframe(path, pattern="*.csv"):
    """
    This methods reads all files in the given directory. Reads the file and return a Pandas DataFrame
    concatenating all the files into a single df
    :return: Pandas DataFrame
    """
    files = sorted(glob(f"{path}/{pattern}"))
    df = pd.concat((pd.read_csv(file) for file in files), index=False)

    return df


def get_stugres_bin(sample_size):
    """Return the number of bins for sample size based on Sturge's rule"""
    return int(np.floor(np.log2(sample_size) + 1))


def get_dtype_columns(df, include='object'):
    """
    Get all column names which are of object type
    """
    return df.select_dtypes(include=include).columns.to_list()


def get_zero_var_cols(df):
    """
    Method to get all columns having zero variance
    """
    variance = df.var()
    # Check for numerical columns
    zero_var_columns = [variance[variance == 0].index.to_list()]
    # Check for Feature columns
    for column in df.get_dtype_columns(include='object'):
        if df[column].nunique == 1:
            zero_var_columns.append(column)

    return zero_var_columns


def get_columns_by_variance(X, y, threshold=0.0):
    """
    Method to fetch columns based on threshold variance
    """
    from sklearn.feature_selection import VarianceThreshold
    selector = VarianceThreshold(threshold).fit(X, y)
    return X.columns[selector.get_support()]


def drop_columns_by_variance(df, threshold=0):
    """
    Method to drop all columns having zero variance
    """
    columns = get_columns_by_variance(df, threshold)
    drop_columns = set(df.columns) - set(columns)
    print(f"Dropping columns : {drop_columns}")
    return df.drop(drop_columns, axis=1)


def get_kbest_columns(X, y, k=2, score_func=None):
    """
    Method to fetch columns based on SelectKBest feature selection
    """
    from sklearn.feature_selection import SelectKBest
    selector = SelectKBest(score_func=score_func, k=k).fit(X, y)
    return X.columns[selector.get_support()]


def get_percentile_columns(X, y, percentile=2, score_func=None):
    """
    Method to fetch columns based on SelectPercentile feature selection
    """
    from sklearn.feature_selection import SelectPercentile
    selector = SelectPercentile(score_func=score_func, percentile=percentile).fit(X, y)
    return X.columns[selector.get_support()]


def get_uniq_label_counts(df):
    """
    Get all unique labels count in the DataFrame
    """
    object_columns = get_dtype_columns(df)
    return list(map(lambda x: (x, len(df[x].unique())), object_columns))


def get_col_top_labels(series, top=10):
    """
    Get top n labels for the given Pandas Series
    """
    index = series.value_counts().head(top).index
    return index.to_list()


def top_one_hot_columns(df, top=10):
    """
    Returns a DataFrame of One Hot Encoded values of all Object columns
    """
    object_columns = get_dtype_columns(df)
    one_hot_df = pd.DataFrame()
    for col in object_columns:
        for label in get_col_top_labels(df[col], top):
            one_hot_col = str(col + '_' + label)
            series = df[col]
            if one_hot_col not in one_hot_df.columns.to_list():
                one_hot_df[one_hot_col] = np.where(series == label, 1, 0)

    return one_hot_df


def print_classification_score(model, X_test, y_test, target_names=None, title="Confusion Matrix"):
    """ Method to print and plot Confusion matrix, F1 Score """
    from sklearn.metrics import classification_report
    y_pred_classes = np.argmax(model.predict(X_test), axis=1)  # Multiclass classification
    y_true_classes = np.argmax(y_test, axis=1)  # Multiclass classification
    print(classification_report(y_true_classes, y_pred_classes, target_names=target_names))
    enhanced_cnf = get_enhanced_confusion_matrix(y_true_classes, y_pred_classes, target_names)
    # Import confusion_matrix plotting from the library
    from charts import plot_confusion_matrix
    plot_confusion_matrix(enhanced_cnf, target_names, title)


def get_enhanced_confusion_matrix(y, y_pred, labels=None):
    """"enhances confusion_matrix by adding sensitivity and specificity metrics"""
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y, y_pred, labels=labels)
    sensitivity = float(cm[1][1]) / float(cm[1][0] + cm[1][1])
    specificity = float(cm[0][0]) / float(cm[0][0] + cm[0][1])
    weighted_accuracy = (sensitivity * 0.9) + (specificity * 0.1)
    return cm, sensitivity, specificity, weighted_accuracy


if __name__ == '__main__':
    None
