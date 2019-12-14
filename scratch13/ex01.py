"""
선형 회귀
"""
import numpy as np
from sklearn.datasets import load_diabetes

# X, y = load_diabetes(return_X_y=True)
# print(X[:5]) # 컬럼 이름을 알 수 없음
# print(X.shape)  # (442, 10)
datasets = load_diabetes()
X = datasets.data
y = datasets.target
print(type(X))  # <class 'numpy.ndarray'>
print(type(y))
print(X.shape, y.shape)  # (442, 10) (442,)  <,)> col 1개 짜리~
features = datasets.feature_names
print(features)  # ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
print(X[0])  # 표준화된 데이터! (전처리까지 끝낸 데이터)
# 모든 특성(컬럼)들이 평균 0, 표준편차 1 로 표준화되 있음
print(y[0])

# 선형회귀 (linear regression)
# y = ax + b

# 1 개의 figure 에 10개의 subplot 을 그림
# y ~ 10 개의 특성
X_list = X.tolist()
y_list = y.tolist()
print(X_list[:5])
print(y_list[:5])
datasets_list =
print(datasets_list)