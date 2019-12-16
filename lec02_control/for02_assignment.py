# coding=utf-8
"""
assignment
"""
# import 문은 항상 맨 위에 쓰는 것이 원칙.
import numpy as np
from math import sqrt

#scores = 빈 리스트 선언
scores = []
# scores[1] = 99 error
# scores.append() 로만 추가 가능

# 난수 선언(0<=x<=100)
for i in range(10):
    x = np.random.randint(0, 101) #100까지 나와야 하므로
    scores.append(x)
print(scores)
# i 는 for 문에서 사용되지 않지
# 만 문법 때문에 필요하다. (비워둘 수는 없으니 _를 쓰는 것을 허용함)
# x를 합쳐주자.
for _ in range(10):
    scores.append(np.random.randint(0, 101))
print(scores)

# list 에 저장된 시험점수 10개의 총점을 계산, 출력
total = 0
for score in scores:
    total += score  # 더해야 하기 때문에, 더할 대상이 필요하므로 total 을 먼저 지정해주어야 함.
print(f'총점 : {total}')
# or
print(f'총점 2 : {sum(scores)}')  # 중괄호 안에 함수를 쓸 수 있음.

# list에 저장된 시험점수 10개의 평균을 계산, 출력
avg = total / len(scores)
print(f'평균 : {avg}')
# or
print('평균2 :', np.mean(scores))
print(f'평균2 : {np.mean(scores)}')

# list 에 저장된 시험점수 10개의 최대값/최소값 출력
print('최대값 : ', max(scores))
print('최소값 : ', min(scores))
# or
max_score = scores[0]  # scores 의 첫번째 값을 max 로 두겠다.
min_score = scores[0]
for score in scores:
    if score > max_score:  # list 에서 현재 최대값보다 더 큰 수를 찾은 경우
        max_score = score
    if score < min_score:  # list 에서 현재 최소값보다 더 작은 수를 찾은 경우 # elif 하면 안됨! 계속 if 문에서 반복, 모든 값 각각 if 문에서 반복.
        min_score = score
print('최대값 : ', max_score, '최소값 : ', min_score)
# cf. sorted() 정렬함수
sorted_scores = sorted(scores)
print('정렬됨 : ', sorted_scores)
print('원본 배열 : ', scores) # 원본 배열은 변경하지 않는다.

# list 에 저장된 시험 점수의 표준편차 계산, 출력
std = []
for i in scores:
    for j in range(10):
        j = (i - np.mean(scores))**2
        std.append(j)
print('표준편차 : ', sqrt(sum(std) / len(std)))
# or
sum_of_scores = 0
for score in scores:  # scores 에서 score 점수를 꺼낸다.
    sum_of_scores += (score - avg)**2  # 오른쪽을 왼쪽에 더해서 저장함.
standard_deviation = sqrt(sum_of_scores / len(scores))
print(f'표준편차 : {standard_deviation}')
print('표준편차2 :', np.std(scores))