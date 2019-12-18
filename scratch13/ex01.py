"""
선형 회귀
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import load_diabetes

# 1. bring the data
X, y = load_diabetes(return_X_y=True)
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

# cf.
# .info -> DF
# sklearn -> ndarray 로 만들어져 있음


# 2. subplots for modeling
# 선형회귀 (linear regression)
# y = ax + b

# 1 개의 figure 에 10개의 subplot 을 그림
# y ~ 10 개의 특성
# 1개의 figure 에 10개의 subplot 을 그려서, 변수들과 당뇨병(y)의 대략적 관계를 파악.
# y ~ age, y ~ sex, y ~ bmi, ...
fig, ax = plt.subplots(3, 4)  # 행 갯수, 컬럼 갯수 -> 그래프 표를 만든다.
for row in range(3):
    for col in range(4):
        axis = ax[row, col]
        idx = 4 * row + col
        if idx > 9:
            break
        x = X[:, idx]
        axis.scatter(x, y)
        axis.set_title(features[idx])
plt.title('all graph')
plt.show()

# flatten 을 이용한 다른 방법
array = np.array([[1, 2],
                  [3, 4]])
print(array)  # 2*2 행렬(2차원 배열)
# row, col 꺼내기 1
for row in range(2):
    for col in range(2):
        print(array[row, col], end=' ')
print()
# flatten 을 이용 2
array_flatten = array.flatten()
print(array_flatten)  # 2차원 배열을 평평하게 만든다.(1차원 배열로 만든다) -> 차원 -1
for i in range(4):
    print(array_flatten[i], end=' ')
print()
# fig, ax 에 적용
fig, ax = plt.subplots(3, 4)
# ax : 3*4형태의 2차원 배열
ax_flat = ax.flatten()
for i in range(len(features)):
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)
    axis.set_title(features[i])
plt.show()



# 3. modeling
# y = b + a*bmi : y 와 bmi 간의 선형관계식을 찾아보자.
bmi = X[:, np.newaxis, 2]  # data 에서 'bmi' 컬럼만 선택,  np.newaxis 로 2차원 배열 만들어줌!
print(bmi[:5])  # ndarray type
print('bmi shape is .. \n', bmi.shape)  # np.newaxis의 효과로 (442, 0) 에서 (442, 1) 로 변했다!

# bmi 를 학습(training set)와 검증(test set) 세트로 분리
bmi_train = bmi[:-40]
bmi_test = bmi[-40:]
y_train = y[:-40]
y_test = y[-40:]

# linear regression model 객체 생성
regr = linear_model.LinearRegression()

# training set 를 학습(fit) : 절편 b와 기울기 a를 결정 (오차를 최소화시키는 방향으로)
regr.fit(bmi_train, y_train)
print('coefficients : \n', regr.coef_)  # 기울기 a : coefficient

# if.  bmi = X[:,2]로 한다면..
# ValueError: Expected 2D array, got 1D array instead:
# error : Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
# 1d array 은 LinearRegression 에 쓸 수가 없다! 2차원 배열이 필요함
# [[1, ], * newaxis => ,(공백)으로 축을 하나 만든다.
#  [2, ],
#  [3, ]] 처럼 열이 1개 이상인 2차원 배열로 만들어야 한다. bmi = X[:, np.newaxis, 2] 로 2차원 배열 만들어주었다!

# 검증 세트로 테스트
y_pred = regr.predict(bmi_test)

# 선형 회귀 식 -> X가 _일 때 y는 얼마인가 (X는 연속분포) -> 값 1개를 연속적으로 예측하므로 선 그래프로 리턴
plt.scatter(bmi_test, y_test)
plt.plot(bmi_test, y_pred, '-', color='g')
plt.title('Diabates vs BMI')
plt.show()
# 오차하강법 - 오차들의 제곱의 합을 최소화시킨다. 즉, 선형회귀식을 데이터에 맞게 조절하여 최적의 선을 만든다.

# y ~ s5 변수 사이 선형관계식을 찾고, 그래프를 그리자
bmi = X[:, np.newaxis, -2]
print(bmi[:5])
bmi_train = bmi[:-40]
bmi_test = bmi[-40:]
y_train = y[:-40]
y_test =y[-40:]
# model object
regr = linear_model.LinearRegression()
# fit
regr.fit(bmi_train, y_train)
print('coefficient is..\n', regr.coef_)  # 계수(변수에 곱해지는 상수 인자), 즉 기울기
print('intercept is..\n', regr.intercept_)
# prediction
y_pred = regr.predict(bmi_test)
# graph - plot
plt.scatter(bmi_test, y_test)  # x의 범위 : bmi_test, y의 값 : y_test (실제값)
plt.plot(bmi_test, y_pred, 'go-')  # x의 범위 : bmi_test, y의 값 : y_pred (예측값)
plt.title('Diabates vs s5')
plt.show()



