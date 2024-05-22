from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score

class CatBoostModel:
    def __init__(self):
        self.model = CatBoostClassifier()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy