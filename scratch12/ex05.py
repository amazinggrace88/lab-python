"""
데이터 전처리!
"""

import pandas as pd
import os
from lab_python.scratch12.ex04 import separate_by_class2, summarize_dataset, summarize_by_class, calculate_probability, calculate_class_probability


def train_test_split(df, test_size):
    """
    train set, test set 으로 df 를 나누자
    대신 data 와 class 가 같이 있어야 한다~
    """
    test_index = int(test_size*len(df))
    trainset = df.iloc[test_index:, :]
    testset = df.iloc[:test_index, :]
    return trainset, testset


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
    # bring the cancer_dataset
    cancer_dataset = pd.read_csv('wisc_bc_data.csv')
    print(cancer_dataset.head())

    # 전처리
    # 1) iris_dataset Class -> 0, 1, 2 로 나누기
    class_index = class_index_number(iris_dataset)
    print(class_index)
    iris_dataset.iloc[:,4] = class_index
    print(iris_dataset.head())
    # 2) cancer_dataset diagnosis 맨 뒤로 보내기
    diagnosis = cancer_dataset.iloc[:, 1]
    print(diagnosis)
    diagnosis_index = diagnosis_index_number(cancer_dataset)
    print(diagnosis_index)
    # 3) diagnosis index 를 cancer_dataset 맨 뒤에 붙이기
    print(cancer_dataset.shape)  # (569, 32)
    del cancer_dataset["diagnosis"]
    print(cancer_dataset)
    cancer_dataset["diagnosis"] = diagnosis_index
    print(cancer_dataset.head())
    # 4) id 를 cancer_dataset 에서 삭제
    del cancer_dataset["id"]
    print(cancer_dataset.head())

    # split
    # iris_dataset
    iris_train, iris_test = train_test_split(iris_dataset, 0.2)
    print(iris_train.shape)  # (120, 5)
    print(iris_test.shape)  # (30, 5)
    # cancer_dataset
    cancer_train, cancer_test = train_test_split(cancer_dataset, 0.2)
    print(cancer_train.shape)  # (456, 32)
    print(cancer_test.shape)  # (113, 32)

    # summaries - train dataset 의 각 컬럼의 평균과 표준편차들을 계산
    # iris_dataset -> iris_nparray -> 통계량 : iris_summary
    iris_train_nparray = iris_train.values
    print(type(iris_train_nparray))  # <class 'numpy.ndarray'>
    iris_summary = summarize_by_class(iris_train_nparray)
    print(iris_summary)
    # cancer_dataset -> cancer_nparray -> 통계량 : cancer_summary
    cancer_train_nparray = cancer_train.values
    print(type(cancer_train_nparray))  # <class 'numpy.ndarray'>
    cancer_summary = summarize_by_class(cancer_train_nparray)
    print(cancer_train_nparray)
    
    # iris_summary : iris_train (np.ndarray 형태) 의 평균, 표준편차, 갯수
    # cancer_summary : cancer_train (np.ndarray 형태) 의 평균, 표준편차, 갯수

    # test
    iris_test_nparray = iris_test.values
    print('test\n', iris_test_nparray[0])
    print(predict(iris_summary, iris_test_nparray))
