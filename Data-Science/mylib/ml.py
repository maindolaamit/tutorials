import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd
import sklearn.compose as compose
import sklearn.ensemble as ensemble
import sklearn.linear_model as linear_model
import sklearn.model_selection as model_selection
import sklearn.preprocessing as preprocessing
import sklearn.svm as svm
import sklearn.tree as tree
import xgboost as xgboost

from . import dispatcher

# Keep randomness same
np.random.seed(2210)


class EstimatorSelectHelper:
    # Code derived and changed accordingly from below
    # https://github.com/davidsbatista/machine-learning-notebooks/blob/master/hyperparameter-across-models.ipynb

    def __init__(self, models):
        self.models = models
        self.keys = models.keys()
        self.search_grid = {}
        self.df_score = None

    def fit(self, X, y, **grid_kwargs):
        for model_key in self.keys:
            # Check the model and param_grid
            model = self.models[model_key][0]
            param_grid = self.models[model_key][1]
            # Call GridSearchCV on the model and param_grid
            print(f"Running GridSearchCV for {model_key}")
            grid = model_selection.GridSearchCV(model, param_grid, **grid_kwargs)
            grid.fit(X, y)
            self.search_grid[model_key] = grid
        return self

    def score_summary(self, sort_by='mean_test_score'):
        frames = []
        for name, grid in self.search_grid.items():
            frame = pd.DataFrame(grid.cv_results_)
            frame = frame.filter(regex='^(?!.*param_).*$')
            frame['estimator'] = len(frame) * [name]
            frames.append(frame)
        df = pd.concat(frames)

        df = df.sort_values([sort_by], ascending=False)
        df = df.reset_index()
        df = df.drop(['rank_test_score', 'index'], 1)

        # columns = ['estimator'] + df.columns.tolist().remove('estimator')
        # Keep required columns
        df.rename(columns={'mean_test_score': 'mean_val_score', 'std_test_score': 'std_val_score'}, inplace=True)
        keep_columns = [
            "estimator",
            "mean_val_score",
            "std_val_score",
            "mean_fit_time",
            "mean_score_time",
            "params",
        ]
        df = df[keep_columns]
        self.df_score = df
        return self.df_score


class RegressionSelectHelper(EstimatorSelectHelper):

    def fit(self, X, y, **grid_kwargs):
        super().fit(X, y, **grid_kwargs)

    def score_summary(self, X_test, y_test, sort_by=['mean_squared_error']):
        super().score_summary()
        test_score = []
        for key, model in self.search_grid.items():
            y_pred = model.predict(X_test)
            import sklearn.metrics as sm
            mse = sm.mean_squared_error(y_test, y_pred)
            mae = sm.mean_absolute_error(y_test, y_pred)
            r2 = sm.r2_score(y_test, y_pred)
            test_score.append([key, model.best_params_, mse, mae, r2])

        test_score_columns = ['estimator', 'params', 'mean_squared_error', 'mean_absolute_error', 'r2_score',
                              'jacobian_score']
        df_test_score = pd.DataFrame(test_score, columns=test_score_columns)
        df_score = pd.merge(self.df_score, df_test_score, on=['estimator', 'params'])

        # Re arrange columns for readability
        score_columns = df_score.columns.tolist()[:2] + test_score_columns[2:] + df_score.columns.tolist()[2:-3]
        self.df_score = df_score[score_columns].sort_values(by=sort_by)
        return self.df_score, self.search_grid


class ClassifierSelectHelper(EstimatorSelectHelper):

    def fit(self, X, y, **grid_kwargs):
        super().fit(X, y, **grid_kwargs)

    def score_summary(self, X_test, y_test, sort_by=['accuracy', 'precision']):
        super().score_summary()

        test_score = []
        for key, model in self.search_grid.items():
            y_pred = model.predict(X_test)
            import sklearn.metrics as sm
            accuracy = sm.accuracy_score(y_test, y_pred)
            precision = sm.precision_score(y_test, y_pred)
            recall = sm.recall_score(y_test, y_pred)
            f1_score = sm.f1_score(y_test, y_pred)
            roc_auc = sm.roc_auc_score(y_test, y_pred)
            log_loss = sm.log_loss(y_test, y_pred)
            test_score.append([key, model.best_params_, accuracy, precision, recall, f1_score, roc_auc, log_loss])

        test_score_columns = ['estimator', 'params', 'accuracy', 'precision', 'recall', 'f1-score', 'roc_auc',
                              'log_loss']
        df_test_score = pd.DataFrame(test_score, columns=test_score_columns)
        df_score = pd.merge(self.df_score, df_test_score, on=['estimator'])
        # Re arrange columns for readability
        score_columns = ['estimator', 'mean_val_score', 'std_val_score', 'mean_fit_time', 'mean_score_time',
                         'params_x', 'params_y', 'accuracy', 'precision', 'recall', 'f1-score', 'roc_auc', 'log_loss']
        self.df_score = df_score[score_columns].sort_values(by=sort_by, ascending=False)
        return self.df_score, self.search_grid


