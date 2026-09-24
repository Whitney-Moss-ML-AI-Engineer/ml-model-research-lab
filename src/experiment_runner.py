"""Small reproducible experiment runner."""
from dataclasses import dataclass
import numpy as np
from sklearn.base import clone
from sklearn.metrics import mean_squared_error

@dataclass
class ExperimentResult:
    name: str
    rmse: float

def run_experiment(name, estimator, X_train, X_test, y_train, y_test):
    model = clone(estimator)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    return ExperimentResult(name, float(np.sqrt(mean_squared_error(y_test, prediction))))

def compare_models(models, X_train, X_test, y_train, y_test, seed=42):
    np.random.seed(seed)
    return [run_experiment(name, model, X_train, X_test, y_train, y_test)
            for name, model in models.items()]
