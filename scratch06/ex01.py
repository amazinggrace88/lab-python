'''
scratch06\ex01.py
확률

사건 공간(universe of events)
: 전체집합
사건(event)
: 부분집합
확률(probability)
: 공리로 정의됨. (어떠한 사건의 공간에서 특정 사건이 선택될 때 발생하는 불확실성)
                전체집합에서 사건이 차지하는 비율
'''
import random

# 동전 1개를 던지는 시행
coin = ['H', 'T']
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(coin))  # random하게 choice -> 균등분포를 가지고 있음
print(random.choice(dice))  # random하게 choice -> 균등분포를 가지고 있음


# 동전 1개는 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2임을 증명
# 방법1
prob = []
for _ in range(10000):
    prob.append(random.choice(coin))
h = prob.count('H')
t = prob.count('T')
print(f'probability of H = {h / 10000}')
print(f'probability of T = {t / 10000}')


# 방법2
prob = [random.choice(coin) for _ in range(10000)]
h = prob.count('H')
t = prob.count('T')
print(f'probability of H = {h / 10000}')
print(f'probability of T = {t / 10000}')


# 방법3 (오쌤)
trials = 10_000  # 숫자 자리수를 _로 천단위로 구분함. why? ,는 데이터 구분할 때 쓰므로
head, tail = 0, 0  # 앞면과 뒷면이 나오는 횟수를 저장할 변수

for _ in range(trials):
    random_coin = random.choice(coin)
    if random_coin == 'H':
        head += 1
    else:
        tail += 1

p_h = head / trials
p_t = tail / trials
print(f'P(H) = {p_h}')
print(f'P(T) = {p_t}')


# 동전 2개를 10,000번 던지는 실험
# 1) 앞면의 갯수가 1개일 확률
# 2) 첫번째 동전이 앞면일 확률
# 3) 적어도 1개의 동전이 앞면일 확룔
# 방법1
trials = 10_000
for _ in range(trials)
