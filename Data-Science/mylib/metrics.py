import numpy as np
from sklearn import metrics as skmetrics

# Keep randomness same
np.random.seed(2210)

class ClassificationMetrics:
    def __init__(self):
        self.metrics = {'accuracy': self._accuracy,
                        'precision': self._precision,
                        'recall': self._recall,
                        'f1': self._f1,
                        'auc': self._auc,
                        'logloss': self._logloss
                        }

    def __call__(self, metric, y_true, y_pred, y_proba=None):
        if metric not in self.metrics:
            raise Exception(f'Invalid metric, should be {self.metrics.keys()}')
        if metric == 'auc':
            if y_proba is not None:
                return skmetrics.auc(y_true=y_true, y_pred=y_pred, y_proba=y_proba)
            else:
                raise Exception(f'y_proba can not be None for AUC.')
        elif metric == 'logloss':
            if y_proba is not None:
                return skmetrics.auc(y_true=y_true, y_pred=y_pred, y_proba=y_proba)
            else:
                raise Exception(f'y_proba can not be None for logloss.')
        else:
            return self.metrics[metric](y_true, y_pred)

    @staticmethod
    def _accuracy(y_true, y_pred):
        return skmetrics.accuracy_score(y_true, y_pred)

    @staticmethod
    def _f1(y_true, y_pred):
        return skmetrics.f1_score(y_true, y_pred)

    @staticmethod
    def _precision(y_true, y_pred):
        return skmetrics.precision_score(y_true, y_pred)

    @staticmethod
    def _recall(y_true, y_pred):
        return skmetrics.recall_score(y_true, y_pred)

    @staticmethod
    def _auc(y_true, y_pred):
        return skmetrics.auc_score(y_true, y_pred)

    @staticmethod
    def _logloss(y_true, y_pred):
        return skmetrics.log_loss(y_true, y_pred)


class RegressionMetrics:
    def __init__(self):
        self.metrics = {'mae': self._mae,
                        'mse': self._mse,
                        'r2': self._r2,
                        'rmse': self._rmse,
                        'msle': self._msle,
                        'rmsle': self._rmsle
                        }

    def __call__(self, metric, y_true, y_pred, y_proba=None):
        if metric not in self.metrics:
            raise Exception(f'Invalid metric, should be {self.metrics.keys()}')
        else:
            return self.metrics[metric](y_true, y_pred)

    @staticmethod
    def _mae(y_true, y_pred):
        return skmetrics.mean_absolute_error(y_true, y_pred)

    @staticmethod
    def _mse(y_true, y_pred):
        return skmetrics.mean_squared_error(y_true, y_pred)

    @staticmethod
    def _r2(y_true, y_pred):
        return skmetrics.r2_score(y_true, y_pred)

    @staticmethod
    def _rmse(y_true, y_pred):
        return np.sqrt(skmetrics.mean_squared_error(y_true, y_pred))

    @staticmethod
    def _msle(y_true, y_pred):
        return skmetrics.mean_squared_log_error(y_true, y_pred)

    @staticmethod
    def _rmsle(y_true, y_pred):
        return np.sqrt(skmetrics.mean_squared_log_error(y_true, y_pred))
