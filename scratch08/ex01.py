'''
Gradient Descent(경사 하강법):
데이터 과학에서 최적화 문제를 만나게 되는 상황이 있음.
최적화 문제 - 특정 상황에서 가장 적합한 모델을 찾는 문제

ex_모델의 error(목표값 - 실제값)을 최소화 - 최솟값을 찾는다
ex_likelihood(우도)를 최대화 - 최댓값을 찾는다
베이즈정리 - 우도 *****자세히 알아볼 것!

경사하강법의 목적 : 타겟 함수를 최소(혹은 최대)로 만들어주는 파라미터를 구한다.


<과정> --------------------------------------------------------
1. 곡선의 접선을 찾는다.
2. 접선의 기울기 방향으로 곡선상의 점을 이동시키면서 최소(혹은 최대)값을 찾는다.
--------------------------------------------------------------
'''
import random

import matplotlib.pyplot as plt


# 2차 함수의 최소(최대)값 찾기
import numpy as np


def f(x):
    return x ** 2


# f(x)의 도함수
def f_derivative(x):
    """y = x ** 2 의 도함수(미분) : y = 2x
    최솟값 찾기
    기울기가 - : x가 + 으로 이동해야 최솟값을 갖는다
    기울기가 + : x가 - 으로 이동해야 최솟값을 갖는다
    최댓값 찾기
    기울기가 + : x가 + 으로 이동해야 최댓값을 갖는다
    기울기가 - : x가 - 으로 이동해야 최댓값을 갖는다
    """
    return 2 * x


def tangent(x, a, x1, y1):
    """기울기가 a이고, 점(x1, y1)을 지나는 직선의 방정식"""
    return a*(x - x1) + y1


def difference_quotient(f, x, h):
    """도함수 공식"""
    return (f(x + h) - f(x)) / h


# 경사하강법
def move(x, direction, step=-0.1):
    """
    gradient 적용하기 위한 step 설정!! 중요
    : x 좌표를 새로운 x로 이동
    :param x: 좌표
    :param direction: 기울기(+/-)값을 결정함
    :param step: 이동할 단위(너무 작으면 느리게 최대/최소값에 도달, 너무 크면 발산할 수도 있음)
    :return: 
    """
    return x + step * direction




if __name__ == '__main__':
    # 그래프를 그릴 x 좌표들의 점들을 만들기 (-3.0, -2.9, .. 2.9, 3.0)
    xs = [x / 10 for x in range(-30, 31)]
    # 그래프를 그릴 y 좌표들의 점들을 만들기
    ys = [f(x) for x in xs]

    # 접선의 기울기 그래프 그리기(x = -1에서의 접선)
    # y = a(도함수 = 기울기)x + b(y절편 = x=0에서의 값 -> 여기서는 x=-1에서 곡선과 접선이 만나는 점의 좌표가 된다.)
    a = f_derivative(-1)
    x1, y1 = -1, f(-1)
    tangents = [tangent(x, a, x1, y1) for x in xs]

    # 도함수의 근사값을 사용(estimates)
    # h 값이 0에 가까워질 수록 더 정확한 접선의 기울기가 됨(극한으로 limit 보냄)
    h = 0.1
    a2 = difference_quotient(f, -1, h=h)
    tangent_estimates = [tangent(x, a2, x1, y1) for x in xs]

    # plt 선 추가
    plt.plot(xs, ys)
    plt.plot(xs, tangents, label='actual')
    plt.plot(xs, tangent_estimates, label=f'estimates: h = {h}')
    plt.axhline(y=0, color='black')  # y=0인 보조선
    plt.axvline(x=0, color='black')  # x=0인 보조선
    plt.legend()
    plt.show()

    # 실제기울기(f_derivative)와 기울기 근사값(difference_quotient)의 비교 : 모든 점에서의 기울기 출력
    xs = [x for x in range(-10, 11)]
    actuals = [f_derivative(x) for x in xs]  # 기울기를 모아둔 [list]를 만들었다.
    estimates_1 = [difference_quotient(f, x, h=1) for x in xs]
    estimates_2 = [difference_quotient(f, x, h=0.1) for x in xs]

    plt.scatter(xs, actuals, label='actual', marker='x')
    plt.scatter(xs, estimates_1, label='h=1', marker='+')
    plt.scatter(xs, estimates_2, label='h=0.1', marker='o')
    plt.legend()
    plt.show()
    # h=0.1 과 actual 의 기울기는 비슷
    # h=1은 둘과 기울기 차이가 남
    # h가 작아지면, 모든 점에서의 접선이 actual 과 비슷해진다는 것 증명하였음.

    # 경사하강법(gradient descent):
    xs = [x * 0.1 for x in range(-30, 31)]
    ys = [f(x) for x in xs]   # y=x**2 그래프의 y 값들
    init_x = 2  # 최솟값을 찾기 위해 시작할 x 좌표
    for _ in range(5):
        # x = init_x 에서의 접선의 기울기
        gradient = difference_quotient(f, init_x, h=0.01)
        # 접선을 그래프에 그리기 위해 저장
        tangent_estimates = [tangent(x, gradient, init_x, f(init_x)) for x in xs]
        plt.plot(xs, tangent_estimates, label=f'x = {init_x}')
        # x 좌표를 새로운 좌표로 이동
        init_x = move(init_x, gradient, step=-0.9)

    plt.plot(xs, ys, label='y=x**2')
    plt.legend()
    plt.ylim(bottom=-1)
    plt.show()
    # -2에서 init_x가 시작하였다. 도함수 -4(기울기=gradient), step(-0.1)*gradient(-4)=0.4
    # -2 + 0.4 = -1.6
    # -1.6 + 2(-1.6)*-0.1 = -1.6 + 0.32 = -1.28

    # ***** step = 학습률 (meta) ***** 중요 : 경사하강법의 점을 옮기는 기준!
    # step=-1의 경우 발산(무한 loop -2, 2)
    # step=-2의 경우 그래프를 기반으로 발산(무한대)
    # step=-0.5의 경우 한 번만에 최솟값 도달
    # : 즉, 이동 거리(step)을 잘 정해주는 것이 매우 중요하다.

    # 움직이기 전의 좌표 - 움직인 후의 좌표 = 0.xxx로 수렴한다(0으로 수렴한다)
    # 임의의 점에서 시작해서 y=x**2의 최솟값을 찾음
    random.seed(1128)  # random 패키지는 0이 난수로 나올 확률이 있다. (조심!)
    init_x = np.random.randint(-10, 10)  # 시작값
    print(f'init_x = {init_x}')
    tolerance = 0.0000001  # 별명(정밀도) : 두 x 값(움직이기 전의 좌표 - 움직인 후의 좌표) 사이의 거리가 tolerance 이하이면 반복문 종료
    count = 0
    while True:  # 반복
        count += 1
        # x 좌표에서의 접선의 기울기를 계산 why? 점 이동 방향 결정하기 위해서
        gradient = difference_quotient(f, init_x, h=0.001)
        # 찾은 기울기를 이용해서 x 좌표를 이동시킴
        next_x = move(init_x, gradient, step=-0.1)  # 최솟값 step= (-)
        print(f'{count}: x = {next_x}')
        if abs(next_x - init_x) < tolerance:
            break
        else:
            init_x = next_x  # 이동한 점이 다음 반복에서는 시작점이 되어야 함.

        # 시작값 & step 값에 따라서 몇단계까지 가는지가 달라진다.
        # step = -0.1(선을따라 수렴) < step = -0.9(지그재그) 수렴하는 단계












