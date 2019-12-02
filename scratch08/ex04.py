'''
선형 회귀(Linear Regression) :

모델 : y = ax+b
목적 : 기울기(slope) a와 y절편 b를 찾자

파라미터 (a, b) : 찾고자 하는 값
                (a, b)를 특정 값으로 가정했을 때의 예상값과 실제값 사이의 오차들의 제곱의 합을 최소로 하는 a, b

실제값 : (x, y)
예상값 : y_hat = theta1 * x + theta2
오차 : e = y_hat - y = theta1 * x + theta2 - y
( 첨자 i 모두 생략 )
오차 제곱 : f = e**2 = ( theta1 * x + theta2 - y )**2
기울기 theta1에 대한 편미분 : ∂f/∂t1 ~ e * x
y절편 theta2에 대한 편미분 : ∂f/∂t2 ~ e
<칠판 필기와 비교하기>

두개의 성분을 가지고 있는 gradient 가 완성되었다.
1) 기울기 theta1에 대한 편미분 e * x
2) y절편 theta2에 대한 편미분 e

이러한 gradient 의 e를 최소화 시켜주는 방법은 다음과 같다.
1) 확률적 경사 하강법(Stochastic Gradient Descent)
2) 배치 경사 하강법(Batch GD)
3) 미니 배치 경사 하강법(Mini-batch GD)

: [step : 학습률, epoch : ]를 바꿈으로서 성능 개선 가능!


'''

# method for 선형회귀
import random

from lab_python.scratch04.ex01 import vector_mean
from lab_python.scratch08.ex03 import gradient_step


def linear_gradient(x, y, theta):
    """
     특정 데이터 (x,y)에서 기울기와 y절편에 대한 편미분 벡터를 리턴

    :param x: 실제 데이터(ex_배기량 등)
    :param y: 실제 데이터(ex_연비 등)
    :param theta: [theta1, theta2] 로 이루어진 벡터(리스트) 
                   theta1 - 기울기, theta2 - y절편
    :return:
    """
    slope, intercept = theta
    y_hat = slope * x + intercept  # 예상값
    error = y_hat - y  # 오차
    # [기울기에 대한 편미분, y절편에 대한 편미분]
    gradient = [error * x, error]
    return gradient
    # 기울기에 대한 편미분 * step : x 방향(기울기=gradient)를 통해 기울기 정한다. (최소값 찾으려면, x의 절대값은 -이다.)
    #                           최솟값 - error와 반대방향으로 움직인다
    # y절편에 대한 편미분을 통해 직선을 아래 / 위 중 어떤 방향으로 움직일 것인지 정한다. (최솟값 - error와 반대방향으로 움직인다)

'''
1) 확률적 경사 하강법(Stochastic Gradient Descent)
    전체 데이터 세트(훈련 세트)에서 샘플 데이터 1개마다 gradient를 계산, 파라미터(기울기, 절편- theta) 변경
    위 과정을 임의의 횟수(epoch)만큼 반복
    (1 epoch:
    - 샘플 데이터1의 slope, intercept 의 error 계산, error 최소화 한 slope2, intercept2 도출
    - 샘플 데이터2의 slope2, intercept2 의 error 계산, error 최소화 한 slope3, intercept3 도출
    - 샘플 데이터3의 slope3, intercept3 의 error 계산, error 최소화 한 slope4, intercept4 도출
    - 샘플 데이터(n)의 slope(n), intercept(n) 의 error 계산, error 최소화 한 slope(n+1), intercept(n+1) 도출)
     2 epoch:
     - 바뀐 theta = [epoch1에서 찾은 slope, epoch1에서 찾은 intercept]가 초기 theta가 된다.
     - 샘플 데이터1의 slope, intercept의 error 계산, 

    단점 : 데이터 안의 공간이 널뛰기하면서 최적화된 기울기와 절편을 찾아갈 때 매끄럽지 못하고 들쭉날쭉하다. 
          step과 초기값을 잘못 설정하면 발산할 수 있다.


2) 배치 경사 하강법(Batch GD)
    전체 데이터 세트(훈련 세트)를 사용하여 **전체 gradient들의 평균** gradient를 gradient로 사용하여 파라미터 theta를 변경
    위 과정을 임의의 횟수(epoch)만큼 반복

    단점 : epoch 자체를 많이 반복해야 한다. why? 평균을 계산하는 것이 epoch 1번이기 때문(feedback 1번)
          비용이 훨씬 많이 든다(표현)

3) 미니 배치 경사 하강법(Mini-batch GD)
    1) 과 2)의 단점을 보강
    전체 데이터 세트(훈련 세트)를 크기를 작게 샘플링해서 처리하는 방식.
    각각의 반복(epoch)마다 데이터 세트의 순서를 섞어서 파라미터(theta)의 최적값을 찾는다.
'''


