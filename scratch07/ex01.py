'''
가설(Hypothesis) 와 통계적추론(Inference)


<가설검정>
귀무가설(영가설, null hypothesis), H0 : 기본적인 가설
대립가설(alternative hypothesis), H1 : 비교되는 가설

(예) 양측검정 --> 보충하기
H0: 동전을 던졌을 때 앞면이 나올 확률 p = 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 1/2이 아니다(p != 1/2)

<증명방법>
H0가 맞다 - 유의수준 계산
H1이 틀리다 - 검정력(H1이 거짓이 될 확률) 계산

(예) 단측검정 : 특정한 기준을 통해 --> 보충하기
H0: 동전을 던졌을 때 앞면이 나올 확률은 p > 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 p <= 1/2


<과정>
         실험
-------------------------------------------------------------
실제    |가설 채택(가설 기각하지 않는다)             | 가설 기각
참               정상                            Type 1 error(제1종 오류) - 유의수준이 기준
거짓    |  Type 2 error(제2종 오류) - 검정력이 기준 | 정상


<가설 기각의 기준>
-------------------------------------------------------------
제 1종 오류(type 1 error) :
    실제는 가설이 참인데, 가설을 기각하는 오류
정확하지 않더라도 type1 error 가 적어지는 쪽으로 선택 - 유의수준을 기준으로 삼는다.



유의수준(significance level) : alpha
    제 1 종 오류가 발생할 확률의 최대 허용 한계
    1%까지는 오류가 발생해도 허용하겠다 - 유의수준 1%
    alpha = 0.05(5%), 0.01(1%)

유의수준에 따라서 가설을 기각할 것인지, 아닌지를 결정

-------------------------------------------------------------
제 2종 오류(type 2 error) :
    실제는 가설이 거짓인데, 가설을 채택하는(가설을 기각하지 않는) 오류
정확하지 않더라도 type2 error 가 적어지는 쪽으로 선택 - 검정력을 기준으로 삼는다.



검정력(power) : 1 - beta
    귀무가설의 잘못을 찾아낼 확률
    귀무가설을 기각하는 확률
    beta : 가설이 실제로는 거짓인데, 기각하지 못하는 확률
    검정력(power)이 커질수록, 제 2종 오류를 범하지 않을 확률이 커진다.

-------------------------------------------------------------
'''
import math
from lab_python.scratch06.ex06 import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial():
    """이항분포(n, p)를 정규분포로 근사했을 때, 평균, 표준편차"""
    mu  = n*p
    std = math.sqrt(n*p(1-p))
    return mu, sigma


# 확률변수가 어떤 구간 안(밖)에 존재할 확률
# P(X < b), P(X > a), P(a < X < b) = F(b) - F(a) = cdf(b) - cdf(a)
# scratch06에서 작성했던 normal_cdf 함수를 이용
# cf. 엄밀히 말하면 P(a <= X < b) = F(b) - F(a) = cdf(b) - cdf(a) 이지만 여기서는 편의상 생략한다.


# P(X < high) - 확률 변수 값이 특정 값보다 작을 확률 = cdf(high)
# 변수 = 함수 이름 저장
# 변수는 함수이름이 되었다 (즉, normal_probability_below 는 normal_cdf라는 함수가 된다.)
normal_probability_below = normal_cdf


# P(X > low) - 확률변수 값이 특정 값보다 클 확률 = 1 - P(X < low)
def normal_probability_above(low, mu=0.0, sigma=1.0):
    return 1 - normal_cdf(low, mu, sigma)


# P(low < X < high) - 확률 변수 값이 특정 범위 안에 있을 확률
#   = P(X < high) - P(X < low)
def normal_probability_between(low, high, mu=0.0, sigma=1.0):
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)


# P(X < low or X > high): 확률변수가 특정 범위 밖에 있을 확률 (low<high)
#   = 1 - P(low < X < high)
def normal_probability_outside(low, high, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(low, high, mu, sigma)

# -------- 확률 계산하는 함수들을 작성(끝)


# 확률이 주어졌을때, 그 확률에 해당하는 변수값을 찾는 역함수 생성
# 하한, 상한으로 이름을 붙여 두 변수값(왼쪽 꼬리 부분 - 하한 / 오른쪽 꼬리 부분 - 상한)을 구한다.
# 상한을 구하여 변수값을 찾는다. P(X < ub) = prob 이 주어졌을 때, 상한 ub를 찾는 함수
def normal_upper_bound(prob, mu, sigma):
    return inverse_normal_cdf(prob, mu, sigma)


# 하한을 구하여 변수값을 찾는다. P(X > lb) = prob 이 주어졌을 때, 하한 lb를 찾는 함수
# P(X < lb) = 1 - prob 이 주어졌을 때, 상한 lb를 찾는 함수와 같다.
def normal_lower_bound(prob, mu, sigma):
    return inverse_normal_cdf(1 - prob, mu, sigma)  # P(X < lb)


# 또는 평균을 중심으로 대칭하여 범위를 구하고 변수값을 찾는다.
# P(lb < X < ub) = prob 이 주어졌을 때,
# 입력한 probability 값을 포함하고, 평균을 중심으로 대칭적인 구간의 상한(ub)와 하한(lb)를 찾는 함수
def normal_two_sided_bounds(prob, mu=0.0, sigma=1.0):
    # 양쪽 끝에 해당하는 확률을 먼저 계산
    tail_prob = (1 - prob) / 2

    # 구간의 상한은 확률 tail_prob 이상을 갖는 하한을 찾으면 된다. 즉, P(X > x) = tail_prob(확률값) 이다.
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    # 또는 P(X < x) = prob + tail_prob 을 만족하는 상한을 찾으면 된다.
    upper_bound = normal_upper_bound(tail_prob + prob, mu, sigma)

    # 구간의 하한은 확률 tail_prob 이하를 갖는 상한을 찾으면 된다. 즉, P(X < x) = tail_prob(확률값) 이다.
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)

    return lower_bound, upper_bound


if __name__ == '__main__':
    # 동전을 던졌을 때 앞면이 나올 확률은 1/2(=0.5) testing(검정)
    # 동전을 1,000번 던지는 실험 - 이항 분포
    # 앞면이 나오는 기댓값 - 정규분포(np, sqrt(np(1-p))

    # 영가설(귀무가설)
    # H0: p = 1/2
    # 영가설이 참이라는 가정 아래에서,
    # 동전 앞면이 나오는 확률의 평균과 표준 편차는
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)

    # 유의 수준 5%:
    # H0이 참이지만 기각을 하는 오류를 5%는 감수
    # H0를 기각하지 않을 확률 95%의 상한과 하한을 찾음
    low, high = normal_two_sided_bounds(0.95, mu, sigma)
    print(f'low= {low}, high={high}')  # (469, 531)



