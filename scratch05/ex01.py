'''
<<통계>>5

<데이터를 어떻게 볼 것인가>
1. 중심이 어디 있는가?
중심경향성: NULL을 대체하는 방법으로 자주 쓰임
1-1. 평균 : 단점 - 이상치에 민감하다
1-2. 중앙값 : 이상치에 영향 덜 받음
1-3. 분위 : 사분위수 / 백분위수
1-4. 최빈값 : 데이터에서 가장 자주 등장하는 값 - 여러개인 경우 모두 찾아야 한다.(2개 이상인 경우)
2. 얼마나 퍼져 있는가?
산포도: 0 근접 - 거의 퍼져 있지 않다 ~ 큰 값 매우 퍼져 있다
2-1. 분산(variance) : 평균을 출발점으로 찾는다
2-2. 표준편차(standard deviation) : 평균을 출발점으로 찾는다
2-3. 범위(range) : 최댓값 - 최솟값
3. 상관관계가 있는가?
상관관계 : 변수 2가지를 생각한다. 변수 2개가 같이 증가/감소하면 비례, 변수 2개가 음의 상관관계를 가지는지
3-1. 공분산(covariance)
3-2. 상관계수(correlation)
3-3.

'''
import numpy as np
import math as mt
from collections import Counter
from lab_python.scratch04.ex01 import dot  # *****중요!*****

def mean(x):
    """
    평균을 계산하여 리턴해주는 함수

    :param x: 원소 n개인 1차원 리스트
    :return: 평균
    """
    return sum(x) / len(x)


def median(x):
    """
    리스트 x를 정렬했을 때 중앙에 있는 값을 찾아서 리턴
    n이 홀수이면 중앙값은 1개
    n이 짝수이면 중앙값은 두 값의 평균
    
    :param x: 원소 n개인 1차원 리스트
    :return: 중앙값
    """
    sort_x = sorted(x)  # 데이터 크기 순으로 정렬(오름차순)
    mid_point = len(x) // 2  # 0부터 시작하기 때문에, 홀수 일때 중앙값이 나온다.
    index_1 = mid_point - 1
    if len(sort_x) % 2:  # n이 홀수인 경우
        return sort_x[mid_point]
    else:  # n이 짝수인 경우
        return (sort_x[index_1] + sort_x[mid_point]) / 2


def quentile(x, p):
    """
    리스트 x의 p 분위에 속하는 값을 찾아서 리턴
    
    :param x: 원소 n개인 1차원 리스트
    :param p: 0~ 1.0 사이의 값 (0.25 1사분위수)
    :return: 해당 분위수(퍼센트)의 값
    """
    sort_x = sorted(x)
    # p_index = int(p*len(x))
    # return sort_x[p_index]
# or
    return sort_x[int(p*len(x))]


def quentile(x, p):
    """
    리스트 x의 p 분위에 속하는 값을 찾아서 리턴

    :param x: 원소 n개인 1차원 리스트
    :param p: 0~ 1.0 사이의 값 (0.25 1사분위수)
    :return: 해당 분위수(퍼센트)의 값
    """
    n = len(x)
    sort_x = sorted(x)
    p_index = int(n * p)  # 해당 퍼센트의 인덱스 - 소수점은 버리겠다.(정수)
    return sort_x[p_index]


def mode(x):
    """
    최빈값.
    from collections import Counter

    :param x:
    :return:
    """
    # step1. 생성자 만들기
    n = Counter(x)  # 생성자 만들었다.
    # n.method : 변수.메소드 쓸 수 있음~ Counter 객체(인스턴스) 생성
    print(n)  # dict 형태
    print(n.keys(), n.values())  # n.keys() x의 데이터들이 인덱스가 되었음, n.values() 빈도수가 value가 됨
    print(n.items())  # [(),()]
    # step2. 빈도수의 최댓값 찾기
    max_count = max(n.values())  # 빈도수의 최댓값
    # freq = []  # 최빈값들을 저장할 리스트
    # for val, cnt in counts.items():  # Counter 객체에 대해서 반복
    #     if cnt == max_count:  # 빈도수가 최대 빈도수와 같으면
    #         freq.append(val)  # 리스트에 저장
    # return freq
    return [val for val, cnt in counts.items()
            if cnt == max_count]


def data_range(x):  # python basic function range 구별 위해 data_붙임
    """
    범위

    :param x: 원소 n개인 1차원 리스트
    :return: 리스트의 최댓값 - 리스트의 최솟값
    """
    return max(x) - min(x)  # 정렬 2번
# or
    # sorted_x = sorted(x)  # 정렬 1번 - 더 빠르다는 장점
    # return sorted_x[len(x)-1] - sorted_x[0]  # 전체길이 - 1 = 마지막 인덱스


