from autopipeline.pipeline.components.classification_base import AutoPLClassificationAlgorithm
from autopipeline.pipeline.components.utils import get_categorical_features_indices

__all__ = ["CatBoostRegressor"]


class CatBoostRegressor(AutoPLClassificationAlgorithm):
    class__ = "CatBoostRegressor"
    module__ = "catboost"

    def _fit(self, estimator, X_train, y_train=None, X_valid=None, y_valid=None, X_test=None,
             y_test=None, feat_grp=None, origin_grp=None):
        categorical_features_indices = get_categorical_features_indices(origin_grp)
        if (X_valid is not None) and (y_valid is not None):
            eval_set = (X_valid, y_valid)
        else:
            eval_set = None
        self.estimator.fit(
            X_train, y_train, cat_features=categorical_features_indices,
            eval_set=eval_set, silent=True
        )
