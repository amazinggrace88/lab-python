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
# 코딩으로 구현


# 동전 3개를 던질 때, 확률변수 X를 동전의 앞면의 갯수라고 하자.
# X = 0, 1, 2, 3
# 동전 3개를 10_000번 던지는 실험을 하여, 각 변수들의 확률을 알아내자.
# P(X=0) = 1/8, P(X=1) = 3/8, P(X=2) = 3/8, P(X=3) = 1/8
import random
from collections import Counter


# 나의 정답
range(3)  # 0~3까지 모든 확률변수
coin = [1, 0]  # 앞 1 뒤 0
trials = 10_000


# 동전 3개를 10,000번 던질 때, 동전 앞면의 갯수만 저장하자!
def experience(n, t):
    exper = []
    for j in range(t):
        all = []
        for _ in range(n):
            rand = random.choice(coin)
            all.append(rand)
        exper.append(tuple(all))
    return exper


a = experience(3, 10000)
print(a[0:20])

a_num = Counter(a)
print(a_num)
# : dict의 key가 (0, 0, 1) 정도로 되어 있는데, tuple의 숫자를 합칠 수는 없을까? 생각해보기


# 오쌤 정답
# 동전 3개를 10,000번 던질 때, 동전 앞면의 갯수만 저장하자!
# step 1. 변수 정의
coin = (1, 0)  # 앞 1 뒤 0
trials = 10_000
experiments = []

# step 2. for문 사용 : 동전 갯수를 list로 변환
for _ in range(trials):
    heads = 0
    for _ in range(3):
        heads += random.choice(coin)
    experiments.append(heads)
print(experiments[0:10])

# step 3. Counter 사용 : list 안의 동전 앞면 갯수 통계 출력
head_counts = Counter(experiments)  # 0, 1, 2, 3의 갯수를 세준다.
print(head_counts)

# step 4. for 문 사용 : 기댓값 계산
expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * (cnt / trials)
print(f'expected value = {expected_value}')


# 주사위 눈의 기댓값
dice = range(6)
experiments = [random.choice(dice) for _ in range(trials)]
print(experiments[0:10])
head_dice = Counter(experiments)
print(head_dice)
expected_dice = 0
for x, cnt in head_dice.items():
    expected_dice += x * (cnt / trials)
print(f'주사위 눈의 기댓값 = {expected_dice}')

