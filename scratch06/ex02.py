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




# 나의 정답
import random
from collections import Counter

trials = 10_000
baby = ['M', 'F']


def experience_baby(type, n, t):
    """
    실험의 결과를 리스트의 리스트로 만든다.

    :param type: 실험 타입
    :param n: 실험의 갯수 (baby의 유형 2가지)
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []
    for _ in range(t):
        case = []
        for _ in range(n):
            rand = random.choice(type)
            case.append(rand)
        cases.append(tuple(case))
    return cases


# list 안 list에 실험 결과 생성
new = experience_baby(baby, 2, trials)
print(new[0:10])


# Counter 를 사용하여 실험결과의 통계 생성
new_count = Counter(new)
print(new_count)


# P(A) = 첫째가 딸인 경우
p_a = 0
for k, v in new_count.items():
    if k[0] == 'F':
       p_a += v
PA = p_a / trials
print(f'P(A) = {PA}')


# P(B) = 둘째가 아들인 경우
p_b = 0
for k, v in new_count.items():
    if k[1] == 'M':
       p_b += v
PB = p_b / trials
print(f'P(B) = {PB}')


# P(C) = 둘 다 딸인 경우
p_c = 0
for k, v in new_count.items():
    if k[0] == 'F' and k[1] == 'F':
       p_c += v
PC = p_c / trials
print(f'P(C) = {PC}')


# P(A, B) = 첫째가 딸인 경우와 둘째가 아들인 경우의 교집합
p_a_b = 0
for k, v in new_count.items():
    if k[0] == 'F' and k[1] == 'M':
        p_a_b += v
PAB = p_a_b / trials
print(f'P(A, B) = {PAB}')


# P(A, C) = 첫째가 딸인 경우와 둘 다 딸인 경우의 교집합
p_a_c = 0
for k, v in new_count.items():
    if k[0] == 'F' and (k[0] == 'F' and k[1] == 'F'):
       p_a_c += v
PAC = p_a_c / trials
print(f'P(A, C) =  {PAC}')


# P(A)*P(B) != P(A,B) 증명
print(f'P(A)*P(B) = {PA * PB}')
print(f'P(A,B) = {PAB}')
print('P(A, B) = P(A) * P(B) 이 성립하면, 두 사건은 독립 사건이므로 두 사건은 독립사건이다.')


# P(A)*P(C) = P(A,C) 증명
print(f'P(A)*P(C) = {PA * PC}')
print(f'P(A,C) = {PAC}')
print('P(A, C) = P(A) * P(C) 이 성립하지 않으면, 두 사건은 독립 사건이 아니므로 두 사건은 종속 사건이다.')


# 오쌤 정답
# for 문 함수로 (메소드로) 만들기 -> refactor -> extract -> method
child = ('boy', 'girl')
trials = 10_000


def baby_bg():
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
            # 사건 A와 사건 B의 교집합
            event_a_b += 1
        if first == 'girl' and second == 'girl':
            event_c += 1
        if first == 'girl' and (first == 'girl' and second == 'girl'):
            # 사건 A와 사건 C의 교집합
            event_a_c += 1
    return event_a, event_a_b, event_a_c, event_b, event_c

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
