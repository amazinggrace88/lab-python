"""
matrix(행렬)을 이용한 modeling 해석
선형회귀식을 행렬을 사용하여 찾아보자.
"""
import numpy as np
import matplotlib.pyplot as plt

# bring the matrix
from sklearn.linear_model import LinearRegression

np.random.seed(1216)
X = 2 * np.random.rand(100, 1)  # 2차원 배열 형태 : 100행 1열
print('X shape is..\n', X.shape)  # 범위 (0.0 ~ 1.0)* 2
y = 4 + 3 * X + np.random.randn(100, 1)  # np.random.randn(100, 1) - 잔차 역할 (randn : 정규분포를 따르는 난수 randn)
print('y shape is..\n', y.shape)  # 똑같이 만들었다.

# graph
plt.scatter(X, y)
plt.show()

# 해석
# 방정식 n 개를 행렬의 곱셈으로 나타내자 (노트 필기 참조)
X_b = np.c_[np.ones((100, 1)), X]
# np.ones((100, 1)) : np.ones - 행렬 안을 1로 채운다. 안을 tuple 로 주어야 함. (100행 1열 1로 채움)
print('X_b shape..\n', X_b.shape)
print(X_b[:5])

# theta 찾기
# linalg module : linear algebra(선형대수)의 약자
# X_b ^ T * y - 내적을 찾는다.
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(theta_best)  # theta_best 는 (b, a) 를 뜻한다.

# 행렬식을 이용해서 찾은 theta 값과 LinearRegression 클래스에서 계산된 theta 비교
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(f'y절편: {lin_reg.intercept_}, 기울기: {lin_reg.coef_}')

X_test = [[0],
          [1],
          [2]]
#  행렬식: y = X_b @ theta
X_test_b = np.c_[np.ones((3, 1)), X_test]
print(X_test_b)
y_pred = X_test_b.dot(theta_best)
print(y_pred)

# scikit-learn 패키지를 사용한 예측
predictions = lin_reg.predict(X_test)
print(predictions)

plt.scatter(X, y)
plt.plot(X_test, y_pred, 'ro-')
plt.show()

