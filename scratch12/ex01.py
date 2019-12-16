"""
Naive Bayes 알고리즘
iris 품종 분류
"""
from sklearn import datasets  # 사이킷런 안의 모듈 이름 dataset
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler  # class
# iris 품종 분류

iris = datasets.load_iris()  # scikit-learn 패키지 안 파일 # 1
print(type(iris))  # <class 'sklearn.utils.Bunch'> : Bunch - 사이킷런에서 사용,, bunch 뭐지?
print(iris)

# Bunch 클래스 - sample dataset 의 형식
# {'data': [], 'target': []} 으로 이루어진 dict 와 비슷한 클래스 (np.array 를 value 로, 'data'를 key 로 가지는 dict 와 비슷,,)
# {'data': array([[5.1, 3.5, 1.4, 0.2],  -> 특성(변수)들 : n 차원 공간의 점(point)
# 'target': array([0, 0, 0, 0,...        -> label(분류 클래스) : 0, 1, 2 라고 숫자로 변환되어서 저장됨(붓꽃 종류)
# bunch라는 객체는 data 와 target 을 가지고 있다.
# point, label 을 data, target 으로 미리 분류해놓은 객체라고 볼 수 있다

# Bunch 클래스 보충
# data: (필수) 독립 변수 ndarray 배열
# target: (필수) 종속 변수 ndarray 배열
# feature_names: (옵션) 독립 변수 이름 리스트
# target_names: (옵션) 종속 변수 이름 리스트
# DESCR: (옵션) 자료에 대한 설명
print('data shape : \n', iris.data.shape)
print('iris target : \n', iris.target_names)
#  ['setosa' 'versicolor' 'virginica'] 이 0, 1, 2 라고 숫자로 변환되어서 저장됨 -
print('iris features : \n', iris.feature_names)
#  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] 즉, 변수 이름들(column)

X = iris.data  # 2
print(type(X))  # np.ndarray
print(X[:5])
y = iris.target  # 3
print(type(y))  # np.ndarray
print(y[:5])

# 3줄 1번에 출력(feature name 없음)
# return_X_y=False => bunch 를 리턴, return_X_y=True => np.ndarray 들의 tuple(data, target)을 리턴(feature name 없음)
X, y = datasets.load_iris(return_X_y=True)

# training / test set split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 데이터들 변환(scaling)
scaler = StandardScaler()  # 생성자 호출
scaler.fit(X_train, y_train)  # 학습 데이터의 평균과 표준편차를 변환할 때 이용
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

# 머신러닝 모델 선택 - Naive Bayes
gnb = GaussianNB()  # Gaussian Naive Bayes 모델 선택 - 정규 분포(연속) <-> 베르누이 나이브 베이즈 - 이항분포 (자료의 형태에 따라 선택)
gnb.fit(X_train_transformed, y_train)  # 학습
y_pred = gnb.predict(X_test_transformed)  # 예측

# 성능 측정
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""
Naive Bayes 알고리즘
iris 품종 분류
"""
from sklearn import datasets  # 사이킷런 안의 모듈 이름 dataset
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler  # class
# iris 품종 분류

iris = datasets.load_iris()  # scikit-learn 패키지 안 파일 # 1
print(type(iris))  # <class 'sklearn.utils.Bunch'> : Bunch - 사이킷런에서 사용,, bunch 뭐지?
print(iris)

# Bunch 클래스 - sample dataset 의 형식
# {'data': [], 'target': []} 으로 이루어진 dict 와 비슷한 클래스 (np.array 를 value 로, 'data'를 key 로 가지는 dict 와 비슷,,)
# {'data': array([[5.1, 3.5, 1.4, 0.2],  -> 특성(변수)들 : n 차원 공간의 점(point)
# 'target': array([0, 0, 0, 0,...        -> label(분류 클래스) : 0, 1, 2 라고 숫자로 변환되어서 저장됨(붓꽃 종류)
# bunch라는 객체는 data 와 target 을 가지고 있다.
# point, label 을 data, target 으로 미리 분류해놓은 객체라고 볼 수 있다

# Bunch 클래스 보충
# data: (필수) 독립 변수 ndarray 배열
# target: (필수) 종속 변수 ndarray 배열
# feature_names: (옵션) 독립 변수 이름 리스트
# target_names: (옵션) 종속 변수 이름 리스트
# DESCR: (옵션) 자료에 대한 설명
print('data shape : \n', iris.data.shape)
print('iris target : \n', iris.target_names)
#  ['setosa' 'versicolor' 'virginica'] 이 0, 1, 2 라고 숫자로 변환되어서 저장됨 -
print('iris features : \n', iris.feature_names)
#  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] 즉, 변수 이름들(column)

X = iris.data  # 2
print(type(X))  # np.ndarray
print(X[:5])
y = iris.target  # 3
print(type(y))  # np.ndarray
print(y[:5])

# 3줄 1번에 출력(feature name 없음)
# return_X_y=False => bunch 를 리턴, return_X_y=True => np.ndarray 들의 tuple(data, target)을 리턴(feature name 없음)
X, y = datasets.load_iris(return_X_y=True)

# training / test set split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 데이터들 변환(scaling)
scaler = StandardScaler()  # 생성자 호출
scaler.fit(X_train, y_train)  # 학습 데이터의 평균과 표준편차를 변환할 때 이용
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

# 머신러닝 모델 선택 - Naive Bayes
gnb = GaussianNB()  # Gaussian Naive Bayes 모델 선택 - 정규 분포(연속) <-> 베르누이 나이브 베이즈 - 이항분포 (자료의 형태에 따라 선택)
gnb.fit(X_train_transformed, y_train)  # 학습
y_pred = gnb.predict(X_test_transformed)  # 예측

# 성능 측정
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
