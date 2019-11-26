'''
중심 극한 정리(Central Limit Theorem)

모집단이 어떤 분포든지 상관없이, 표본의 크기가 충분히 크다면
모든 가능한 표본 평균은 모평균 주위에서 정규분포를 따른다.

= sample들의 평균은 모평균 주위에 있다.

= 만약 모집단이 평균이 mu이고, 표준편차가 sigma인 정규분포를 따른다면,
표본평균의 분포는 평균이 mu이고, 분산이 sigma/sqrt(n)인 정규분포가 된다.(n은 충분히 크다는 가정)

베르누이 확률 변수(Bernoulli random variable):
    어떤 시행의 결과가 '성공', '실패' 중 하나로 나타나고,
    성공의 확률이 p, 실패할 확률이 1 - p라 할 때
    그 결과가 성공이면 확률 변수는 1을 갖고,
    결과가 실패면 확률 변수는 0을 갖는 확률 변수 X

베르누이 확률 질량 함수(PMF: Probability Mass Function)
    pmf(x) = p if x = 1, 1 - p if x = 0
           = (p**x) ((1-p)**(1-x))

이항 확률 변수(binomial random variable):
    n개의 독립적인 베르누이 확률 변수들 더한 것

(비유)
베르누이 확률 변수 -> 동전 한 개를 던질 때 앞면의 수
이항 확률 변수 -> 동전 n개를 던질 때 앞면의 수

베르누이 확률 변수의 기댓값(평균) = p, 표준편차 = sqrt(p(1-p))
중심 극한 정리: n이 적당히 크다면, 이항 확률 변수는 대략
평균이 np이고, 표준 편차가 sqrt(np(1-p)) -> 분산 np(1-p)인
정규 분포의 확률 변수와 같다.

-> 표본의 평균과 분산을 알아내면, 모집단의 평균과 분산을 예측할 수 있는 것이다.
'''
import math
import random


# 베르누이 확률 변수 리턴 함수
from collections import Counter
import matplotlib.pyplot as plt
from lab_python.scratch06.ex06 import normal_cdf, normal_pdf


def bernoulli_trial(p):
    """베르누이 확률 변수 1 또는 0을 확률 p에 따라서 리턴"""
    x = random.random()  # random() : 0 이상 1 미만의 난수 리턴
    return 1 if x < p else 0  # p : 1이 나올 확률


def binomial(n, p):
    """이항 확률 변수 : 1이 나올 확률 p인 베르누이 시행을 n번 했을 때, 1이 나오는 횟수를 리턴"""
    s = 0  # 1이 나오는 횟수
    for _ in range(n):
        s += bernoulli_trial(p)
    return s



if __name__ == '__main__':
    # for _ in range(10):
    #     print(bernoulli_trial(0.9), end= ' ')

    # for _ in range(10):
    #     print(binomial(10, 0.5), end=' ')
    # # 0.5의 확률로 10번 반복하여 실행한 실험 10번에서 각각 표본들의 1의 횟수 계산 및 리턴
    # 0~10까지의 범위를 가지며, 표본들의 1의 횟수의 평균은 5가 될 것이다.

    # <이항분포의 표본들의 평균 그래프 = pmf(x)>
    trials = 10_000
    n = 100  # 동전을 던지는 횟수
    p = 0.5  # 동전의 앞이 나올 확률
    data = [binomial(n, p) for _ in range(trials)]
    print(data[0:10])
    # plt.hist(data)
    # plt.show()  # histogram 을 그리는 다른 방법
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]  # key (1, 0 로 이루어진 배열)
    y_bar = [v / trials for v in histogram.values()]  # 1의 횟수 / trials, 0의 횟수 / trials
    plt.bar(x_bar, y_bar, color='0.75')

    # why? 이렇게 하는 이유?
    # y축에 단위를 0.5로 (즉, 확률로) 주기 위해서 Counter 를 사용하여 그래프를 만들었다.
    # binomial(n, p)에서 n을 늘릴 수록, 표본 평균들의 분포가 정규분포를 따라간다.
    # binomial(n, p)에서 p을 늘릴 수록, 표본 평균들의 평균이 np 쪽으로 편향된다.

    # <위의 평균 그래프에 정규분포 근사(approximation)>
    # 목적 : 이항 확률 변수는 n이 충분히 크면 정규 분포가 된다 (가정) 확인
    mu = n * p  # 평균
    sigma = math.sqrt(n*p*(1-p))  # 표준 편차
    # 정규 분포 그래프를 그리기 위해서
    x_line = range(min(data), max(data) + 1)
    # x_line = range(0, n+1) 로도 쓸 수 있다.
    y_line = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in x_line]
    # y_line = pdf(x + 0.5)의 면적 - pdf(x - 0.5)의 면적이므로 pdf 선이 출력된다.
    # y_line = [normal_pdf(x, mu, sigma) for x in x_line]  # pdf 로 선이 출력된다.
    plt.plot(x_line, y_line)
    plt.show()

















