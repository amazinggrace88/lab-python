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

datasets = load_boston()  # Bunch - python 의 dict 와 비슷한 타입 (dict 을 상속받아 만들어졌기 때문)
print('dataset keys : \n', datasets.keys())  # 'DESCR' - Describe
print('dataset DESCRIBE is : \n', datasets['DESCR'])

# data | target separate
X = datasets.data
y = datasets.target
print('X shape , y shape is : \n', X.shape, y.shape)  # (506, 13) (506,) --> 행이 506개인가 보군! (506,) 1차원 리스트
print('X head is : \n', X[:2])
print('y head is : \n', y[:2])
features = datasets.feature_names  # = datasets['feature_names'] 오쌤추천방법

# cf. bunch 의 인덱싱 방법 - 두가지 방법 제공 : d['myname'] or d.myname
# if. d['column-name'] -> 정상작동
# if. d.column-name -> 오작동, 공백 또는 대시(-) 가 있으면 d.column - d.name 으로 받아들여진다.
# cf. dict 의 인덱싱 방법
d = {'myname': 'grace', 'myage': 28}
print(d['myname'])

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
# 선처럼 보이는 건 카테고리!


# 3. modeling
# 3-1. RM 단순선형회귀
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(f'X_train len : {len(X_train)}, X_test len : {len(X_test)}')

# 학습 세트를 사용해서 선형회귀 - 단순 선형회귀, 다중 선형회귀
# price = b0 + b1 * RM: 집값 ~ 방의 갯수(독립변수)
X_train_rm = X_train[:, np.newaxis, 5]  # X_train_rm 만 추출한다. 1차원 리스트이므로 2차원 배열로 만들어 주었다.
X_test_rm = X_test[:, np.newaxis, 5]
# 1d array 은 LinearRegression 에 쓸 수가 없다! 2차원 배열이 필요함
print(f'X_train_rm : {X_train_rm.shape}, X_test_rm : {X_test_rm.shape}')

# lin 객체 생성
lin_reg = LinearRegression()  # Linear Regression 객체 생성
lin_reg.fit(X_train_rm, y_train)  # fitting 즉 적합(학습) 시킨다 -> b0, b1 을 찾는다.(절편 및 기울기)
# RM을 주고 결과값을 준다.
print(f'intercept : {lin_reg.intercept_}, coefficient : {lin_reg.coef_}')
# 예측
y_pred_rm = lin_reg.predict(X_test_rm)  # 전체를 넘기는 것이 아니라, RM을 넘기는 거다~
# 그래프 : 실제값 - scatter, 예측값 - plot
plt.scatter(X_test_rm, y_test)
plt.plot(X_test_rm, y_pred_rm, 'go-')
plt.xlabel('RM')
plt.ylabel('Price')
plt.title('Price ~ RM')
plt.show()

# mean square error 계산
# 오차의 제곱의 평균이 작은 것이,, 더 좋은 예측이지!
# error_i = y_i(실제값) - y_i_hat(예측값), error^2 = (y_i - y_i_hat)**2
# MSE : sum(error^2) / 갯수
mse = mean_squared_error(y_test, y_pred_rm)  # 실제값, 예측값 array
print('Price ~ RM : mse is :', mse)
# RMSE(Squared-root MSE)
rmse = np.sqrt(mse)
print('Price ~ RM : rmse is :', rmse)
# R2 score 계산
# The coefficient R^2 : 결정계수
# 방법 1. lin_reg.score
r2_1 = lin_reg.score(X_test_rm, y_test)  # X test sample(X_test_rm), y 실제값 !! parameter 조심하기~
# 방법 2. r2_score in metrics
r2_2 = r2_score(y_test, y_pred_rm)  # y_true 실제값, y_pred 예측값 !! parameter 조심하기~
print(f'Price ~ RM : R^2 1 = {r2_1}, R^2 2 = {r2_2}')

# 결정계수의 의미 : 전체 모델의 약 44% 정도 설명 가능하다.
# 결정계수 : 통계학에서, 결정계수(決定係數, 영어: coefficient of determination)는 추정한 선형 모형이 주어진 자료에 적합한 정도를 재는 척도
# 반응 변수의 변동량 중에서 적용한 모형으로 설명가능한 부분의 비율
# 결정계수의 값은 0에서 1사이에 있으며, 종속변인과 독립변인 사이에 상관관계가 높을수록 1에 가까워진다
# (결정계수가 0에 가까운 값을 가지는 회귀모형은 유용성이 낮은 반면, 결정계수의 값이 클수록 회귀모형의 유용성이 높다고 할 수 있다)

# train set 에 대한 결정계수도 만들 수 있다.
r2_3 = lin_reg.score(X_train_rm, y_train)  # train set 에서의 rm 에서의 설명력
print(f'Price ~ RM in train set : R^2 4 = {r2_3}')
# r2_score in metrics 는 parameter 가 다르므로 쓸 수 없다 ~


