"""
Boston house prices dataset
"""
# 보스톤 집값 데이터 세트 로딩
# 데이터 탐색 하기 + 그래프
# 데이터 탐색 결과를 바탕으로 선형회귀 (단순, 다중) 수행
# 학습 세트, 검증 세트 split
# 선형회귀 공식 도출, 예측하기
# 예측한 그래프 그리기
# 선형회귀 mean square error 계산 - 평균 제곱 오차
# R2 score 계산 - 결정 계수

# 1. 데이터 탐색 하기 + 그래프
import array
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

datasets = load_boston()  # Bunch - python 의 dict 와 비슷한 타입 (dict을 상속받아 만들어졌기 때문)
print('dataset keys : \n', datasets.keys())  # 'DESCR' - Describe
print('dataset DESCRIBE is : \n', datasets['DESCR'])

# data | target separate
X = datasets.data
y = datasets.target
print('X shape , y shape is : \n', X.shape, y.shape)  # (506, 13) (506,) --> 행이 506개인가 보군! (506,) 1차원 리스트
print('X head is : \n', X[:2])
print('y head is : \n', y[:2])
features = datasets.feature_names  # = datasets['feature_names'] 오쌤추천방법

# cf. dict 의 인덱싱 방법
d = {'myname': 'grace', 'myage': 28}
print(d['myname'])
# cf. bunch 의 인덱싱 방법 - 두가지 방법 제공 : d['myname'] or d.myname
# if. d['column-name'] -> 정상작동
# if. d.column-name -> 오작동, 공백 또는 대시(-) 가 있으면 d.column - d.name 으로 받아들여진다.

print('column name(features) is : \n', features)  # column names..
print(len(features))  # 13 개의 column 있어요~

# 2. subplots for modeling : y ~ feature
fig, ax = plt.subplots(4, 4)
ax_flat = ax.flatten()
for i in range(len(features)):
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)  # 집값과 각 변수들 간의 산점도
    axis.set_title(features[i])
plt.show()
# 내 생각에는..RM이 가장 상관관계가 있을 것 같고, LSTAT은 반비례 관계가 있을 것 같다(2차식도 가능). DIS 도 조금은..? - 변수 2개를 합쳐볼 수 있을 듯!
# 1개씩 나타낼 수도 있고, 2개씩 나타낼 수도 있고,
# 선처럼 보이는 것은 카테고리!

# 3. modeling
# 3-1. RM 단순선형회귀
# 'RM' column 은 index 5번째~
print(features[5])  # RM
RM = X[:, np.newaxis, 5]  # RM 은 # y = b + a*RM 이므로 x의 역할을 한다.

# 학습 세트, 검증 세트 split : 행이 506개 이므로, 506*0.8=404.8 405행까지 학습세트하자~
print(506 * 0.8)  # 404.8
RM_train = RM[:405]
RM_test = RM[405:]
y_train = y[:405]
y_test = y[405:]

# 선형회귀 공식 도출, 예측하기
lin_reg = LinearRegression()  # LR 객체 생성
lin_reg.fit(RM_train, y_train)
y_pred = lin_reg.predict(RM_test)

# 예측한 그래프 그리기
plt.scatter(RM_test, y_test)
plt.plot(RM_test, y_pred, 'go-')
plt.title('<RM impact on house prices>')
plt.show()
# 선형회귀 mean square error 계산
RM_mse = mean_squared_error(y_test, y_pred)
print(RM_mse)  # 73.84557039053418 --> 평균 제곱 오차
# R2 score 계산 : 결정계수 : a statistical measure of how close the data are to the fitted regression line.
# It is also known as the coefficient of determination
# or the coefficient of multiple determination for multiple regression
RM_r2 = r2_score(y_test, y_pred)
print(RM_r2)  # -1.777369130133816


# 3. modeling
# 3-2. 다중선형회귀
poly_feature = PolynomialFeatures(degree=2, include_bias=False)
# 차원의 갯수는 column 의 갯수와 상관없이! 그래프의 모양을 보고 결정한다
# if.. 차원의 갯수를 너무 늘려버리면???? 그래프가 데이터에 과적합이 되어버릴 수 있다.
# if.. 차원의 갯수를 너무 적게 하면 그래프가 정확하지 않음
# 학습 세트, 검증 세트 split : 행이 506개 이므로, 506*0.8=404.8 405행까지 학습세트하자~
train_set = X[:405]
test_set = X[405:]
#
# train_pf = poly_feature.fit_transform(train_set)
# print('train set\'s polynomial feature is..\n', train_pf[:5])
# print('train set\'s pf shape is .. \n', train_pf.shape)  # (405, 104) 행 405개, 열 104개
# test_pf = poly_feature.fit_transform(test_set)
# print('test set\'s polynomial feature is..\n', train_pf[:5])
#
# # 선형회귀 공식 도출, 예측하기
# y_pred_pf = lin_reg.fit(train_pf, y_train)
#
# # 예측한 그래프 그리기
# plt.scatter(train_pf, y_test)
# # --> 질문하기 : 왜,, 안되니? train_pf, y_test로 해주었는데
# # ( 사실 당연히 안되지! train_pf 는 행이 405개, 열이 104개나 된다고,, x는 값이 하나여야 한다)
# plt.plot(test_pf, y_pred_pf, 'go-')  # --> 설마 pf는 이상한 모양인가?
# plt.show()
#
# # ex04 에서 했었던, X_test = np.linspace(-3, 3, 100).reshape(100, 1) 를 이용하는 것 같기는 한데,, shape을 다시 잡아주는 거?
# # 그렇다면 왜 reshape() 을 해줄까? --> x를 값이 하나인 리스트 처럼 만드는 건가?
# # 교호작용???
#
# # 선형회귀 mean square error 계산
# pf_mse = mean_squared_error(y_pred_pf, y_test)  # ---> ???
# print(pf_mse)
#
# # R2 score 계산 : 결정계수 : a statistical measure of how close the data are to the fitted regression line.
#
