"""
2. 연속 확률 변수(연속형 변수)에서의 나이브 베이즈 원리 구현
"""
# - 산술연산(numerical operator) : +,-,*,**(거듭제곱),/(소수점까지 나누기),//(몫만 반환),%(나머지)
import random
from collections import defaultdict  # 기본 패키지 collections
from math import exp, pi, sqrt

import numpy as np
import pandas as pd


# 부분집합으로 나누는 함수
# why? Class 별로 평균, 표준편차 계산하기 위해
from sklearn.datasets import load_iris


def separate_by_class(dataset):
    """
    dataset 를 Class 별로 구분한 사전(dict)를 리턴
        {class_0: [[], [], ..],
         class_1: [[], [], ..], .. }
    dataset : list 로 가정
    """
    separated = dict()  # 빈 dict 생성 {} 는 set, dict 모두 다 해당되므로
    for i in range(len(dataset)):
        vector = dataset[i]  # row 전체 - 리스트로 가정
        class_value = vector[-1]  # row 의 Class : 가장 마지막 원소
        if class_value not in separated:
            # Class 값이 separated 라는 dict 에 없으면
            separated[class_value] = []  # 비어있는 리스트 생성
        separated[class_value].append(vector)  # 0, 1 따로따로 list 에 넣는다.
    return separated


def separate_by_class2(dataset):
    """dataset : list 로 가정"""
    separated = defaultdict(list)
    # defaultdict 객체 생성 -> key 값이 없으면 자동으로 비어있는 리스트 생성해주는 객체다~ (안에 value 의 datatype 설정해줘야 되요~ ex_list )
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]  # 리스트의 마지막 원소는 클래스(레이블)
        # 클래스를 key 로 갖는 리스트에 vector 를 추가함
        separated[class_value].append(vector)
    return separated


def summarize_dataset(dataset):
    """
    dataset 의 각 컬럼(=변수=특성)의 평균과 표준편차, 갯수들을 계산, 리턴
    [(x1 variable's mean, stddev, count), (x2 variable's mean, stddev, count), ...]
    """
    # for col in zip(*dataset):
    #     print('unpacking \n', col)
    # # * : unpacking 연산자

    # unpacking 연산자 설명
    # *[1, 2] -> 1, 2
    # *[[1, 2], [3, 4]] -> [1, 2], [3, 4]
    # zip(*[[1, 2], [3, 4]]) -> zip([1, 2], [3, 4]) -> zip의 역할 : 성분별로 묶어준다 -> [1, 3], [2, 4] 즉 컬럼을 뽑아냈다.

    summaries = [(np.mean(col), np.std(col), len(col)) for col in zip(*dataset)]  # zip(*list) => col 만 꺼내준다.
    # 마지막 Class 는 필요없는 통계량이므로 삭제하자! (데이터가 아니라 클래스(label))
    del summaries[-1]  # list 를 삭제 - del 사용
    return summaries


# 클래스별로 평균, 표준편차를 계산
def summarize_by_class(dataset):
    """
    데이터 세트의 변수(특성)들에 대해서, 각 클래스 별로 평균, 표준편차 개수 요약
    {class_0 : [(x1_mean, x1_std, x1_len),
                (x2_mean, x2_std, x2_len)],
     class_1 : [(x1_mean, x1_std, x1_len),
                (x2_mean, x2_std, x2_len)]}
    """
    # dataset 을 Class 별로 분류
    separated = separate_by_class2(dataset)  # type : dict
    summaries = dict()
    for class_value, vectors in separated.items():
        summaries[class_value] = summarize_dataset(vectors)
    return summaries


# 확률을 계산 using 확률밀도함수 (PDF: Probability Density Function)
def calculate_probability(x, mu, sigma):
    """Gaussian Normal Distribution"""
    exponent = exp(-(x - mu)**2 / (2 * sigma ** 2))
    return (1 / (sqrt(pi*2) * sigma)) * exponent


