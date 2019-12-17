# review
# sklearn.linear_model 구현 - with boston
# 1. SGDClassifier : stochastic gradient descent classifier
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
# bring the data
iris = load_iris()
X = iris.data
y = iris.target
print('X is : \n', X[:1])
print('y is : \n', y[:1])
features = iris.feature_names
print(features, len(features))  # 13 columns

# 1. make graph
# sns.pairplot - 변수간의 관계, 경향성 check
# seaborn 쓸 때는 DataFrame 으로 변환하기
# why ? pairplot은 데이터프레임을 인수로 받아 그리드(grid) 형태로 각 데이터 열의 조합에 대해 스캐터 플롯을 그린다.
# 출처 : https://datascienceschool.net/view-notebook/4c2d5ff1caab4b21a708cc662137bc65/
iris_df = pd.DataFrame(X, columns=features)
iris_df['Species'] = y
print(iris_df.iloc[:5, :])  # DataFrame 확인
print(iris_df.describe())

# 2. modeling
# model - SGDClassifier
# model 은 np.ndarray 로 만들어서 파라미터로 넣어준다.
# why? sklearn -> ndarray 로 만들어져 있음
# array 로 만들어준다.
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(f'X_train len : {len(X_train)}, X_test len : {len(X_test)}')

# SGDC 객체 생성
sgdc = SGDClassifier()
sgdc.fit(X_train)