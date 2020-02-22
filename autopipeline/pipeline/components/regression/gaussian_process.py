from copy import deepcopy

from autopipeline.pipeline.components.base import AutoPLRegressionAlgorithm


class GaussianProcess(AutoPLRegressionAlgorithm):
    class__ = "GaussianProcessRegressor"
    module__ = "sklearn.gaussian_process"

    def after_process_hyperparams(self):
        from sklearn.gaussian_process.kernels import RBF
        hyperparams=deepcopy(self.hyperparams)
        thetaL=hyperparams.pop("thetaL")
        thetaU=hyperparams.pop("thetaU")
        n_features = self.shape[1]
        kernel = RBF(
            length_scale=[1.0]*n_features,
            length_scale_bounds=[(thetaL, thetaU)]*n_features
        )
        hyperparams.update({
            "kernel":kernel
        })
        return hyperparams