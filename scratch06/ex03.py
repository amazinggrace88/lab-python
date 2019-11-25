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
import random

kid = ('boy', 'girl')
trials = 10_000
older_girl = 0  # 첫째가 딸인 경우 P(A)
both_girl = 0  # 두 아이가 모두 딸인 경우 P(B)
either_girl = 0  # 두 자녀 중 최소 한 명이 딸인 경우 P(C)

for _ in range(trials):
    older = random.choice(kid)
    younger = random.choice(kid)
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girl += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

# 첫째가 딸일 경우에 두 자녀 모두 딸일 경우의 확률
p1 = both_girl/older_girl
print(f'P(both|older) : {p1}')
# 적어도 한 명이 딸일 경우에 두 자녀 모두 딸일 확률
p2 = both_girl/either_girl
print(f'P(both|either) : {p2}')

