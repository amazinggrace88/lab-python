'''
n차원(3차원 이상)의 경사 하강법 - using 편미분
'''
from lab_python.scratch04.ex01 import scalar_multiply, add


def partial_difference_quotient(f, v, i, h=0.001):
    """
    함수 f의 i번째 편도함수가 v에서 가지는 값
    함수 z = f(x,y)
    편미분 = (f([x1, x2, .. , xi+h, .. xn]) - f([x1, x2, .. xn])) / h

    :param f: f(vector) = float(숫자) 인 함수이름
    :param v: 기울기(gradient)를 계산할 위치 = n차원이므로 벡터(리스트)
    :param i: i번째 변화율 : ~번째 파라미터 : 기울기를 계산할 성분의 인덱스 - 정수
    :param h: i번째 성분의 변화량
    :return: 편미분 결과 - 벡터 (i 번째 성분 방향의 gradient)
    """
    # f([x1, x2, .. , xi+h, .. xn] 구현
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]  # enumerate: index, 값
    # i번째 방향으로 살짝 떨어진 점 f(w) - 원래 점 f(v) / h
    return (f(w) - f(v)) / h

    # or
    # w = []
    # for j, v_j in enumerate(v):
    #     if j == i:
    #         v_j += h
    #     w.append(v_j)
    # return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.001):
    """
    gradient의 근사값
    [∂f/∂x_1, ∂f/∂x_2, ... ∂f/∂x_n] => ∂f(partial) 즉, 편미분값

    :param f: f(vector) = float 함수
    :param v: 기울기를 구하려는 점의 좌표 [x1, ... xn]
    :param h: 증분(increment - 증가하는 양)
    :return: 모든 성분의 gradient(도함수)로 이루어진 벡터(리스트)
    """
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]


def gradient_step(v, gradient, step=-0.1):
    """
    [xi + step * ∂f/∂x_i]

    :param v: 이동 전 점의 위치 즉, xi
    :param gradient: 점 v에서의 기울기 (∂f/∂x_i)
    :param step: 이동시키는 가중치(학습률)
    :return: 기울기의 방향으로 이동한 점의 위치(새로운 점의 위치)
    """
    increment = scalar_multiply(step, gradient)
    return add(v, increment)  # vector add

