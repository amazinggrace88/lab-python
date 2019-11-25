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
from lab_python.scratch04.ex01 import dot
from collections import Counter
'''
동전 2개를 던지는 실험(10,000번)
1) 앞면의 개수가 1개일 확률 1/2 (HT, TH)
2) 첫번째 동전이 앞면일 확률 1/2 (HH, HT)
3) 적어도 한 개의 동전이 앞면일 확률 3/4 (HH, HT, TH)
= 1 - (2개의 동전이 뒷면일 확률) = 여사건

동전 3개를 던지는 실험(10,000번)
앞면의 개수가 1개일 확률 3/8 (HTT, THT, TTH) 

'''

# 동전 1개를 던지는 시행
coin = ['H', 'T']
dice = [1, 2, 3, 4, 5, 6]
trials = 10_000
# print(random.choice(coin))  # random 하게 choice -> 균등분포를 가지고 있음
# print(random.choice(dice))  # random 하게 choice -> 균등분포를 가지고 있음


# 실험의 결과를 저장하기 (오쌤 정답)
def experiment(type, n, t):
    """
    실험의 결과를 [ [ [], [], [] ],/  [ [], [], [] ],/  [ [], [], [] ] ]

    :param type: 실험 타입(동전던지기 or 주사위 던지기, ..)
    :param n: 실험의 개수
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []  # 실험 결과를 저장
    for _ in range(t):  # 실험 횟수만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 실험 갯수만큼 반복
            rand = random.choice(type)  # H or T
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 저장
        cases.append(tuple(case))
    return cases


coin_exp = experiment(coin, 2, 10_000)
coin_exp_three = experiment(coin, 3, 10_000)
dice_exp = experiment(dice, 2, 10_000)
# print('coin experience = ', coin_exp[0:10])  # 10개씩 출력
# print('three coin experience = ', coin_exp[0:10])
# print('dice experience = ', dice_exp[1:10])

# counter 이용하여 사건 개수 찾기 (오쌤 정답)
coin_event_counts = Counter(coin_exp)  # list 는 Counter 를 쓸수가 없다. why? TypeError: unhashable type
coin_event_counts_three = Counter(coin_exp_three)
dice_event_counts = Counter(dice_exp)
# print('event all coin counts = ', coin_event_counts)
# print('event all three coin counts = ', coin_exp_three)
# print('event all dice counts = ', dice_event_counts)
# Counter (from collections import Counter)


# hash algorithm : 정렬을 위한 알고리즘 (hashable)
# list 의 list 의 갯수는 셀 수 없음! why? 그 안의 원소들이 바뀔 수 있다. 나중에 순서가 바뀔 수 있으므로 정렬할 수 없다.
# 튜플로 바꿔주어야 정렬이 가능하다. -> experiment 함수에서 각 결과를 tuple로 결과 후 저장
# 튜플은 추가 자체가 안되기 때문에 ()로 시작하여 .append()가 불가능함. 따라서 [list]로 시작하여 ()변환할 것.
# [{}] list 안의 dict 도 갯수를 셀 수 없음


# H 찾아주는 함수 만들기
def how_many_heads(x):
    counter = Counter(x)
    print(counter)
    return counter['H']
# dict를 주었을 때 dict 안 tuple ('H', 'T') 가 x가 된다. H = {0, 1, 2} 개가 된다.


# case 의 갯수를 센다.
num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_heads(ev) == 1:
        num_of_cases += cnt
p_h1 = num_of_cases / trials
print('P(앞면이 1개일 확률) = ', p_h1)


num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if ev == ('H', 'H') or ev == ('H', 'T'):
        num_of_cases += cnt
p_first_h = num_of_cases / trials
print('P(첫번째 동전이 앞면일 확률) = ', p_first_h)


num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_heads(ev) == 1 or how_many_heads(ev) == 2:
        num_of_cases += cnt
p = num_of_cases / trials
print('P(적어도 1개가 앞면일 확률) = ', p)


# 여사건 이용
num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_heads(ev) == 0:
        num_of_cases += cnt
p = num_of_cases / trials
print('P(적어도 1개가 앞면) =', 1 - p)


# H = 1, T = 0 약속 -> coin = [1, 0]
coin2 = [1, 0]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2):
        if 1 == random.choice(coin2):
            num_of_heads += 1
    cases.append(num_of_heads)
print(cases[0:10])


# 주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률
# (2, 6), (3, 5), (4, 4), (5, 3), (6, 2) : 5 / 36
# 나의 정답
trials = 10_000
for _ in range(trials):
    num_of_sums = 0
    for key, value in dice_event_counts.items():
            if ( key[0] + key[1] ) == 8:
                num_of_sums += 1
            # if key == (2, 6) or key == (3, 5) or key == (4, 4) or key == (5, 3) or key == (6, 2):
            #     num_of_sums += 1

print('주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률 = ', num_of_sums / 36 )


# 정답 (오쌤)
dice_exp = experiment(dice, 2, 10_000)
# print(dice_exp[0:5])

event_counts = Counter(dice_exp)
print('주사위의 경우의 수 = ', len(event_counts))  # 36개 나옴 -> 6*6개 나옴
print(event_counts)

num_of_cases = 0
for ev, cnt in event_counts.items():
    # if ev[0] + ev[1] == 8:
    if sum(ev) == 8:  # why? sum(iterable) => so we can put list/tuple/etc..
        num_of_cases += cnt
p = num_of_cases / trials
print('주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률 = ', p, 5/36)
# lambda 식 써보기


# 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률
# 1 - 여사건(두 눈이 모두 홀수가 나올 확률) : 33 / 36
# 나의 정답
for _ in range(trials):
    num_of_sums_even = 0
    for key, value in dice_event_counts.items():
        if (key[0] % 2 == 0) or (key[1] % 2 == 0):
            num_of_sums_even += value

print('주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 = ', (num_of_sums_even) / trials)

# 오쌤 정답
num_of_cases = 0
for ev, vnt in event_counts.items():
    if ev[0] % 2 == 0 or ev[1] % 2 == 0:
        num_of_cases += vnt
p = num_of_cases / trials
print('주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 = ', p, 27/36)



'''
여기서부터 내가 만든 정답! 
'''
# 나의 정답
# 동전 1개는 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2임을 증명
# 방법1
prob = []
trials = 10_000
for _ in range(trials):
    prob.append(random.choice(coin))
h = prob.count('H')
t = prob.count('T')
# print(f'probability of H = {h / 10000}')
# print(f'probability of T = {t / 10000}')


# 방법2
prob = [random.choice(coin) for _ in range(trials)]
h = prob.count('H')
t = prob.count('T')
# print(f'probability of H = {h / 10000}')
# print(f'probability of T = {t / 10000}')


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
# print(f'P(H) = {p_h}')
# print(f'P(T) = {p_t}')


# 동전 2개를 10,000번 던지는 실험
# 1) 앞면의 갯수가 1개일 확률
# 2) 첫번째 동전이 앞면일 확률
# 3) 적어도 1개의 동전이 앞면일 확룔


data_coin_1 = []
data_coin_2 = []

for _ in range(trials):
    data_coin_1.append(random.choice(coin))
    data_coin_2.append(random.choice(coin))

# 1) 앞면의 갯수가 1개일 확률
# 방법1
h_1 = 0
for x, y in zip(data_coin_1, data_coin_2):
    if x == 'H' and y == 'T':
        h_1 += 1
    elif x == 'T' and y == 'H':
        h_1 += 1

# print(f'P(coin count = 1) = {h_1 / trials}')

# 방법2
coin_2 = [x + y for x, y in zip(data_coin_1, data_coin_2)]
HTTH = 0
for i in coin_2:
    if i == 'HT' or i == 'TH':
        HTTH += 1

# print(f'P(coin count = 1) = {HTTH / trials}')
# print(coin_2)

# 2) 첫번째 동전이 앞면일 확률
# 방법1
h_first = 0
for x, y in zip(data_coin_1, data_coin_2):
    if x == 'H':
        h_first += 1

# print(f'P(first head) = {h_first / trials}')

# 방법2
H_first = 0
for i in coin_2:
    if i == 'HH' or i == 'HT':
        H_first += 1

# print(f'P(first head) = {H_first / trials}')


# 3) 적어도 1개의 동전이 앞면일 확룔
# 방법1
h_at_least = 0
for x, y in zip(data_coin_1, data_coin_2):
    if x == 'H' or y == 'H':
        h_at_least += 1

# print(f'P(at least 1 head) = {h_at_least / trials}')

# 방법2
H_at_least = 0
for i in coin_2:
    if i == 'HH' or i == 'HT' or i == 'TH':
        H_at_least += 1

# print(f'P(at least 1 head) = {H_at_least / trials}')


# 동전 3개를 10,000번 던지는 실험
# 앞면의 갯수가 1개일 확률 3/8 (HTT, THT, TTH)
data_coin_3 = []
for _ in range(trials):
    data_coin_3.append(random.choice(coin))

# 방법1
ohfco = 0
for x, y, z in zip(data_coin_1, data_coin_2, data_coin_3):
    if x == 'H' and y == 'T' and z == 'T':
        ohfco += 1
    elif x == 'T' and y == 'H' and z == 'T':
        ohfco += 1
    elif x == 'T' and y == 'T' and z == 'H':
        ohfco += 1

# print(f'P(1 head for 3 coins) = {ohfco / trials}')

# 방법2
coin_3 = [x + y + z for x, y, z in zip(data_coin_1, data_coin_2, data_coin_3)]
ohfct = 0
for i in coin_3:
    if i == 'HTT' or i == 'THT' or i == 'TTH':
        ohfct += 1

# print(f'P(1 head for 3 coins) = {ohfct / trials}')
