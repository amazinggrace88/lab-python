import random
from collections import Counter

dice = [1, 2, 3, 4, 5, 6]
trials = 10_000


def experiment(type, n, t):
    """
    실험의 결과를 [ [ [], [], [] ],/  [ [], [], [] ],/  [ [], [], [] ] ]

    :param type: 실험 타입 (동전던지기 or 주사위 던지기, ..)
    :param n: 실험의 개수
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t):  # 실험 횟수만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 실험 갯수만큼 반복
            rand = random.choice(type)  # H or T
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 저장
        cases.append(tuple(case))
    return cases


dice_exp = experiment(dice, 2, 10_000)

dice_event_counts = Counter(dice_exp)

for _ in range(trials):
    num_of_sums_even = 0
    for key, value in dice_event_counts.items():
        if (key[0] % 2 == 0) or (key[1] % 2 == 0):
            num_of_sums_even += value

print('주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 = ', (num_of_sums_even) / trials)



# ex02
'''
사건의 종속성 vs 독립성

사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속 사건(dependent event)
사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 사건 B는 독립 사건(independent event)

동전 2개를 던지는 경우,
A: 첫번째 동전이 앞면
B: 두번째 동전이 뒷면
C: 두 동전 모두 앞면

A와 B는 독립 사건
A와 C는 종속 사건

P(A) = 사건 A 가 일어날 확률
P(B) = 사건 B 가 일어날 확률
P(C) = 사건 C 가 일어날 확률
P(A, B) = 사건 A와 사건 B의 교집합이 일어날 확률

P(A, B) = P(A) * P(B) 이 성립하면, 두 사건은 독립 사건.
'''

# 자녀가 2명인 경우 - 전체사건
# 사건 A : 첫째가 딸인 경우
# 사건 B : 둘째가 아들인 경우
# 사건 C :  둘 다 딸인 경우
# A와 B가 독립사건, A와 C는 종속사건임을 증명


# 오쌤 정답
# for 문 함수로 (메소드로) 만들기 -> refactor -> extract -> method
child = ('boy', 'girl')
trials = 10_000

def baby_bg():
    # assignment 를 해주고 나서
    # for 문을 돌려야 한다.
    event_a = 0
    event_b = 0
    event_a_b = 0
    event_c = 0
    event_a_c = 0
    for _ in range(trials):
        first = random.choice(child)
        second = random.choice(child)
        if first == 'girl':
            event_a += 1
        if second == 'boy':
            event_b += 1
        if first == 'girl' and second == 'boy':
            event_a_b += 1
        if first == 'girl' and second == 'girl':
            event_c += 1
            event_a_c += 1
    return event_a, event_b, event_c, event_a_b, event_a_c

# 함수 리턴값이 여러개이면, 여러개 리턴값을 지정해주고 함수를 호출한다.


event_a, event_a_b, event_a_c, event_b, event_c = baby_bg()

p_a = event_a / trials
p_b = event_b / trials
p_a_b = event_a_b / trials
p_c = event_c / trials
p_a_c = event_a_c / trials

print(f'P(A,B) = {p_a_b}, P(A)P(B) = {p_a * p_b}')
print(f'P(A,C) = {p_a_c}, P(A)P(C) = {p_a * p_c}')

# 리팩토링 하다(Refactoring) - 일련의 리팩토링을 적용하여 겉으로 보이는 동작의 변화 없이 소프트웨어 구조를 바꾸다.
# 소프트웨어를 보다 쉽게 이해할 수 있고, 적은 비용으로 수정할 수 있도록 겉으로 보이는 동작의 변화 없이 내부 구조를 변경하는 것



# ex03
'''
조건부 확률(Conditional Probability)

P(A) = 사건 A 가 일어날 확률
P(B) = 사건 B 가 일어날 확률
P(C) = 사건 C 가 일어날 확률
P(A, B) = 사건 A와 사건 B의 교집합이 일어날 확률
P(A|B) = 사건 B가 일어났을 때, 사건 A가 일어날 확률 ( = P(A, B) / P(B) )

if A와 B가 독립 사건이면, P(A, B)  = P(A)P(B)
   P(A|B) = P(A)P(B) / P(B) = P(A)

조건부 확률 예시 : 2 자녀 가정
1 각아이가 딸이거나 아들일 확률은 동일하다.
2. 둘째의 성별은 첫째의 성별과 독립이다.
A 사건 : 첫째가 딸인 경우 P(A) = 2/4
B 사건 : 두 아이가 모두 딸인 경우 P(B) = 1/4
C 사건 : 두 자녀 중 최소 한 명이 딸인 경우 P(C) = 3/4

P(A,B) = 1/4
P(A,C) = 2/4
첫째가 딸인 경우에 두 아이가 모두 딸일 확률
P(B|A) = P(B,A)/P(A) = P(B)/P(A) = 1/2
첫째가 딸일 경우에 최소 한 명이 딸인 경우
P(C|A) = P(C,A)/P(A) = (1/2) / (1/2) = 1
적어도 한 명이 딸일 경우에 두 자녀 모두 딸일 경우
P(B|C) = P(B,C)/P(C) = (1/4) / (3/4) = 1/3
'''

# 조건부확률 구현
import random

kid = ('boy', 'girl')
trials = 10_000
older_girl = 0  # 첫째가 딸인 경우 P(A)
both_girl = 0  # 두 아이가 모두 딸인 경우 P(B)
either_girl = 0  # 두 자녀 중 최소 한 명이 딸인 경우 P(C)

for _ in range(trials):  # trials 를 꼭 넣어야함
    first = random.choice(kid)
    second = random.choice(kid)
    if first == 'girl':
        older_girl += 1
    if first == 'girl' and second == 'girl':
        both_girl += 1
    if first == 'girl' or second == 'girl':
        either_girl += 1

p1 = both_girl / older_girl
print(f'P(both|older) : {p1}')
p2 = both_girl / either_girl
print(f'P(both|either) : {p2}')



# ex04
'''
베이즈 정리(Bayes's Theorem)

: 사건 F가 발생했다는 가정 하에 사건 E가 발생할 확률을 활용하여 사건 E가 발생할 확률을 구하는 과정
    사후확률을 활용하여 사전확률을 구한다.
P(A|B) = P(A,B)/P(B)
       = P(B,A)/P(B)
       = P(B|A)P(A)/P(B)
       = P(B|A)P(A)/(P(A,B) + P(B,~A)) *전체 사건이 A와 ~A로만 이루어졌을 경우에 전개 가능

10，000명 중에 1 명이 걸리는 질병(Disease):
    P(D) = 1/10000 = 0.01% = 0.0001
    P(~D) = 1 - P(D) = 9999/10000 = 99.99% = 0.9999

질병이 있는 경우 '양성', 질병이 없는 경우 '음성'이라고 판단하는 검사의 정확도 99%
    질병이 있는 경우에 양성인 경우
    P(T|D) = 99/100 = 99%
    질병에 걸리지 않는 사람을 양성이라고 한 경우
    P(T|~D) = 1/100 = 1%

양성 판정인 경우 실제로 병에 걸렸을 확률
    P(D|T) = P(T|D)P(D) / [P(T|D)P(D) + P(T|~D)P(~D)]
           =  0.99*0.0001 / [0.99*0.0001 + 0.01*0.9999]
           =  0.98%
why?
    P(D|T) = P(D,T)/P(T)
           = P(T|D)P(D)/P(T)
           = P(T|D)P(D)/[P(T|D)P(D) + P(T|~D)P(~D)]
'''



# ex05
'''
확률변수(random variable)
    어떤 확률 분포와 연관되어 있는 변수

    동전 1개를 던지는 확률분포에서 동전 앞면의 갯수 X를 확률변수라고 생각할 수 있다.
    동전 앞면의 갯수 X
    P(X=1) = 1/2
    P(X=0) = 1/2

기댓값(Expected Value)
    확률변수 * 확률변수의 확률 의 합
    \Sigma_{i=1}^{n} X_i*P(X = X_i) (이산인 경우)
    전체 데이터를 갯수로 나눠준 것 : 평균
    확률변수의 확률을 해당 확률변수의 값으로 가중평균한 값
    ex_동전 1개를 던질 때, 동전 앞면의 기댓값
    E(X) = 1 * 1/2 + 0 * 1/2 = 1/2 = 0/5

확률분포
    확률변수들의 분포
    1. 이산형 분포 (확률변수의 갯수가 이산인 경우)
    2. 연속형 분포 (확률변수의 갯수가 연속인 경우)

결합확률분포
    확률변수 X, Y,, 등 여러 확률변수의 분포

'''
import random
from collections import Counter

coin = [1, 0]
trials = 10_000


def experience(n, t):  # n : 1번의 실험에서의 시행 횟수 t : 실험 횟수
    all = []  # list 를 먼저 만든다.
    for j in range(t):  # 범위를 주어서 합을 [] 안에 append
        one_time = 0
        for i in range(n):
            rand = random.choice(coin)
            one_time += rand
        all.append(one_time)
    return all


a = experience(3, 10000)
print(f'동전 실험 결과 = {a[0:20]}')

a_num = Counter(a)  # Counter로 통계량 추출
print(f'동전 실험 결과의 통계 = {a_num}')
# : dict의 key가 (0, 0, 1) 정도로 되어 있는데, tuple의 숫자를 합칠 수는 없을까? 생각해보기


# 오쌤 정답
# 동전 3개를 10,000번 던질 때, 동전 앞면의 갯수만 저장하자!
# step 1. 변수 정의
coin = (1, 0)  # 앞 1 뒤 0인 tuple을 만들자.
trials = 10_000
experiments = []  # [] list로 만들어야 변경이 가능하지?! - tuple은 안되나..?

# step 2. for문 사용 : 동전 갯수를 list로 변환 (def 를 사용하지 않았다 - 나의 정답과의 차이점)
for i in range(trials):
    coin_count = 0
    for _ in range(3):
        rand = random.choice(coin)
        coin_count += rand
    experiments.append(coin_count)
print('3번의 시행 중 앞면의 갯수의 합들의 리스트 = ', experiments[0:20])

# step 3. Counter 사용 : list 안의 동전 앞면 갯수 통계 출력
coin_count_stats = Counter(experiments)
print('앞면의 갯수의 통계량 = ', coin_count_stats)

# step 4. for 문 사용 : 기댓값 계산
expected_value = 0
for k, v in coin_count_stats.items():
    expected_value += k * (v / trials)
print('expected value = ', expected_value)


# 주사위 눈의 기댓값 (실험 1번, 시행 1번)
dice = (1, 2, 3, 4, 5, 6)
print('dice = ', dice)
experiments = [random.choice(dice) for _ in range(trials)]
print('실험 1번 = ', experiments[0:20])
dice_stats = Counter(experiments)
print('실험 1번의 통계량 = ', dice_stats)
expected_dice = 0
for k, v in dice_stats.items():
    expected_dice += k * (v/trials)
print(f'주사위 눈의 기댓값 = {expected_dice}')



# ex06
'''
연속확률분포
    1) 확률밀도함수 (Probability Density Function : PDF)
    : f(x)
    : f(x)={\frac  {d}{dx}}F(x)
    : p(a <= x < b) = integral from a to b [pdf(x)dx]

    2) 누적분포함수 (Cumulative Destribution Function : CDF)
    : \int_{a}^{b}f(x)dx
    : F(x)=\int _{{-\infty }}^{x}f(x)dx
    : cdf(x) = P(x <= b)
    (확률밀도함수의 적분값이 누적분포함수)
    : p(a <= x < b) = F(b) - F(a)


간단한 실습
1. 균등분포 그래프로 나타내기
2. 정규분포 그래프로 나타내기
* Scipy 패키지를 사용하여서도 구현해보기
'''
import math
from matplotlib import pyplot as plt


# 1. 균등분포 그래프로 나타내기
# 균등분포의 확률밀도함수(Probability Density Function)
def uniform_pdf(x):
    return 1 if 0<= x < 1 else 0


# 균등분포의 누적분포함수(Cumulative Distribution Function)
def uniform_cdf(x):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    else:
        return 1



# 2. 정규분포 그래프로 나타내기
# 정규분포의 확률밀도함수(Probability Density Function)
def normal_pdf(x, mu=0.0, sigma=1.0):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2/ 2/ sigma ** 2) / (sqrt_two_pi * sigma))


# 정규분포의 누적확률변수(Cumulative Distribution Function)
def normal_cdf(x, mu=0.0, sigma=1.0):
    """
    평균이 mu이고, 표준편차가 sigma인 정규분포의 누적 확률 변수
    math.erf() 함수(error function-오차함수 : 정규분포의 누적분포함수와 같으며 초월함수)를 이용하여 구현
    """
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2


# 누적확률을 알고 있을 때, 확률변수를 찾아라 percentile!
# 역함수를 이용하자.
# ex : y = 2^x <-> x = {\log_2 y}

def inverse_normal_cdf(p, mu=0.0, sigma=1.0, tolerance = 0.00001):
    if mu != 0.0 or sigma != 1.0:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)  # z-score 정규화
    low_z, low_p = -10,0, 0
    high_z, high_p = 10.0, 1
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2.0
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            high_z, high_p = mid_z, mid_p
        else:
            break
    return mid_z


# 이산 quentile함수와 유사한 개념이지만, 연속에서는 모든 확률변수가 연속이므로 이진 정렬 알고리즘을 사용하여 x를 구한다.
# binary search - 이진 정렬 알고리즘 - 스무고개 게임과 같은 논리로 작동한다.




if __name__ == '__main__':
    xs = [x / 10 for x in range(-50, 51)]
    ys = [uniform_pdf(x) for x in xs]
    # ys : xs라는 범위 중 하나인 x를 uniform_pdf(x) 함수에 넣어 0<=x<1이면 1, 아니면 0을 출력하도록 한 list
    plt.plot(xs, ys)
    plt.title('uniform distribution pdf')
    plt.show()

    ys_cdf = [uniform_cdf(x) for x in xs]
    plt.plot(xs, ys_cdf)
    plt.title('uniform distribution cdf')
    plt.show()