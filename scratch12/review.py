"""review"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

class Myscaler:
    def fit(self, X):
        """X의 평균, 표준편차 저장"""
        self.feature_means = np.mean(X, axis=0)  # column
        self.feature_std = np.std(X, axis=0)

    def transform(self, X):
        dim = X.shape
        transformed = np.empty(dim)
        for row in range(dim[0]):
            for col in range(dim[1]):
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_std[col]
        return transformed

if __name__ == '__main__':
    # 유방암 데이터를 가지고 plot => 차원축소하기 + graph 그리기
    cancer = pd.read_csv('wisc_bc_data.csv')
    print(cancer)
    print(cancer.shape)  # [569 rows x 32 columns]
    cancer_by_diagnosis = cancer.groupby(by='diagnosis')
    print('groupby cancer_by_diagnosis \n', cancer_by_diagnosis.head())
    col_names = cancer.columns.tolist()
    axis_for_graph = col_names[2:]  # id, diagnosis 뺐다
    print(axis_for_graph)
    print(len(axis_for_graph))  # 30 개 column

    xy = []
    for i in range(30):
        for j in range(i+1, 30):
            xy.append((axis_for_graph[i], axis_for_graph[j]))
    print('column 의 조합 : \n', xy)  # column 각 2개 조합 완성!
    print('xy의 길이 : \n', len(xy))  # 435
    # print(xy[1][0])
    # print(xy[1][1])
    print('xy의 예시 : \n', xy[1])

    # 435 개를 그릴 수는 없잖아..? ㅠ.ㅠ -> for 문 돌려서 25개 씩 돌림! (4개 만들어짐)
    for index_i in range(0, 100, 25):
        fig, ax = plt.subplots(5, 5)
        xy_idx = index_i
        for row in range(5):
            for col in range(5):
                axis = ax[row, col]  # numpy array 에서 사용하는 방법 (= ax[row][col] 가능)
                x = xy[xy_idx][0]
                y = xy[xy_idx][1]
                xy_idx += 1
                axis.set_title(f'{x} vs {y}')
                axis.set_xlabel(x)  # subplot 의 x 레이블
                axis.set_ylabel(y)  # subplot 의 y 레이블
                for name, group in cancer_by_diagnosis:
                    axis.scatter(group[x], group[y], label=name)
    plt.legend()
    plt.show()

"""review"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

class Myscaler:
    def fit(self, X):
        """X의 평균, 표준편차 저장"""
        self.feature_means = np.mean(X, axis=0)  # column
        self.feature_std = np.std(X, axis=0)

    def transform(self, X):
        dim = X.shape
        transformed = np.empty(dim)
        for row in range(dim[0]):
            for col in range(dim[1]):
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_std[col]
        return transformed

if __name__ == '__main__':
    # 유방암 데이터를 가지고 plot => 차원축소하기 + graph 그리기
    cancer = pd.read_csv('wisc_bc_data.csv')
    print(cancer)
    print(cancer.shape)  # [569 rows x 32 columns]
    cancer_by_diagnosis = cancer.groupby(by='diagnosis')
    print('groupby cancer_by_diagnosis \n', cancer_by_diagnosis.head())
    col_names = cancer.columns.tolist()
    axis_for_graph = col_names[2:]  # id, diagnosis 뺐다
    print(axis_for_graph)
    print(len(axis_for_graph))  # 30 개 column

    xy = []
    for i in range(30):
        for j in range(i+1, 30):
            xy.append((axis_for_graph[i], axis_for_graph[j]))
    print('column 의 조합 : \n', xy)  # column 각 2개 조합 완성!
    print('xy의 길이 : \n', len(xy))  # 435
    # print(xy[1][0])
    # print(xy[1][1])
    print('xy의 예시 : \n', xy[1])

    # 435 개를 그릴 수는 없잖아..? ㅠ.ㅠ -> for 문 돌려서 25개 씩 돌림! (4개 만들어짐)
    for index_i in range(0, 100, 25):
        fig, ax = plt.subplots(5, 5)
        xy_idx = index_i
        for row in range(5):
            for col in range(5):
                axis = ax[row, col]  # numpy array 에서 사용하는 방법 (= ax[row][col] 가능)
                x = xy[xy_idx][0]
                y = xy[xy_idx][1]
                xy_idx += 1
                axis.set_title(f'{x} vs {y}')
                axis.set_xlabel(x)  # subplot 의 x 레이블
                axis.set_ylabel(y)  # subplot 의 y 레이블
                for name, group in cancer_by_diagnosis:
                    axis.scatter(group[x], group[y], label=name)
    plt.legend()
    plt.show()
