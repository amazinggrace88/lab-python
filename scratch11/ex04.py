import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from lab_python.scratch11.ex03_knn_function import train_test_split, MyScaler, MyKnnClassifier

if __name__ == '__main__':
    col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
    iris = pd.read_csv('iris.csv', header=None, names=col_names)
    print(iris.iloc[:5])

    # 데이터 프레임을 이용하여, 각 특성(변수)들과 Class(label)과의 관계 그래프 그리기 (차원 2개_x, y로 표시)
    iris_groupby_class = iris.groupby(by='Class')  #pyplot 에서도 groupby 쓸 수 있다.
    for name, group in iris_groupby_class:
        # print(name, len(group))  # groupby - group 이름(label 의 이름), len() : label 당 행 갯수
        plt.scatter(group['sepal-length'], group['sepal-width'], label=name)  # scatter 그래프 3개를 그려준다. (그룹별로 따로 점을 뿌리기)
    plt.legend()
    plt.xlabel('sepal-length')
    plt.ylabel('sepal-width')
    plt.show()  # 그래프 상 sepal-length, sepal-width 두 개를 가지고도 분류가 가능할 것 같다는 추론 할 수 있음.

    for name, group in iris_groupby_class:
        # print(name, len(group))  # groupby - group 이름(label 의 이름), len() : label 당 행 갯수
        plt.scatter(group['petal-length'], group['petal-width'], label=name)  # scatter 그래프 3개를 그려준다. (그룹별로 따로 점을 뿌리기)
    plt.legend()
    plt.xlabel('petal-length')
    plt.ylabel('petal-width')
    plt.show()

    # 하나의 화면을 분할하여 plot 대치하는 방법


if 0:
    # split
    X = iris.iloc[:, :-1].to_numpy()  # point
    y = iris.iloc[:, 4].to_numpy()  # labels  --> numpy 안해도 되는건가..? pd 인데
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # scaling
    scaler = MyScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    # knn algorithm apply
    knn = MyKnnClassifier(n_neighbors=7)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    # evaluation 1. accuracy rate..
    print(np.mean(y_test == y_pred))  # 0.9333333333333333
    # evaluation 2. conf_matrix, report
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    report = classification_report(y_test, y_pred)
    print(report)

    # 유방암 데이터
    cancer = pd.read_csv('wisc_bc_data.csv')
    print(cancer.head())
    # split
    X = cancer.iloc[:, 2:].to_numpy()
    y = cancer.iloc[:, 1].to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # scaling
    scaler = MyScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    # knn algorithm apply
    knn = MyKnnClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    # evaluation 1. accuracy rate..
    print(np.mean(y_test == y_pred))
    # evaluation 2. conf_matrix, report
    conf_matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(conf_matrix)
    print(report)

    