# 3-2. LSTAT 단순선형회귀
# Price ~ LSTAT 의 관계
# price = b0 + b1 * lstat
# lstat 컬럼으로 이루어진 X 배열을 만들자
X_train_lstat = X_train[:, np.newaxis, 12]  # 학습세트
X_test_lstat = X_test[:, np.newaxis, 12]  # 검증세트
# fitting 적합 or training 학습
lin_reg.fit(X_train_lstat, y_train)
print(f'intercept : {lin_reg.intercept_}, coefficient : {lin_reg.coef_}')
# predict
y_pred_lstat = lin_reg.predict(X_test_lstat)
plt.scatter(X_test_lstat, y_test)
plt.plot(X_test_lstat, y_pred_lstat, 'go-')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.title('Price ~ LSTAT')
plt.show()
# 결정계수
mse = mean_squared_error(y_test, y_pred_lstat)
print('Price ~ LSTAT : mse is :', mse)
rmse = np.sqrt(mse)
print('Price ~ LSTAT : rmse is :', rmse)
r2_4 = lin_reg.score(X_test_lstat, y_test)
r2_5 = r2_score(y_test, y_pred_lstat)
print(f'Price ~ LSTAT : R^2 = {r2_4}, R^2 = {r2_5}')


# 3-3. LSTAT 다중선형회귀
# Price ~ LSTAT + LSTAT**2 선형회귀
# price = b0 + b1*lstat + b2*lstat**2
# 3-2 와 R2 를 비교하여 더 큰 녀석이 데이터를 잘 설명한다.

# PolynomialFeatues 객체 생성
poly = PolynomialFeatures(degree=2, include_bias=False)
# interactiotn_only = false 교호작용 효과만 분석 (즉 제곱항, 세제곱항 쓰지 않음)
# include_bias : True 오차(잔차) 삽입
# PolynomialFeatues 객체에 대한 설명 : 데이터에 다항식 항들을 컬럼으로 추가해주는 클래스 객체

# 학습세트에 다항식 항을 추가 -> fit/train 할 때 사용 (필기 참고)
X_train_lstat_poly = poly.fit_transform(X_train_lstat)  # 컬럼 옆에 lstst^2 등 을 붙여준다. (x+y)
# 검증세트에 다항식 항을 추가 -> fit/train 할 때 사용
X_test_lstat_poly = poly.fit_transform(X_test_lstat)

# fitting
lin_reg.fit(X_train_lstat_poly, y_train)
print(f'intercept : {lin_reg.intercept_}, coefficient : {lin_reg.coef_}')
# coefficient 계수가 작다 -> 직선에 가까운 직선이다.

# predict
y_pred_lstat_poly = lin_reg.predict(X_test_lstat_poly)  # polynomial 항을 넣는다~

# graph
plt.scatter(X_test_lstat, y_test)  # X_test_lstat: polynomial 항을 넣는 것이 아니야~~ 주의!
xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100, 1))  # 구간을 100개로 나누고, 1차원 리스트로 배열함
xs_poly = poly.fit_transform(xs)  # fit_transform 왜 나온거지? --> 그래프 만드는 때에도 만드는 객체인 거(그냥 컬럼 더해주는 역할일 뿐)
ys = lin_reg.predict(xs_poly)  # polynomial feature 를 만들었으므로 predict 다시 만들어야 함. ????? 다시 해보기~!!!
plt.plot(xs, ys, 'r')
plt.show()
# 이상하게 나오는 코드
# plt.plot(X_test_lstat, y_pred_lstat_poly, 'r')
# 이유 : plot은 점과 점사이를 직선으로 연결한다. X_test_lstat 가 랜덤하게 연결되어있으므로
mse = mean_squared_error(y_test, y_pred_lstat_poly)
rmse = np.sqrt(mse)
r2_6 = r2_score(y_test, y_pred_lstat_poly)
r2_7 = lin_reg.score(X_test_lstat_poly, y_test)  # predict 할 때 사용했던 x값, y 실제값
print('Price ~ LSTAT 2 : rmse is :', rmse)
print(f'Price ~ LSTAT 2 in train set : R^2 = {r2_6}, R^2 ={r2_7}')  # 결정계수(r2 score)도 커졌고, 오차(rmse) 적어졌다.


# 3-4. RM, LSTAT 두가지 변수를 합한 선형 회귀
# Price ~ RM, LSTAT 선형회귀
# price = b0 + b1 * rm + b2 * lstat
X_train_rm_lstat = X_train[:, [5, 12]]  # np.newaxis 필요 없다 : 이미 2차원 array 이기 때문!
X_test_rm_lstat = X_test[:, [5, 12]]
print('train set - rm and lstat : ', X_train_rm_lstat[:5])

lin_reg.fit(X_train_rm_lstat, y_train)  # fit/train
print(f'intercept : {lin_reg.intercept_}. coefficient : {lin_reg.coef_}')  # 계수 2개 (b1, b2)
# intercept : -0.6680381939230706. coefficient : [ 5.0114298 rm 양수,  -0.66908291 lstat ] -> 변수들 간의 상관관계가 있으면 값이 영향을 받는다.

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)  # 예측
print('실제값 : ', y_test[:5])
print('예측값 : ', y_pred_rm_lstat[:5])  # 실제값 예측값 그냥 비교

