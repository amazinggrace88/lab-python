"""
Logistic Regression (로지스틱 회귀)

***** 선형회귀와의 구분 *****
Linear Regression : 값을 예측하기 위한 목적
Logistic Regression : 분류하기 위한 목적

cf.
(확률을 사용하지만, 오늘은 class만 소개함)
. ~ 안에 있는
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# from sklearn import datasets 라고 해도 되요~ 개발자마다 다르므로 모두 알아두기
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris['data']  # X = iris.data 으로 써도 됨
y = iris['target']  # y = iris.target 으로 써도 됨
features = iris['feature_names']  # iris.feature_names 으로 써도 됨
print(features)  # column 으로 부적합(공백, 괄호 등)


# DataFrame 으로 변환
iris_df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# DataFrame 에 꼭 target 추가해야 함!
iris_df['species'] = y
print(iris_df.iloc[:5, :])  # scikit-learn datasets은 숫자로 되어 있음 -> 0, 1, 2
print(iris_df.describe())  # count    150.000000   150.000000    150.000000   150.000000  150.000000 이므로 각 컬럼 null 없음

sns.pairplot(iris_df, hue="species", vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])  # target을 빼버리고 x만 가지고 그린 것~
plt.show()
# 해석
# petal_length, petal_width 비례관계
# petal_length, petal_width 만 있어도 price 예측 가능(클래스끼리 가로로 겹치는 부분 적다-구분가능)


# 데이터(X)와 타겟(y)을 학습세트, 검증세트로 분리
# ndarray 타입을 써주어야 한다~ why?
# 순서가 있으므로, shuffle - split 한다.
# random_state=1217 : set.seed 와 똑같은 역할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1217)
# 분류 알고리즘 중에서 Logistic Regression 선택
log_reg = LogisticRegression()  # 2 개 보면 그 앞 패키지를 보고 선택 (linear_model)
# fitting
log_reg.fit(X_train, y_train)
# prediction
predictions = log_reg.predict(X_test)
print('true : ', y_test)
print('pred : ', predictions)  # 관계식을 찾으려고 하는 게 아니라, 분류를 하려고 해요~!
# 성능 측정 : confusion matrix
print('confusion matrix : \n', confusion_matrix(y_test, predictions))
print('classification report : \n', classification_report(y_test, predictions))
#  0 [[ 9  0  0]
#  1  [ 0 11  1] 1번을 2번이라고 예측
#  2  [ 0  1  8]] : 2번을 1번이라고 예측

# SGDClassifier - stochastic gradient decent 로 해보기!
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html