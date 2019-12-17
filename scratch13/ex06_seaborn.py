"""
seaborn 을 이용한 데이터 탐색 과정
seaborn - dataframe 으로 사용하는 것이 편하다.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()   # array 형태이므로 DataFrame 으로 만들어주는 과정 필요해요
X = boston['data']  # boston.data
y = boston['target']  # boston.target
features = boston['feature_names']  # boston.feature_names

# DataFrame 만들기 (numpy.ndarray -> pandas.DataFrame)
boston_df = pd.DataFrame(X, columns=features)
# DataFrame에 target column 추가
boston_df['Price'] = y
print(boston_df.head())
# null 확인
print('shape : \n', boston_df.shape)
print('discribe : \n', boston_df.describe())
# shape 의 row 값과, describe - count 의 row 갯수가 다르다면, 값 중에 null 이 있는 것이다

# 전체 DataFrame 에서 특정 column 만 추출하기
columns = ['LSTAT', 'INDUS', 'NOX', 'RM', 'Price']
subset_df = boston_df[columns]
print('특정 column 만 추출 : \n', subset_df.head())

"""
# seaborn 
전체 데이터에 대한 경향성 보기 위한 최고의 라이브러리
전체 변수의 서로에 대한 상관성을 보여줌
특정 column 의 변수별 그래프
"""
sns.pairplot(subset_df)
plt.show()
# 대각선 histogram
# x 축의 모든 x 는 ~다.
# y 축의 모든 y 는 ~다.
# 전체 column 의 변수별 그래프
# sns.pairplot(boston_df)
# plt.show()

# 상관 행렬 - 상관 계수로 이루어진 행렬
# 상관 계수 - correlation coefficient : 변수들간의 관계
# 상관 계수를 만들고 상관 행렬을 만든다.
corr_matrix = subset_df.corr().round(2)  # 상관계수 계산하는 함수 DataFrame.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()
# 상관 계수가 클 수록 아주 진하거나(반비례) 연한 색(비례)으로 표시됨 (heatmap)
# 두개의 변수가 같은 방향으로 편차가 생기는지, 다른 방향으로 편차가 생기는지 계산한다. (같은 변수는 공분산 1)
# 상관관계가 인과관계는 아니다. 서로 같이 움직이는 경향인 것일 뿐 원인과 결과는 아니다.

# interactive graph etc.. important ! https://seaborn.pydata.org/#