# 그래프는 3차원을 그려야 한다.
# x축 rm, z축 lstat, y축 price

# mse
mse = mean_squared_error(y_test, y_pred_rm_lstat)
print('rm, lstat mse : ', mse)
rmse = np.sqrt(mse)
print('rm, lstat rmse : ', rmse)
r2_8 = r2_score(y_test, y_pred_rm_lstat)
print('rm, lstat r2 score : ', r2_8)  # 결정계수가 너무 커지면 overfitting 의 문제점이 발생할 수 있다. (데이터에 과적합)


# 3-5. Price ~ RM + LSTAT + RM^2 + RM * LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 * rm^2 + b4 * rm * lstat + b5 * lstat^2
# 학습/검증세트에 다항식항(컬럼)을 추가
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
print('X trainset rm lstat - poly 객체 : \n', X_train_rm_lstat_poly[:2])
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)
print('X testset rm lstat - poly 객체 : \n', X_test_rm_lstat_poly[:2])
# fitting
lin_reg.fit(X_train_rm_lstat_poly, y_train)
print(f'intercept : {lin_reg.intercept_}, coefficient : {lin_reg.coef_}')  # 계수 5개
# price = b0 + b1 * rm + b2 * lstat + b3 * rm^2 + b4 * rm * lstat + b5 * lstat^2
#             [-1.76285033e+01  1.52009093e+00  2.09295492e+00 -3.53889752e-01 -3.14275848e-03] --> rm의 계수인 b1 부터 시작
# 해석 :       rm의 계수가 음수가 나왔다. (rm 에 반비례한다는 의미) -> 그러나 fit 함수는 price 의 오차만 줄이면 되기 때문에 rm의 계수는 관심 없음!
#             여기서 price는 과적합되었다고 말할 수 있다. (지금 trainset 에 너무 fit 되어있어 예측력 없어보임 -> R2 score 가 높아짐)
#             lstat 도 원래는 반비례였는데 정비례로 나와버림 !
#             why ? 추가되면서 두 개의 interaction 이 생겼기 때문에, b4가 다른 변수들에 영향을 주는 것이다. --> 다중공선성?
#             (https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91%EA%B3%B5%EC%84%A0%EC%84%B1 정리~)

# predict
y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)
print('y true : ', y_test[:5])
print('y prediction : ', y_pred_rm_lstat_poly[:5].round(2))  # .round(2) 반올림 소숫점 2자리 np.array 이면 ok!!
# 해석 : 실제값과 예측값의 차이 정말정말 적다! why? 제곱항을 넣어버렸기 때문.. -> 잘못된 모델이다!
mse = mean_squared_error(y_test, y_pred_rm_lstat_poly)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat_poly)
print(f'Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2: mse : {mse}, rmse : {rmse}, r2 score : {r2}')
#  rmse : 5.715001544053191, r2 score : 0.6303959336867977  --> 정확도가 좋아진 것 처럼 보여주지만 실제로는 너무 과적합.


# 3-6. Price ~ RM + LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 * lstat^2
# LSTAT + LSTAT^2 를 binomial 객체로 만들고 RM 을 bind 한다. np.c_[]
# LSTAT + LSTAT^2 다항식을 가진 binomial 객체 :  X_train_lstat_poly,  X_test_lstat_poly
X_train_last = np.c_[X_train_rm, X_train_lstat_poly]
X_test_last = np.c_[X_test_rm, X_test_lstat_poly]
print(f'X_train_last shape : \n', X_train_last.shape)
print(f'X_test_last shape : \n', X_test_last.shape)  # 행의 갯수 동일해야 함
print(f'X_train_last head(2) : \n', X_train_last[:2])  # 제곱해보면 진짜 잘됬는지 알 수 있다
print(f'X_test_last head(2) : \n', X_test_last[:2])
# fitting
lin_reg.fit(X_train_last, y_train)
print(f'Price ~ RM + LSTAT + LSTAT^2 : intercept : {lin_reg.intercept_}, coefficients : {lin_reg.coef_}')
# price = b0 + b1 * rm + b2 * lstat + b3 * lstat^2
#       [ 4.14148052 -1.79652146  0.03381396] --> rm 정비례, lstat 반비례 : 상식적인 그래프 도출되었다! (fitting 적절)
# prediction
y_pred_last = lin_reg.predict(X_test_last)
print('y true : ', y_test[:5])
print('y pred : ', y_pred_last[:5].round(2))
# mse, rmse, r2 score
mse = mean_squared_error(y_test, y_pred_last)
rmse = np.sqrt(mse)
r2_last = r2_score(y_test, y_pred_last)
print(f'Price ~ RM + LSTAT + LSTAT^2:  mse : {mse}, rmse : {rmse}, r2 score : {r2_last}')
# 해석 : 3-5, 3-6 두개의 모델이 거의 비슷한 결정계수 + 3-6 은 coef_가 상식적이므로 3-6 채택하자~~ (상식적으로 생각하쟈~~)

# cmd + pip install seaborn
# cmd + pip show seaborn -> location 디렉토리에 설치되어있는 거 찾아보기