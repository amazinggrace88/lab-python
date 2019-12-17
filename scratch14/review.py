# review
# sklearn.linear_model 구현 - with boston
# 1. SGDClassifier : stochastic gradient descent classifier
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
# bring the data
boston = load_boston()
X = boston.data
y = boston.target
print('X is : \n', X[:1])
print('y is : \n', y[:1])
features = boston.feature_names
print(features, len(features))  # 13 columns

# 1. make graph
# sns.pairplot - 변수간의 관계, 경향성 check
# seaborn 쓸 때는 DataFrame 으로 변환하기
# why ? pairplot은 데이터프레임을 인수로 받아 그리드(grid) 형태로 각 데이터 열의 조합에 대해 스캐터 플롯을 그린다.
# 출처 : https://datascienceschool.net/view-notebook/4c2d5ff1caab4b21a708cc662137bc65/
boston_df = pd.DataFrame(X, columns=features)
boston_df['Price'] = y
print(boston_df.iloc[:5, :])  # DataFrame 확인
print(boston_df.describe())  # count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  506.000000 null x
# sns.pairplot(boston_df)
# plt.show()

# 2. modeling
# model - SGDClassifier