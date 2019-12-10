"""
scikit-learn 패키지를 이용한 knn(k nearest neighbor)
# scikit-learn 소개
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler  # class 를 import 하겠다는 의미
from sklearn.metrics import confusion_matrix, classification_report

if __name__ == '__main__':  # main 이라고 치고 enter

    # 1. data preparation
    col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']  # csv file's col-name
    # csv file 에서 DataFrame 생성
    dataset = pd.read_csv('iris.csv', header=None, names=col_names)
    # DataFrame 확인
    print(dataset.shape)  # 150 행, 5 열
    print(dataset.info())  # 행/열 정보와 dtype 정보, column dtype 리턴 cf. object : 문자열
    print(dataset.describe())  # 요약된 통계 정보 리턴 (문자열 제외, 숫자열에만 대해 정보를 제공~)
    print(dataset.head())  # (=dataset.iloc[0:5] =dataset.iloc[:5])
    print(dataset.tail())  # (=dataset.iloc[-1:]) np.array 또한 마찬가지 - 마지막 행~ (종이 필기 보기)

    # 2. data 전처리
    # : NA 처리(없음) --> 있으면 해야한다~
    # : 학습 세트(training set)와 검증 세트(test set)로 나누기
    # 순서 1) 데이터 세트를 데이터(포인트)와 레이블로 구분 -> pd에서 np.ndarray 로 변환
    # Dataset 의 Class 를 label 이라고 부른다(답지)
    # 순서 2) 학습 세트(training set)와 검증 세트(test set)로 구분

    # 순서 1) 데이터 세트를 데이터(포인트)와 레이블로 구분하여 np.ndarray 로 생성 - why? scikit-learn 이 array 타입을 사용하기 때문에 (.to_numpy())
    X = dataset.iloc[:, :-1].to_numpy()  # pd.DataFrame 의 :-1(0:-1인데 0 생략) - col 0~-1까지 (마지막 열 제외) 즉, 4차원 공간의 vector(점)
    print(X)
    y = dataset.iloc[:, 4].to_numpy()  # 전체 행, 마지막 열 데이터 즉, label
    print(y)

    # 순서 2) 학습 세트(training set)와 검증 세트(test set)로 구분
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 순서 있음.(지켜야되~)
    # 과정 : shuffle 할 때, X, y 같이 shuffle 시켜준다.(인덱스만 셔플하여 X, y 를 똑같이 선택)
    print(len(X_train), len(X_test), len(y_train), len(y_test))  # 120 30 120 30
    print(X_train[:3])  # [[]]
    print(y_train[:3])  # []

    # 3. 표준화 (or 정규화) : 거리 계산을 위해서 각 특성(변수)들을 스케일링 - z-score 표준화 선택
    # Z-score 표준화: 평균을 0, 표준편차 1 로 변환
    scaler = StandardScaler()  # Scaler 객체 생성 : copy: Any = True 이므로 () 안에 아무것도 넣지 마
    scaler.fit(X_train)  # 컬럼 당 평균과 표준편차 계산함. 4개 변수에 대해 평균, 표준편차 계산
    X_train = scaler.transform(X_train)  # 스케일링(표준화) 수행 : z-score 공식 데이터 하나에 대입 (Perform standardization by centering and scaling)
    X_test = scaler.transform(X_test)
    # ***** train set 의 각 컬럼의 평균, 표준편차를 가지고 test 에 적용함. - test 의 평균과 표준편차를 가지고 하지 않아~
    # 가정 : test set 은 train set 의 분포를 따른다.

    # 스케일링(z-score 표준화 수행 결과 확인)
    for col in range(4):
        print(f'train 평균 = {X_train[:, col].mean()}, 표준편차 = {X_train[:, col].std()}')  # 왜 평균 0 이 아니지..? e-16 잊지 말자! (자연로그)
        # array 의 mean/std 를 호출해주면 numpy 패키지가 계산한다.
        print(f'test 평균 = {X_test[:, col].mean()}, 표준편차 = {X_test[:, col].std()}')
        # 완전하게 0, 1 이 아니다 - train set 의 평균, 표준편차 를 가지고 계산했기 때문
        
    # 4. 학습/예측
    # k-nn 분류기 생성
    classifier = KNeighborsClassifier(n_neighbors=5)  # 분류기 생성 # n_neighbors= : 최단거리 5개를 뽑아서 다수인 label 을 따른다.(홀수로 선택하는 것이 좋다)
    # 분류기 학습 (정답지를 주고 학습하라고 시킨다 - knn 알고리즘의 그림을 그렸다 (label을 준다))
    classifier.fit(X_train, y_train)  # 분류기 학습
    # 예측 (5개 중 다수인 것을 선택)
    y_pred = classifier.predict(X_test)  # X_train, y_train 를 학습지로 주고 X_train 만 정답지를 주었음.
    print(y_pred)

    # 5. 모델 평가
    # 혼동행렬 만들기
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)  # 대각선 : 맞춘 것, 대각선 이외 : 틀린 것
    report = classification_report(y_test, y_pred)
    print(report)
    # accuarcy  : 정확도 : (TP + TN) / (TP + FP + FN + TN)
    # precision : 정밀도 : TP / (TP + FP)
    # recall    : 재현율 : TP / (TP + FN) 정밀도와 반비례관계!
    # f1-score  :
    # support   :
    # accuracy  :전체 - 틀린 갯수 (즉, 맞은 갯수) / 전체 갯수
    # macro avg :
    # weighted avg :
    #                  precision    recall  f1-score   support
    #
    #     Iris-setosa       1.00      1.00      1.00         9 -> Iris-setosa 를 positive 로 두고 계산한 결과!
    # Iris-versicolor       0.89      0.89      0.89         9 ->
    #  Iris-virginica       0.92      0.92      0.92        12 ->

    # 6. 성능 개선 - knn 에서 조작 가능한 값 - k 값 (이웃의 수) 의 변화에 따른 error 감소율 분석
    errors = []
    for i in range(1, 31):
        knn = KNeighborsClassifier(n_neighbors=i)  # 이웃의 수 i
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != y_test))
        # 예측한 i 와 실제 label 을 비교하여 error 의 평균을 계산함
        # pred_i != y_test 가 True(1), False(0)로 만들어지는 boolean 이고,
        # numpy 는 True, False를 1, 0으로 자동으로 변환하여 np.mean()을 계산한다. - numpy는 np.array 만 특별취급! (list는 [] == [] 똑같은지 전체 비교!)
        # 즉, i 마다 error 의 평균을 계산하는 것이다.
    print(errors)  # [] 형태를 출력 - 목적 : error 가 가장 적을 때의 k값(=i)를 찾기
    # graph 로 나타내기
    plt.plot(range(1, 31), errors, marker='o')
    plt.title('Mean Error with K-value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()
