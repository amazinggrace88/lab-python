"""
R 을 활용한 머신러닝 - 암 데이터 파일(csv)
scikit learn 패키지를 활용하여 kNN 수행하고 예측결과를 알아보기!
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report



if __name__ == '__main__':
    # 1. data preparation
    dataset = pd.read_csv('wisc_bc_data.csv')  # , header=0 여쭙기
    print(dataset.shape)  # (569, 32)
    print(dataset.info())  # dtype : float / id int
    print(dataset.describe())  # mean 보고 scaling 필요 유무 판단하기~
    print(dataset.head())

    # 2. data 전처리
    # : NA 처리(없음)
    # : 학습 세트(training set)와 검증 세트(test set)로 나누기
    # 순서 1) 데이터 세트를 데이터(포인트)와 레이블로 구분
    X = dataset.iloc[:, 2:].to_numpy()  # id - 필요없는 변수!~
    y = dataset.iloc[:, 1].to_numpy()
    print(X[0])
    print(y[0])  # Dataset 의 Class 를 label 이라고 부른다(답지)
    # 순서 2) 학습 세트(training set)와 검증 세트(test set)로 구분
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 3. 표준화 (or 정규화) : 거리 계산을 위해서 각 특성(변수)들을 스케일링 - z-score 표준화 선택
    # Z-score 표준화: 평균을 0, 표준편차 1 로 변환
    scaler = StandardScaler()  # 메소드(method): StandardScaler()
    scaler.fit(X_train)  # X_train 세트의 평균/표준편차 계산
    X_train = scaler.transform(X_train)  # 똑같은 변수에 저장
    X_test = scaler.transform(X_test)
    print(np.mean(X_train[:, 0]))  # -2.982717857806135e-15 => 표준화된 X_train 의 평균을 구함
    print(np.mean(X_test[:, 0]))  # 0.04153666561804639 => X_test 는 X_train 의 표준화를 따르기 때문에 평균이 0이 아니다
    print(np.std(X_train[:, 0]))  # 0.9999999999999999

    # 4. 학습/예측
    # k-nn 분류기 생성 (KNN은 학습이 큰 의미가 없다.. 그냥 알고리즘 그림처럼 만들어주는 것 뿐!)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(y_pred)

    # 5. 모델 평가
    # 혼동행렬 만들기
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    # [[68  1 암이 아닌데 암이라고 하는 비율]
    #  [ 1 암인데 암이 아니라고 하는 비율 44]]
    report = classification_report(y_test, y_pred)
    print(report)
    # accuarcy  : 정확도 : (TP + TN) / (TP + FP + FN + TN)
    # precision : 정밀도 : TP / (TP + FP)
    # recall    : 재현율 : TP / (TP + FN) 정밀도와 반비례관계!
    # precision : 0.99(B) / 1(M)
    # recall    : 1(B) / 0.97(M)
    #               precision    recall  f1-score   support
    #            B       0.99      0.99      0.99        69 -> B를 positive로 두고 계산한 결과!
    #            M       0.98      0.98      0.98        45 -> M을 positive로 두고 계산한 결과!

    # 6. 성능 개선 - knn 에서 조작 가능한 값 - k 값 (이웃의 수) 의 변화(1~30)에 따른 error 감소율 분석
    errors = []
    for i in range(1, 31):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        i_pred = knn.predict(X_test)
        errors.append(np.mean(i_pred != y_test))
    print(errors)  # 1, 2종 오류 모두 error 에 들어감 -> FN을 줄여주는 방향 - 즉, recall 을 높이는 방향으로 혼동행렬 보면서 error 계산
    plt.plot(range(1, 31), errors, marker='*')
    plt.title('Mean Error with K-value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()
    
