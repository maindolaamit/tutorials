import pandas as pd
import numpy as np
from sklearn import preprocessing

# Keep randomness same
np.random.seed(2210)

class CategoricalFeatures:
    def __init__(self, df, features, encoding_type='label', fillna_strategy='mode'):
        """
        Handle Categorical Features
        :param df: Pandas DataFrame
        :param features: Categorical Features
        :param encoding_type: encoding type
                label : Label encoding type
                binary : Binary encoding
                onehot : One Hot Encoding
                top-onehot : One Hot Encoding of Top 10 labels
        :param fillna_strategy: fill NA strategy explained below. Default "mode"
                mode -  mode of values
                new - create a new category unknown UKN for the null values
        """
        self.df = df
        self.features = features
        self.encoding_type = encoding_type
        self.fillna_strategy = fillna_strategy

        # Handle the NA
        self._handle_na()
        self.output_df = df.copy(deep=True)
        self.encoders = dict()

    def _handle_na(self):
        if self.fillna_strategy == 'new':
            for column in self.features:
                self.df[column] = self.df[column].astype(str).fillna('UKN')
        else:
            self.df = self.df[self.features].fillna('UKN')

    def _ordinal_encoding(self, columns):
        oe = preprocessing.OrdinalEncoder()
        for column in columns:
            self.encoders[column] = oe
            self.output_df[column] = oe.fit_transform(self.output_df[columns])
            self.output_df[column] = self.output_df[column].astype(int)

        return self.output_df

    def _label_encoding(self, columns):
        le = preprocessing.LabelEncoder()
        for column in columns:
            le.fit(self.df[column])
            self.encoders[column] = le
            self.output_df[column] = le.fit_transform(self.df[column])
            self.output_df[column] = self.output_df[column].astype(int)
        return self.output_df

    def _count_frequency_encoding(self, columns):
        """
        Perform top one-hot encoding for the labels
        """
        for column in columns:
            series = self.df[column]
            count_dict = series.value_counts().to_dict()
            self.encoders = count_dict
            self.output_df[column] = self.output_df[column].map(count_dict)
            self.encoders[column] = count_dict
        return self.output_df

    @staticmethod
    def get_col_top_labels(series, top=10):
        """
        Get top n labels for the given Pandas Series
        """
        index = series.value_counts().head(top).index
        return index.to_list()

    @staticmethod
    def get_uniq_labels_count(df, feature):
        """
        Get count of all the unique labels in a column
        :param df: Pandas DataFrame
        :param feature: Feature/Column
        :return: Cont of all unique labels
        """
        return len(df[feature].unique())

    @staticmethod
    def get_all_uniq_labels_count(df, features):
        """
        Get count of all the unique labels
        :param df: Pandas DataFrame
        :param features: Features/Columns
        :return: List of Tuples having columns and count of unique labels
        """
        return list(map(lambda x: (x, len(df[x].unique())), features))

    def _top_one_hot_encoding(self, columns):
        """
        Perform top one-hot encoding for the labels
        """
        for column in columns:
            series = self.df[column]
            top_labels = self.get_col_top_labels(series)
            for label in top_labels:
                one_hot_col = str(column + '_' + label)
                self.output_df[one_hot_col] = np.where(series == label, 1, 0)
            self.output_df.drop(column, axis=1, inplace=True)

        return self.output_df

    def _one_hot_encoding(self, columns):
        print('onehot encoding')
        # ohe = preprocessing.OneHotEncoder()
        for column in columns:
            onehot_df = pd.get_dummies(self.df[column], prefix=column)
            self.output_df = pd.concat([self.output_df, onehot_df])
            self.output_df.drop(column, axis=1, inplace=True)
        return self.output_df

    def _label_binarizer_encoding(self, columns):
        for column in columns:
            lbl = preprocessing.LabelBinarizer()
            lbl.fit(self.df[column].values)
            val = lbl.transform(self.df[column].values)
            self.output_df = self.output_df.drop(column, axis=1)
            for j in range(val.shape[1]):
                new_col_name = column + f"__bin_{j}"
                self.output_df[new_col_name] = val[:, j]
            # self.binary_encoders[column] = lbl
        return self.output_df

    def fit_transform(self):
        if self.encoding_type == 'label':
            return self._label_encoding(self.features)
        elif self.encoding_type == 'ordinal':
            return self._ordinal_encoding(self.features)
        elif self.encoding_type == 'ohe':
            return self._one_hot_encoding(self.features)
        elif self.encoding_type == 'count_freq':
            return self._count_frequency_encoding(self.features)
        elif self.encoding_type == 'ohe-top':
            return self._top_one_hot_encoding(self.features)
        elif self.encoding_type == 'label_binarizer':
            return self._label_binarizer_encoding(self.features)
        else:
            raise Exception(f'{self.encoding_type} : Invalid value for encoding type')


if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    # print(df.head(2))
    features = ['diagnosis']
    cat = CategoricalFeatures(df, features, 'ordinal', 'mode')
    transformed = cat.fit_transform()
    print(transformed[:6])
