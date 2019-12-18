"""선형회귀의 예측값을 t로 넣어 시그모이드함수를 계산,
시그모이드 함수 > 0.5 = 1
시그모이드 함수 < 0.5 = 0
을 계산하여 분류 문제를 해결한다
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


def logistic(x):
    """Logistic Sigmoid 함수"""
    return 1 / (1 + math.exp(-x))


def predict(row, betas):
    """row 의 x1, x2 값과 betas 의 b0, b1, b2 를 사용해서
    회귀식 y_hat = b0 + b1*x1 + b2*x2 를 만들고
    회귀식(즉, 예측값)을 로지스틱 함수의 파라미터에 전달해서 리턴값을 받음
    즉, 선형회귀식의 예측값 하나하나를 시그모이드 함수에 넣어주는 역할"""
    y_hat = betas[0]
    for i in range(len(betas) - 1):  # ?
        y_hat += betas[i + 1] * row[i]
    return logistic(y_hat)


def coefficient_sgd(dataset, learning_rate, epochs):  #stochastic gradient decent
    """회귀식 y = b0 + b1*x1 + b2*x2 의 계수들(b0, b1, b2) 을 확률적 경사하강법으로 근사값을 추정"""
    # 회귀식에서 처음에 사용할 betas 초기값을 0 부터 시작
    betas = [0 for _ in range(len(dataset[0]))]  # col 을 주기 위해서 dataset 의 첫번째 row 를 주었다
    for epoch in range(epochs):
        # sse : sum of squared errors
        sse = 0
        for sample in dataset:  # dataset 에서 row 갯수만큼 반복
            prediction = predict(sample, betas)  # row 1개와 beta 를 가지고 선형회귀식을 만들어 추정한 예측값 prediction 리턴
            error = sample[-1] - prediction
            sse += error ** 2  # 계속될 수록 sse가 줄어든다 why? 원래 경사하강법의 목적이 sse 줄이는 것
            betas[0] = betas[0] + learning_rate * error * prediction * (1 - prediction)
            for i in range(len(sample) - 1):
                betas[i + 1] = betas[i + 1] + learning_rate * error * prediction * (1 - prediction) * sample[i]
            # 계수들(b0, b1, b2)를 아래와 같은 방법으로 업데이트
            # b_new = b + learning_rate * error * prediction * (1 - prediction) * x
            #         위 식에서 x (b0일때는 1, 나머지는 각각 x1, x2 를 대입)
            #         시그모이드 함수 미분, 합성함수 미분, 분수 미분 사용
            print(f'>>> epoch:{epoch}, learning rate:{learning_rate}, sum squared error:{sse}')
    # 모든 epochs 가 끝난 다음에 최종 betas 리턴
    return betas

# learning_rate : 좌표를 움직이는 속도 (거리) : 발산 및 수렴 개념
#                 고정된 값만 쓰는 것 아니다. -> 오차가 수정 안되는 경우 (처음에는 많이, 나중에는 조금씩 이동)
# gradient 방향값 : 최솟값일때 gradient(-) 반대 방향 -> (+) / gradient(+) 반대 방향 -> (-)
# gradient 방향값 : 최댓값일때 gradient(-) 방향 -> (-) / gradient(+) 방향 -> (+)
# epoch : 전체 샘플을 다시 한번 반복하는 갯수
# 임계값도 줄 수 있다. 경사하강법을 통해 오차가 줄어들지만 오차가 지속되는 경우 break 가능


if __name__ == '__main__':
    iris = load_iris()
    print(iris.DESCR)  # dataset explanation
    X = iris.data  # iris['data']
    y = iris.target  # iris['target']
    features = iris.feature_names  # iris['feature_names']

    for i in range(len(features)):
        plt.scatter(X[:, i], y, label=features[i])
    plt.legend()
    plt.show()
    # 그래프를 보면 겹치는 부분이 없는 것이 구분이 잘 되는 특성들이다.
    #                     Min  Max   Mean    SD   Class Correlation (-1에 가깝거나 1에 가까울 수록 상관관계가 높다)
    #     sepal length:   4.3  7.9   5.84   0.83    0.7826
    #     sepal width:    2.0  4.4   3.05   0.43   -0.4194
    #     petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    #     petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
    # X 특성 높은 두개 선택
    X = X[:, 2:4]
    print(X[:5])

    # setosa 5개, setosa 가 아닌 품종 5개 sampling
    indices = [x for x in range(0, 100, 10)]
    sample_data = np.c_[X[indices, :], y[indices]]
    print(sample_data)  # 실제값

    # 선형회귀 -> 시그모이드 로 logistic 회귀
    np.random.seed(1218)
    betas = np.random.random(3)  # random 3개 -> b0, b1, b2 역할
    print('betas', betas)
    for sample in sample_data:
        prediction = predict(sample, betas)
        # 오차 = 실제값 - 예측값
        error = sample[-1] - prediction
        print(f'True : {sample[-1]}, Pred : {prediction}, error : {error}')

    learning_rate = 0.3
    epochs = 100
    betas = coefficient_sgd(sample_data, learning_rate, epochs)
    print('betas = ', betas)

    # 모델 성능 측정
    test_sample1 = np.r_[X[1, :], y[1]]  # row binding - np.r_
    print('test sample 1 : ', test_sample1)
    prediction = predict(test_sample1, betas)  # 첫번째 샘플에 대한 예측값
    print(f'True : {test_sample1[-1]}, Pred : {prediction}')

    test_sample2 = np.r_[X[51, :], y[51]]
    print('test sample 2 : ', test_sample2)
    prediction = predict(test_sample2, betas)
    print(f'True : {test_sample2[-1]}, Pred : {prediction}')