# 클래스별로 분류되어있는 평균, 표준편차 다 알고 있을 때(summaries 인풋), 새로운 값이 들어오면 (vector 인풋)
def calculate_class_probability(summaries, vector):
    """
    주어진 vector 의 각 클래스별 예측값을 계산
    P(class|x1, x2) ~ P(x1|class)*P(x2|class)*P(class)
    """
    total_rows = sum([vectors[0][2] for _, vectors in summaries.items()])
    # 전체 데이터 row 10개 있다~ dict 이기 때문에 total len() 2 개 뿐!
    # vectors[0] : dict 의 list 중 1 번째 tuple
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        # p = P(class)
        probabilities[class_value] = class_summaries[0][2] / total_rows  # class = 0 or 1 에 속할 확률 P(class=0 or 1)
        for i in range(len(class_summaries)):
            mu, sigma, count = class_summaries[i]
            # prob = P(x1|class)
            prob = calculate_probability(vector[i], mu, sigma)  # vector[i] 의 확률을 pdf 로 계산하겠다.
            # p = P(class)*P(x1|class) -> for 문 반복(누적)
            probabilities[class_value] *= prob
    return probabilities  # P(go_out|rainy, broken) ~ P(rainy|go_out)*P(broken|go_out)*P(go_out)


if __name__ == '__main__':
    # test dummy data
    # [[x1, x2, 0 or 1], ...]
    random.seed(1212)
    dataset = [[random.random(), random.random(), x // 5] for x in range(10)]  # 나눈 몫! (x//5)-> 0 이거나 1
    print(dataset)

    # separated 형태 바꿈! - train set 처럼
    separated = separate_by_class(dataset)  # list 넘김
    print(separated)
    separated2 = separate_by_class2(dataset)  # list 넘김
    print(separated2)  # defaultdict(<class 'list'>

    # pandas DataFrame 변환
    df = pd.DataFrame(dataset, columns=['x1', 'x2', 'Class'])
    print(df)  # 출력 더 보기 좋다~ (연속형 변수)

    # summary : dataset 의 각 컬럼(=변수=특성)의 평균과 표준편차들을 계산, 리턴
    summary = summarize_dataset(dataset)
    print(summary)  # [(0.39146032325166713, 0.25603536009593864, 10), (0.5617387271721289, 0.23925734857414413, 10)]

    for col in zip(*dataset):
        print('unpacking \n', col)
    # * : unpacking 연산자 실습
    # *[1, 2] -> 1, 2
    # *[[1, 2], [3, 4]] -> [1, 2], [3, 4]
    # zip(*[[1, 2], [3, 4]]) -> zip([1, 2], [3, 4]) -> zip의 역할 : 성분별로 묶어준다 -> [1, 3], [2, 4] 즉 컬럼을 뽑아냈다.

    # 결론
    summaries = summarize_by_class(dataset)
    print(summaries)  # dict 리턴  dict 의 원소(tuple) 2 개 짜리 list
    # {0: [(0.5575868660862423, 0.1890225124131006, 5), (0.4838391907643089, 0.20840352482452287, 5)],
    # 1: [(0.22533378041709198, 0.2004560913806744, 5), (0.6396382635799489, 0.24273329600420898, 5)]}

    # test for calculate_class_probability
    print(dataset[0])  # [0.7899567764583166, 0.29996159568611847, 0]
    probabilities = calculate_class_probability(summaries, dataset[0])
    print(probabilities)  # {0: 0.642932959094217, 1: 0.011630975375924323} -> 합쳐서 1이 아니다. 나이브베이즈의 분모 계산 안했기 때문

    # iris data example
    X, y = load_iris(return_X_y=True)
    # print(X[:5])
    # print(y[:5])
    # print(np.c_[X, y])
    iris_dataset = np.c_[X, y]  # class 와 데이터가 붙어 있어야 한다~
    # print(iris_dataset[:5])
    # print(iris_dataset[-5:])

    # iris_dataset[0], iris_dataset[50], iris_dataset[100]
    summaries = summarize_by_class(iris_dataset)
    probabilities = calculate_class_probability(summaries, iris_dataset[100])
    print(probabilities)  # {0.0: 6.10015464109645e-111(마이너스), 1.0: 0.015262048871741643, 2.0: 0.003719709397757642}: 1
    print(iris_dataset[100])  # [7.  3.2 4.7 1.4 1. ]: 1
