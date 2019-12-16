"""
knn function test
"""
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report


def train_test_split(X, y, test_size):
    length = len(X)
    indices = np.array([i for i in range(length)])
    np.random.shuffle(indices)
    cut = int(length * (1 - test_size))
    X_train = X[indices[:cut]]
    y_train = y[indices[:cut]]
    X_test = X[indices[:cut]]
    y_test = y[indices[:cut]]
    return X_train, y_train, X_test, y_test


class MyScaler:
    def fit(self, X):  # 평균, 표준편차 저장
        self.feature_means = np.mean(X, axis=0)
        self.feature_std = np.std(X, axis=0)
    
    def transform(self, X):
        dim = X.shape  # X (행, 열)
        transformed = np.empty(dim)  # 빈 array
        for row in range(dim[0]):  # row 갯수만큼 반복
            for col in range(dim[1]):  # col 갯수만큼 반복
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_std[col]
        return transformed

class MyKnnClassifier:
    def __init__(self, n_neighbors):  # 최근접 이웃 k 개수 저장
        self.k = n_neighbors

    def fit(self, X_train, y_label):  # train data 의 답지를 저장함
        self.points = X_train
        self.labels = y_label

    def predict(self, X_test):
        predicts = []
        for test_pt in X_test:
            distances = self.distance(self.points, test_pt)
            winner = self.majority_vote(distances)
            predicts.append(winner)
        return np.array(predicts)

    def distance(self, X, y):
        return np.sqrt(np.sum((X - y) ** 2, axis=1))

    def majority_vote(self, distances):
        indices_by_distance = np.argsort(distances)
        k_nearest_neighbor = [self.labels[i] for i in indices_by_distance[:self.k]]
        vote_counts = Counter(k_nearest_neighbor)
        winner, winner_count = vote_counts.most_common(1)[0]
        return winner

if __name__ == '__main__':
    col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
    dataset = pd.read_csv('iris.csv', header=None, names=col_names)
    X = dataset.iloc[:, :-1].to_numpy()
    print(X)
    y = dataset.iloc[:, 4].to_numpy()
    print(y)
    # split
    X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
    # scaling
    scaler = MyScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    print('X_train is .. \n', X_train[:5])
    print('y_train is .. \n', y_train[:5])
    X_test = scaler.transform(X_test)
    print('scaled X_test is .. \n', X_test[:5])
    # knn classifier
    classifier = MyKnnClassifier(n_neighbors=3)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(y_pred[:5])
    # evaluation
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    report = classification_report(y_test, y_pred)
    print(report)
