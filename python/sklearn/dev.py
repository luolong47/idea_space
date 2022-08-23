if __name__ == '__main__':
    from sklearn.datasets import load_iris
    from xgboost import XGBClassifier
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.model_selection import HalvingRandomSearchCV
    from scipy.stats import uniform

    iris = load_iris()
    logistic = XGBClassifier()
    params = dict(C=uniform(loc=0, scale=4), penalty=['l2', 'l1'])
    clf = RandomizedSearchCV(logistic, params, random_state=0)
    X = iris.data
    y = iris.target
    search = clf.fit(X, y)
    print(search.best_params_)
    # {'C': 2, 'penalty': 'l1'}


def hello():
    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import HalvingRandomSearchCV
    from scipy.stats import randint
    import numpy as np

    X, y = load_iris(return_X_y=True)
    clf = RandomForestClassifier(random_state=0)
    np.random.seed(0)

    param_distributions = {"max_depth": [3, None],
                           "min_samples_split": randint(2, 11)}
    search = HalvingRandomSearchCV(clf, param_distributions,
                                   resource='n_estimators',
                                   max_resources=10,
                                   random_state=0).fit(X, y)
    print(search.best_params_)
