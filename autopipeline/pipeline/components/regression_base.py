from autopipeline.pipeline.components.base import AutoPLComponent


class AutoPLRegressionAlgorithm(AutoPLComponent):
    """Provide an abstract interface for regression algorithms in
    auto-sklearn.

    Make a subclass of this and put it into the directory
    `autosklearn/pipeline/components/regression` to make it available."""

    # def _pred_or_trans(self, X_train, X_valid=None, X_test=None):
    def _pred_or_trans(self, X_train_, X_valid_=None, X_test_=None, X_train=None, X_valid=None, X_test=None,
                       is_train=False):
        return self.after_pred_y(self.estimator.predict(X_train_))

    def predict(self, X):
        return self.pred_or_trans(X)

    def after_pred_y(self, y):
        return y
