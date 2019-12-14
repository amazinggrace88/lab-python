"""
데이터 전처리!
"""
import numpy as np
import pandas as pd
import os
from lab_python.scratch12.ex04 import separate_by_class2, summarize_dataset, summarize_by_class, calculate_probability, calculate_class_probability
from sklearn.metrics import confusion_matrix, classification_report

def train_test_split(df, test_size):
    """
    train set, test set 으로 df 를 나누자
    대신 data 와 class 가 같이 있어야 한다~
    """
    test_index = int(test_size*len(df))
    trainset = df.iloc[test_index:, :]
    testset = df.iloc[:test_index, :]
    return trainset, testset

# 오쌤 정답
def train_test_split(df, test_size):
    """df=데이터 프레임, test_size=테스트 세트의 비율
    학습 세트(X_train)와 검증 세트(X_test)를 리턴
    train/test set: 리스트 또는 np.ndarray
    [[x1, x2, ..., lable1], [x1, x2, ..., label2], [], ...], [[], [], [], ...]
    """
    # DataFrame을 numpy.ndarray 타입으로 변환
    array = df.to_numpy()
    # array의 순서를 무작위로 섞음.
    np.random.shuffle(array)
    # 학습 세트/테스트 세트를 나누기 위한 인덱스
    cut = int(len(array) * (1-test_size))
    # 학습 세트/테스트 세트 나눔
    train_set = array[:cut]
    test_set = array[cut:]
    # 결과 리턴
    return train_set, test_set
    

def predict(summaries, X_test):
    """테스트 세트의 예측값들의 배열(리스트)을 리턴 [2, 1, 0, 2, 1, 0..  ]"""
    # list making
    prediction_list = []
    for i in range(len(X_test)):
        # vote
        dict_for_vote = calculate_class_probability(summaries, X_test[i])
        for key, value in dict_for_vote.items():
            max_value = max(value)
            if value == max_value:
                prediction_list.append(key)
    return prediction_list

# 오쌤 정답
def predict(summaries, X_test):
    """테스트 세트의 예측값들의 배열(리스트)을 리턴 [2, 1, 0, 2, 1, 0..  ]"""
    predicts = []
    # X_test 의 원소 갯수만큼 반복하면서
    for test in X_test:
        # 각 원소(예측값을 찾으려는 데이터)의 클래스에 속할 확률을 계산
        probabilities = calculate_class_probability(summaries, test)
        # 각 클래스에 속할 확률들 중에서 최댓값을 찾음
        best_label, best_prob = None, -1  # 확률이 0 보다 작아지는 경우는 없으므로
        for k, v in probabilities.items():
            if v > best_prob:  # 더 큰 확률값을 찾을 경우
                best_prob = v
                best_label = k
        # 확률 최댓값의 키값을 예측값 리스트에 추가
        predicts.append(best_label)
    return predicts

# 오쌤 정답2
def predict(summaries, X_test):
    """테스트 세트의 예측값들의 배열(리스트)을 리턴 [2, 1, 0, 2, 1, 0..  ]"""
    # X_test 의 원소 갯수만큼 반복하면서
    predicts = []
    for test in X_test:
        # 각 원소(예측값을 찾으려는 데이터)의 클래스에 속할 확률을 계산
        probabilities = calculate_class_probability(summaries, test)
        # 각 클래스에 속할 확률들 중에서 최댓값을 찾음
        best_label, _ = sorted(probabilities.items(), key=lambda x: -x[1])[0]
        # sorted(dict) : dict 의 키들을 오름차순 정렬한 리스트를 보여줌
        # sorted(dict.values()) : dict 의 값들을 오름차순 정렬한 리스트를 보여줌
        # sorted(dict.items()) : (key, value) 튜플을 기본값 key 값을 기준으로 정렬
        # value 를 기준으로 하고 싶다 : sorted(Iterable, key=정렬기준함수)
        # key=lambda x: x[1] 확률값을 기준으로 정렬함! (작은 값부터 정렬됨, 오름차순)
        # key=lambda x: -x[1] 원래 제일 큰 값이었던 것이 제일 작은 것으로 변함(내림차순 정렬로 변함)
        predicts.append(best_label)
    return predicts


# 1)
# iris_dataset Class -> 0, 1, 2 로 나누기
def class_index_number(df):
    """
    class 문자열을 숫자로 바꾼 리스트를 리턴
    : [iris-setosa, ..] = [0, 1, 2]
    """
    class_index = []
    for i in range(len(df)):
        if df.iloc[i, 4] == "Iris-setosa":
            class_index.append(0)
        if df.iloc[i, 4] == "Iris-versicolor":
            class_index.append(1)
        if df.iloc[i, 4] == "Iris-virginica":
            class_index.append(2)
    return class_index


# 2) cancer_dataset Class -> 0, 1 로 나누기
def diagnosis_index_number(df):
    """
    class 문자열을 숫자로 바꾼 리스트를 리턴
    :
    """
    class_index = []
    for i in range(len(df)):
        if df.iloc[i, 1] == "B":
            class_index.append(0)
        if df.iloc[i, 1] == "M":
            class_index.append(1)
    return class_index


