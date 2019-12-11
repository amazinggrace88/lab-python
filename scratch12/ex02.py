"""
scikit-learn 패키지에 포함된 위스콘신 대학 암 데이터를 로딩해서
naive bayes 모델로 예측 결과를 분석.
"""
from sklearn import datasets  # 사이킷런 안의 모듈 이름 dataset
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler  # class
# bring the data!
cancer = datasets.load_breast_cancer()
print('data shape : \n', cancer.data.shape)  #  (569, 30)
print('cancer targets : \n', cancer.target_names)  #  ['malignant' 'benign']
X = cancer.data
y = cancer.target
print(X[:5])  # 소수점으로 나와 있음
print(y[:5])  # index 로 저장
# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# scaling
scaler = StandardScaler()
scaler.fit(X_train, y_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)
# fit
gnb = GaussianNB()
gnb.fit(X_train_transformed, y_train)
# predict
y_pred = gnb.predict(X_test_transformed)
# evaluation
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
# confusion_matrix
# [[37  7]
#  [ 3 67]]
