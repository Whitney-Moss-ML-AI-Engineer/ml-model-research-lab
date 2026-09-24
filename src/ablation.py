"""Generic feature ablation experiment."""
from sklearn.base import clone

def ablate_feature_groups(model, X_train, X_test, y_train, y_test, groups):
    results = {}
    for name, columns in groups.items():
        train = X_train.drop(columns=columns)
        test = X_test.drop(columns=columns)
        fitted = clone(model).fit(train, y_train)
        results[name] = fitted.score(test, y_test)
    return results