if __name__ == '__main__':
    # bring the iris_dataset
    col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']  # csv file's col-name
    iris_dataset = pd.read_csv('iris.csv', header=None, names=col_names)
    print(iris_dataset.head())

    # 전처리
    # if. Class 를 모를 때는?
    class_index = class_index_number(iris_dataset)
    print(class_index)
    iris_dataset.iloc[:, -1] = class_index  # 제일 마지막 열 ~
    print(iris_dataset.head())

    iris_train, iris_test = train_test_split(iris_dataset, 0.2)
    print(iris_train.shape)  # (120, 5)
    print(iris_test.shape)  # (30, 5)

    # summaries - train dataset 의 각 컬럼의 평균과 표준편차들을 계산
    # iris_dataset -> iris_nparray -> 통계량 : iris_summary
    iris_train_nparray = iris_train.values
    print(type(iris_train_nparray))  # <class 'numpy.ndarray'>
    iris_summary = summarize_by_class(iris_train_nparray)
    print(iris_summary)


    # 오쌤 정답
    # 중복되는 값 append 안되는 데이터 타입: set - 마지막 컬럼을 set 에다 넣어서 출력해봐요~
    species = set(iris_dataset.iloc[:, -1])
    print('species : \n', species)
    # 1) iris_dataset Class -> 0, 1, 2 로 나누기
    iris_dataset.loc[iris_dataset['Class'] == 'Iris-setosa', 'Class'] = 0  # boolean 인덱싱 사용할 때는 loc 씀!
    print(iris_dataset)
    iris_train, iris_test = train_test_split(iris_dataset, test_size=0.2)
    print('Train set:', iris_train.shape)
    print('Test set:', iris_test.shape)
    # array 이므로 .head() 안됨!
    model = summarize_by_class(iris_train)
    iris_pred = predict(model, iris_test)
    print(iris_pred)
    print(iris_test[:, -1] == iris_pred)
    print(confusion_matrix(iris_test[:, -1], iris_pred))
    print(classification_report(iris_test[:, -1], iris_pred))


    # bring the cancer_dataset
    cancer_dataset = pd.read_csv('wisc_bc_data.csv')
    print(cancer_dataset.head())
    # diagnosis를 숫자로 변환
    diagnosis = cancer_dataset.iloc[:, 1]
    print(diagnosis)
    diagnosis_index = diagnosis_index_number(cancer_dataset)
    print(diagnosis_index)

    # id, diagnosis 삭제
    print(cancer_dataset.shape)  # (569, 32)
    del cancer_dataset["diagnosis"]
    print(cancer_dataset)
    cancer_dataset["diagnosis"] = diagnosis_index
    print(cancer_dataset.head())

    del cancer_dataset["id"]
    print(cancer_dataset.head())

    cancer_train, cancer_test = train_test_split(cancer_dataset, 0.2)
    print(cancer_train.shape)  # (456, 32)
    print(cancer_test.shape)  # (113, 32)
    # cancer_dataset -> cancer_nparray -> 통계량 : cancer_summary
    cancer_train_nparray = cancer_train.values
    print(type(cancer_train_nparray))  # <class 'numpy.ndarray'>
    cancer_summary = summarize_by_class(cancer_train_nparray)
    print(cancer_train_nparray)

    # iris_summary : iris_train (np.ndarray 형태) 의 평균, 표준편차, 갯수
    # cancer_summary : cancer_train (np.ndarray 형태) 의 평균, 표준편차, 갯수

    # 오쌤 정답
    cancer_dataset = pd.read_csv('wisc_bc_data.csv')
    print(cancer_dataset.head())
    cancer_dataset.info()

    # id, diagnosis 삭제
    # 1
    ret = cancer_dataset.drop(columns='id', axis=1)  # 지우는 방법은 여러가지~ (함수 도움말을 보자 - columns(컬럼이름), index(row 방향), axis=1컬럼방향,  inplace(원본 바꿀지말지)..)
    ret = cancer_dataset.drop(columns=['id'])  # 같은 결과, 원본 변경되지 않았음.
    print(ret.head())
    # 2
    del cancer_dataset["diagnosis"]  # 원본 변경
    print(cancer_dataset)
    # 3
    diagnosis = set(cancer_dataset['diagnosis'])  # 컬럼만 뽑아냄!
    print(diagnosis)  # {'M', 'B'}
    # B 가 종양이 아닌 경우 = 0, M 이 종양인 경우 = 1
    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'B', 'Class'] = 0  # 새로운 컬럼 추가!
    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'M', 'Class'] = 1
    print(cancer_dataset.tail())

    # diagnosis 컬럼을 데이터 프레임의 마지막으로 옮김
    column_names = cancer_dataset.columns.tolist()  # .tolist() : 리스트 바로 만들어준다.
    # [name for name in cancer_dataset.columns]
    print(column_names)
    column_names.remove('diagnosis')
    column_names.append('diagnosis')
    print(column_names)
    # 방법1
    # df = cancer_dataset.reindex(columns=column_names)
    # print(df.head())
    # 방법2
    # cancer_dataset[['diagnosis', 'radius_mean']]  # ['diagnosis', 'radius_mean'] col 만 뽑는다(select ['', ''] 순서대로)
    df = cancer_dataset[column_names]  # 컬럼의 순서는 diagnosis 가 제일 마지막
    print(df.head())
    # 4
    df = cancer_dataset.loc[:, ::-1].head()  # ::-1 컬럼번호를 모두 바꿔버린다 (좌우 반전-> 제일 마지막이 제일 처음으로!) -> 행에도 올 수 있음(오름차순을 내림차순으로)
    print(df.head())
    # enumerate ?

    # predict
    cancer_train, cancer_test = train_test_split(df, test_size=0.2)
    model = summarize_by_class(cancer_train)
    predicts = predict(model, cancer_test)
    print(confusion_matrix(cancer_test[:, -1], predicts))
    print(classification_report(cancer_test[:, -1], predicts))


# multinomial naive bayes 예제 찾아보기