def de_mean(x):
    """
    편차들의 리스트

    :param x:
    :return:
    """
    mu = mean(x)
    return [x_i - mu for x_i in x]  # \sum (x_i - M)


def variance(x):
    """
    (x1 - mean(x))**2 + (x2 - mean(x))**2 + ... (xn - mean(x))**2 / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :return: 분산
    """
    sum = 0
    for i in x:
        sum += (i - mean(x))**2
    return sum / ( len(x) - 1 )


def variance(x):
    """
    (x1 - mean(x))**2 + (x2 - mean(x))**2 + ... (xn - mean(x))**2 / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :return: 분산
    """
    n = len(x)  # 원소개수
    x_bar = mean(x)  # 평균
    return sum([(x_i - x_bar)**2 for x_i in x]) / (n-1)


def variance(x):
    """
    (x1 - mean(x))**2 + (x2 - mean(x))**2 + ... (xn - mean(x))**2 / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :return: 분산
    """
    n = len(x)
    deviations = de_mean(x)  # 편차들의 리스트
    return sum([d**2 for d in deviations]) / (n-1)


def variance(x):
    """
    (x1 - mean(x))**2 + (x2 - mean(x))**2 + ... (xn - mean(x))**2 / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :return: 분산
    """
    # scratch04\ex01의 dot(v,v) 자기자신을 곱하여 더한 것과 같다. " \sigma (x_i - M)**2 "
    # from lab_python.scratch04.ex01 import dot을 맨 위에 써서 import시켜준다.
    n = len(x)
    deviations = de_mean(x)  # \sum (x_i - M)
    return dot(deviations, deviations) / (n-1)


def standard_deviation(x):
    """
    sqrt(variance)

    :param x: 원소 n개인 1차원 리스트
    :return: 표준편차
    """
    return mt.sqrt(variance(x))


def covariance(x, y):
    """
    공분산(covariance)
    cov = sum((x_i - x_bar)(y_i - y_bar)) / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :param y: 원소 n개인 1차원 리스트
    :return: 공분산
    """
    x_bar = mean(x)  # x의 평균
    y_bar = mean(y)  # y의 평균
    x_deviations = [x_i - x_bar for x_i in x]
    y_deviations = [y_i - y_bar for y_i in y]
    sum_of_deviations = 0
    for xd, yd in zip(x_deviations, y_deviations):
        sum_of_deviations += xd * yd
    return sum_of_deviations / ( len(x) - 1 )


def covariance(x, y):
    """
    공분산(covariance)
    cov = sum((x_i - x_bar)(y_i - y_bar)) / (n-1)

    :param x: 원소 n개인 1차원 리스트
    :param y: 원소 n개인 1차원 리스트
    :return: 공분산
    """
    x_bar = mean(x)  # x의 평균
    y_bar = mean(y)  # y의 평균
    x_deviations = [x_i - x_bar for x_i in x]
    y_deviations = [y_i - y_bar for y_i in y]
    sum_of_deviations = dot(x_deviations, y_deviations)
    return sum_of_deviations / (len(x) - 1)


def correlation(x, y):
    """
    상관계수(correlation)
    Corr = cov(x, y) / (sd(x) * sd(y))

    :param x:
    :param y:
    :return:
    """
    sd_x = standard_deviation(x)
    sd_y = standard_deviation(y)
    if sd_x != 0 and sd_y != 0:
        corr = covariance(x, y) / (standard_deviation(x) * standard_deviation(y))
    else:
        corr = 0
    return corr
# 표준편차가 0이 되는 경우는 correlations 분모 0인 error
# standard_deviation 하나라도 0이 된다면 -> 수학책 찾아보기.


if __name__ == '__main__':
    A = [i for i in range(1, 11)]
    print(A)
    print('mean = ', mean(A))
    print('median = ', median(A))
    print('quentile = ', quentile(A, 0.25))
    print('variance = ', variance(A))
    print('standard deviation = ', standard_deviation(A))

    B = [10, 20, 30, 40, 50]
    print(B)
    print('mean = ', mean(B))
    print('median = ', median(B))
    print('quentile = ', quentile(B, 0.25))
    print('variance = ', variance(B))
    print('standard deviation = ', standard_deviation(B))


    x = [2, 2, 3, 3, 4, 4, 4, 6, 6, 6, 100]
    y = [10, 2, 5, 3, 4, 1, 4, 0, 6, 1, 7]
    data_cov = covariance(x, y)
    print('x,y\'s covariance = ', data_cov)
    data_corr = correlation(x, y)
    print('x,y\'s correlation = ', data_corr)

# cf.
# callable : 부를수 있는 객체 - 함수