dataset = [(x, 20*x + 5) for x in range(-50, 51)]  # 실제 데이터셋
# y = 20*x + 5라는 직선이 있는데, 우리가 기울기 20, 절편 5를 찾아보자.


def minibatches(dataset, batch_size, shuffle=True):
    """미니배치"""
    # 데이터 세트를 무작위로 섞음
    if shuffle:
        random.shuffle(dataset)

    # 배치 시작 인덱스: 0, batch_size, 2*batch_size, 3*batch_size,, 식으로 [] list를 만들었다
    batch_starts = [s for s in range(0, len(dataset), batch_size)]
    mini = [dataset[s:s + batch_size] for s in batch_starts]
    return mini


if __name__ == '__main__':

    # 1) 확률적 경사 하강법(Stochastic Gradient Descent)
    print('1) 확률적 경사 하강법 -----')
    # 임의의 파라미터 초기값 [기울기 1, y절편 1] : y = x + 1
    theta = [1, 1]
    # step 상수 선언 : 파라미터의 값을 변경할 때 사용할 가중치 (학습률)
    step = 0.001  # next_x = init_x + step * gradient 식에서 step

    # 임의의 횟수(epoch)만큼 반복 200번 epoch * 101개 dataset
    for epoch in range(200):
        # 전체 데이터 세트(훈련 세트)에서 샘플 데이터 1개마다 gradient를 계산 : for x, y in dataset : dataset에서 추출
        random.shuffle(dataset)  # dataset의 순서 섞는다. 똑같은 데이터가 섞이면서 순서 바뀐 상태에서 for loop에서 만들었던 theta를 주고 다시 error 최소화
        for x, y in dataset:
            gradient = linear_gradient(x, y, theta)
            # 파라미터(기울기, 절편- theta) 변경
            theta = gradient_step(theta, gradient, -step)  # error를 최소화하는 문제이므로 step 절대값은 - 이다.
        if (epoch + 1) % 10 == 0:  # 10 epoch마다 출력
            print(f'{epoch}: {theta}')

    # 2) 배치 경사 하강법(Batch GD)
    print('2) 배치 경사 하강법 -----')
    theta = [1, 1]
    step = 0.001

    for epoch in range(5000):  # 5000 * 100번
        # 모든 sample 에서의 gradient 를 계산
        gradients = [linear_gradient(x, y, theta) for x, y in dataset]
        # gradients 의 평균 계산
        gradient = vector_mean(gradients)
        # 파라미터 theta(기울기, 절편)을 변경
        theta = gradient_step(theta, gradient, -step)  # 최솟값 : - step
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')

    # 3) 미니 배치 경사 하강법(Mini-batch GD)
    print('3) 미니 배치 경사 하강법 -----')
    theta = [1, 1]
    step = 0.001

    for epoch in range(1000):
        # 20개의 미니배치 선택 : 섞어서 20개를 뽑는다. (= random sample 뽑는다)
        mini_batches = minibatches(dataset, 20, True)
        for batch in mini_batches:  # 20개만 들어있는 dataset
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')


















