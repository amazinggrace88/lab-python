"""
선형회귀 알고리즘 구현

: 수학적으로 구현하기
 1. 그래프 그리기
 2.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def odds(p):
    return p / (1 -p)  # 성공 / 실패 비율

# 컴퓨터 연산 특징 : 더하기 빼기가 곱하기 나누기보다 오차가 적다 (오차는 곱할수록 커지기 때문 underflow 작은범위 바깥으로 나가는 경우)
# 컴퓨터 기법 : 확률을 log 취하여 더하고 나중에 지수로 바꿔주는 연산을 한다 (정확한 계산 위해)
# overflow?

def log_odds(p):
    """odds 에 log 를 취한 값"""
    return math.log(odds(p))  # 자연로그 log e 사용했음 # e - 2.718..


def sigmoid(t):
    """logistic 함수 라고도 이야기 함 (시그마에서 나온 시그모이드, 로지스틱 회귀에 쓰인다)
    log_odds(odds에 log를 취한 값)을 알고 있을 때, 성공확률 p를 계산"""
    return 1 / (1 + math.exp(-t))  # 시그모이드 ~ 노트 필기 참조 - 쉬움!


if __name__ == '__main__':
    p = 0.8
    print(f'p = {p}, odds(p) = {odds(p)}, log_odds(p) = {log_odds(p)}')

    t = 1.39
    probability = sigmoid(t)
    print(f'probability = {probability}')

    # graph
    # 1. odds
    xs = np.linspace(0.01, 0.99, 100)  # why ? 0.99? 1이면 odd 무한대 # 0.01~0.99까지 100개의 점 (임의 아니고, 순서 있음)
    # print(xs)
    ys = [odds(x) for x in xs]
    plt.plot(xs, ys)
    plt.ylim(bottom=0.0, top=10.0)
    for i in range(1, 5):
        plt.axhline(y=(2*i), color='0.5')  # y 축 2, 4, 6, 8
        plt.axvline(x=(0.2*i), color='0.5')  # x 축 0.2, 0.4, 0.6, 0.8
    plt.title('odds')
    plt.show()

    # 2. log odds
    ys = [log_odds(x) for x in xs]
    plt.plot(xs, ys)
    plt.title('log odds')
    plt.axhline(color='0.5')
    plt.axvline(color='0.5')
    plt.axvline(x=0.5, color='0.5')
    plt.axvline(x=1, color='0.5')
    plt.show()
    # x^0 = 1
    # 성공과 실패의 경우가 0.5 이면 odd=1 log1 = 0
    # 시그모이드는 log odds 를 반전시켜 놓은 모양
    # t값은 -무한대, 무한대까지 취할 수 있다~ why? 확률값이 아니고, t는 log odd에서 -무한대, 무한대

    # 3. sigmoid (logistic function)
    # x의 범위를 바꾼다 : t이므로
    xs = np.linspace(-10, 10, 100)
    ys = [sigmoid(x) for x in xs]
    plt.plot(xs, ys)
    plt.title('sigmoid')
    plt.axvline(color='0.5')
    plt.axhline(y=0.5, color='0.5')
    plt.axhline(y=1, color='0.5')
    plt.axhline(color='0.5')
    plt.show()


