def evaluate_classifiers(X_train, y_train, X_test, y_test, is_binary=False, cv=5, sort_by=None):
    """
    Perform Initial regression with all known models
    and return the DataFrame having accuracy score
    """
    models = {
        'SGDClassifier': (linear_model.SGDClassifier(), {}),
        'DecisionTreeClassifier': (tree.DecisionTreeClassifier(), {}),
        'SVM': (svm.SVC(), {}),
        'RandomForestClassifier': (ensemble.RandomForestClassifier(), {}),
        'LightGBMClassifier': (lgb.LightGBMClassifier(), {}),
        'AdaBoostClassifier': (ensemble.AdaBoostClassifier(), {}),
        'GradinetBoostingClassifier': (ensemble.GradientBoostingClassifier(), {}),
        'XGBClassifier': (xgboost.XGBClassifier(verbose=0), {}),
    }

    # LogisticRegression
    if is_binary:
        models.update({'LogisticRegression': (linear_model.LogisticRegression(), {})})

    select = ClassifierSelectHelper(models)
    select.fit(X_train, y_train, cv=cv, verbose=0)
    df_score, search_grid = select.score_summary(X_test, y_test)
    return df_score, search_grid


@staticmethod
def get_display_time(elapsed_seconds):
    hours, min, sec, message = 0, 0, 0, ""
    import math
    if elapsed_seconds > 60 * 60:
        hours = math.floor(int(elapsed_seconds / 3600))
        min = math.floor(int(elapsed_seconds - hours * 3600) / 60)
        sec = elapsed_seconds - hours * 3600 - min * 60
        return f"{hours} Hour {min} Minutes {sec} seconds"
    elif elapsed_seconds > 60:
        min = math.floor(int(elapsed_seconds / 60))
        sec = elapsed_seconds - min * 60
        return f"{min} Minutes {sec} seconds"
    else:
        sec = elapsed_seconds
        return f"{sec} seconds"


def fine_tune_model(model, param_grid, x_train, y_train, cv=5, verbose=0, randomized=False):
    """
    Fine Tune a given Model by using GridSearchCV with the Passed parameter grid
    :param model: Estimator Model
    :param param_grid: Parameters grid
    :param x_train: Train dataset
    :param y_train: Train target
    :param cv: No. of cross validations, default 5
    :param verbose: verbose, default 0
    :param randomized: default False, if True, randomized search to be used
    :return:
    """
    from time import perf_counter

    start_time = perf_counter()

    print(f"Performing Grid search for {type(model).__name__}...")

    grid_search = None
    if randomized:
        grid_search = model_selection.RandomizedSearchCV(model, param_grid, cv=cv, verbose=verbose, n_jobs=-1)
    else:
        grid_search = model_selection.GridSearchCV(model, param_grid, cv=cv, verbose=verbose, n_jobs=-1)

    # Start fine tuning of the model
    grid_search.fit(x_train, y_train)
    time_taken = round(perf_counter() - start_time, 2)
    print(f"Time elapsed(s) : {get_display_time(time_taken)} | score : {grid_search.best_score_:.2}")
    print(f"Best parameters : {grid_search.best_params_} ")
    return grid_search.best_estimator_


FOLD_MAPPPING = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}


def train_models(fold, df, target_col, drop_columns, models,
                 problem_type='classification', score='accuracy'):
    train_df = df[df.kfold.isin(FOLD_MAPPPING.get(fold))].reset_index(drop=True)
    valid_df = df[df.kfold == fold].reset_index(drop=True)

    train_df = train_df.drop(drop_columns + target_col, axis=1)
    valid_df = valid_df.drop(drop_columns + target_col, axis=1)

    y_train = train_df[target_col].values
    y_valid = valid_df[target_col].values

    for name, model in models.items():
        model.fit(train_df)

        if problem_type == 'classification':
            from metrics import ClassificationMetrics
            dispatcher.MODELS[model]
            preds = model.predict_proba(valid_df)[:, 1]
            metric = ClassificationMetrics()
            print(metric(score, y_valid, preds))
        else:
            from metrics import RegressionMetrics
            preds = model.predict(valid_df)
            metric = RegressionMetrics()
            print(metric(score, y_valid, preds))

        # Export the model
        joblib.dump(model, f"models/{model}_{fold}.pkl")
        joblib.dump(train_df.columns, f"models/{model}_{fold}_columns.pkl")


if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    df.drop(["id", "Unnamed: 32"], axis=1, inplace=True)
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    # Return the dataframe
    le.fit(df["diagnosis"])
    df["diagnosis"] = le.transform(df["diagnosis"])
    X, y = df.drop("diagnosis", axis=1), df["diagnosis"].values
    columns = X.columns.to_list()
    num_cols = len(columns)
    print(X.shape, y.shape)

    # Transform the data
    column_transformer = compose.ColumnTransformer([
        ('scaled', preprocessing.StandardScaler(), columns),
        ('normalize', preprocessing.Normalizer(), columns),
        ('yeo-johnson', preprocessing.PowerTransformer(method='yeo-johnson'), columns)
    ])

    X_ = column_transformer.fit_transform(X, y)
    keys = column_transformer.named_transformers_.keys()
    for i, key in enumerate(keys):
        start = i * column_transformer.n_features_in_
        end = start + column_transformer.n_features_in_
        print("=" * 100)
        print(f"{column_transformer.named_transformers_[key]} - {start}:{end}")
        X_value = X_[:, start:end]
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X_value, y, test_size=0.2)
        print("Evaluating classification models ...")
        df_clf_score, clf_grids = evaluate_classifiers(X_train, y_train, X_test, y_test, is_binary=True)
        print(df_clf_score)
        exit(0)
