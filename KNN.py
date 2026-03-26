import numpy as np

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]


        k_indices = np.argsort(distances, axis=0)[:self.k]


        k_nearest_labels = [self.y_train[i] for i in k_indices]


        values, counts = np.unique(k_nearest_labels, return_counts=True)
        return values[np.argmax(counts)]