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
제 1종 오류(type 1 error) : -> *****
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


def normal_approximation_to_binomial(n, p):
    """이항분포(n, p)를 정규분포로 근사했을 때, 평균, 표준편차"""
    mu = n*p
    std = math.sqrt(n*p*(1-p))
    return mu, std


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


def two_sided_p_value(x, mu=0, sigma=1):
    """양측 검정에서 사용하는 p-value"""
    if x > mu:
        # 만약 x가 평균보다 크다면, x보다 큰 부분이 꼬리다
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 만약 x가 평균보다 작다면, x보다 작은 부분이 꼬리다
        return 2 * normal_probability_below(x, mu, sigma)


if __name__ == '__main__':
    # 동전을 던졌을 때 앞면이 나올 확률은 1/2(=0.5) testing(검정)
    # 동전을 1,000번 던지는 실험 - 이항 분포
    # 앞면이 나오는 기댓값 - 정규분포(np, sqrt(np(1-p))

    # 영가설(귀무가설)
    # H0: p = 1/2
    # 영가설이 참이라는 가정 아래에서, 정규분포로 근사! *****
    # 동전 앞면이 나오는 확률의 평균과 표준 편차는
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)
    print(f'p=0.5 가정: mu_0 = {mu}, sigma_0 = {sigma}')

    # 유의 수준 5%:
    # H0이 참이지만 기각을 하는 오류를 5%는 감수
    # H0를 기각하지 않을 확률 95%의 상한과 하한을 찾음
    low, high = normal_two_sided_bounds(0.95, mu, sigma)
    print(f'low= {low}, high={high}')  # (469, 531)


    # 대립가설
    print()
    print('H0: p = 1/2 가정')
    print('=========================================')
    # 대립가설 양측검정
    print('<대립가설 - 양측검정 방법>')
    # H0: p = 1/2 가정
    # H1: p != 1/2 (1/2가 아닌 것은 모두)
    # 유의수준(alpha): 영가설이 참인데 가설을 기각할 가능성
    # Beta: 제 2종 오류: 영가설이 거짓인데 가설을 기각하지 않을 가능성 (거짓인 것을 밝혀내지 못할 확률)
    # 검증력: 1 - Beta : 제 2종 오류를 범하지 않을 확률 (높을수록 검증력 좋다)

    # 만약 동전 앞면이 나오는 확률이 1/2이 아니라고 가정하면
    # 동전 앞면이 나올 확률을 0.5 + 매우 작은 값(0.05)라고 가정했을 때, 정규분포 근사 후 평균/표준편차
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    print(f'p=0.55 가정 : mu_1 = {mu_1}, sigma = {sigma_1}')

    # 대립가설 : 틀린 가정(p = 0.5라는 가정에서 95%구간이 p=0.55라는 가정)에서 나올 확률
    beta = normal_probability_between(low, high, mu_1, sigma_1)
    print('beta(제2종 오류) =', beta)  # 틀린 가정을 맞다고 확신할 확률
    power = 1 - beta
    print('power(검증력) =', power)  # 틀린 가정을 틀렸다고 확신할 확률

    # 틀린 가정을 맞다고 확신할 확률
    # p = 0.5 의 pdf 그래프와 p = 0.55 의 pdf 그래프의 겹치는 부분이 beta. (더 자세히 알아볼 것)
    print('----------------------------------------')
    # p = 0.45 라고 가정 (양측검정 - 사이에 들어가는 값이 귀무가설에 포함되는 확률을 계산하는 것)
    mu_2, sigma_2 = normal_approximation_to_binomial(1000, 0.45)
    print(f'p=0.45 가정 : mu_2 = {mu_2}, sigma = {sigma_2}')
    beta = normal_probability_between(low, high, mu_2, sigma_2)
    print('beta(제2종 오류) =', beta)
    power = 1 - beta
    print('power(검증력) =', power)
    # p = 0.55 와 p = 0.45는 똑같은 검증력을 가진다.

    # 대립가설
    print()
    print('=========================================')
    # 대립가설 단측검정
    # 대립가설 단측검정
    print('<대립가설 - 단측검정 방법>')
    print('H0: p <= 1/2 가정')
    # H0: p <= 0.5 귀무가설
    # H1: p > 0.5
    # p=0.5일 때 유의수준 5%의 upper bound 구간
    high = normal_upper_bound(0.95, mu, sigma)
    print('유의 수준 5% 상한 =', high)
    beta = normal_probability_below(high, mu_1, sigma_1)
    print('단측검정: beta =', beta)
    power = 1 - beta
    print('단측 검정 검정력 = ', power)
    print('----------------------------------------')

    # H0: p >= 0.5
    print('H0: p >= 1/2 가정')
    # H1: p < 0.5  (i.e. p = 0.45)
    # p=0.5를 가정한 정규 분포에서 유의 수준 5% lower bound를 찾음
    # beta = lower bound 보다 클 확률
    low = normal_lower_bound(0.95, mu,sigma)
    print('low =', low)
    # beta : p = 0.45 를 가정한 정규분포에서 lower bound 보다 클 확률
    beta = normal_probability_above(low, mu_2, sigma_2)
    power = 1 - beta
    print('단측 검정력 = ', power)

    print()
    print('=========================================')
    # p-value: H0이 참이라고 가정할 때, 실험에서 관측된 값보다 더 극단적인 값(우연히 발생한 값)이 관측될 확률
    # 양측검정
    print('<p-value-양측검정 방법>')
    # p-value(극단적인 값이 나올 확률)이 유의수준(5%)보다 더 작다면,
    # 그 값은 우연히 발생한 값이라고 생각할 수 있다.(우연히 발생한 값이라고 생각할 수 있다.)
    # H0 기각
    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다.
    # p-value가 유의수준보다 크다면, 그 값은 우연히 발생할 수 없다(우연이 아니라 필연적으로 발생하였다.)
    # H0 기각하지 않음
    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다.
    p_value = two_sided_p_value(530, mu, sigma)
    print('p-value =', p_value)
    # 0.057 > 0.05(유의수준) : p-value가 유의수준보다 크다.
    # 허용할 수 있는 오차범위보다 크므로, 우연히 발생하였다고 생각할 수 없으므로 H0를 기각하지 않는다. (채택한다)

    print('----------------------------------------')
    # 단측검정
    print('<p-value-단측검정 방법>')
    print('H0: p <= 1/2 가정')
    # H0: p <= 0.5 귀무가설
    # H1: p > 0.5
    # p=0.5를 가정한 정규 분포에서 유의 수준 5% lower bound 를 찾음
    low = normal_lower_bound(0.95, mu, sigma)
    print('low =', low)
    # beta: p=0.45를 가정한 정규 분포에서 lower bound 보다 클 확률
    beta = normal_probability_above(low, mu_2, sigma_2)
    power = 1 - beta
    print('단측 검정력 =', power)  # 0.9363

    # p-value: H0이 참이라고 가정할 때,
    # 실험에서 관측된 값보다 더 극단적인 값이 관측될 확률
    # p-value(극단적인 값이 나올 확률)이 유의 수준(5%)보다 작다면, 그 값은 우연히 발생한 값이라고 생각할 수 있다.
    # -> H0 기각함
    # p-value 가 유의 수준보다 크다면, 그 값은 우연히 발생한 값이라고 말할 수 없다.
    # -> H0를 기각하지 않음(채택)

    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다.
    # H0: p = 0.5, H1: p != 0.5
    p_value = two_sided_p_value(530, mu, sigma)
    print(p_value)  # 0.057 > 0.05(유의수준)

    # 동전을 1000번 던져서 앞면이 525번 발생
    # -> 앞면의 확률 p = 525/1000 = 0.525
    p_bar = 525 / 1000
    mu = p_bar  # 모집단의 평균을 실험값의 평균으로 대체
    # 표본의 표준편차로 모집단의 표준 편차를 추정
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000)
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(bounds)  # (0.494, 0.555)
    # 실험을 통해서 찾은 95% 신뢰 구간
    # 진짜 p값(앞면이 나올 진짜 확률)은 위 구간에 포함된다
    # 95% 확신할 수 있다.

    # 동전을 1000번 던졌을 때, 540번 앞면 발생
    p_bar = 540 / 1000  # 표본 평균
    mu = p_bar  # 모집단 평균 = 표본 평균
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000)  # 모집단 표준편차
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(bounds)  # (0.509, 0.570)
    # p = 0.5인 가설은 신뢰 구간에 포함되지 못함.

    # A/B Test
    # N_a = 1000, n_a = 200, N_b = 1000, n_b = 180 (또는 150)
    z1 = a_b_test_statistic(1000, 200, 1000, 180)
    print('z1 =', z1)  # -1.14
    p_value_1 = two_sided_p_value(z1)
    print('p-value 1 =', p_value_1)  # 0.254
    # p-value > 0.05
    # A와 B의 차이가 우연히 발생할 확률 유의 수준보다 높다
    # -> A와 B가 차이가 있다고 말할 수 없다.
    # -> A와 B가 차이가 있다는 가설을 기각

    z2 = a_b_test_statistic(1000, 200, 1000, 150)
    print('z2 =', z2)  # -2.94
    p_value_2 = two_sided_p_value(z2)
    print('p-value 2 =', p_value_2)  # 0.003
    # p-vale < 0.05
    # -> A와 B의 차이가 우연히 발생할 확률이 유의 수준보다 낮다
    # -> A와 B의 차이가 있다고 말할 수 있다.
    # -> A와 B의 차이가 있다는 가설을 채택

