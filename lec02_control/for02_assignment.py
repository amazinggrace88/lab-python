'''
assignment
'''

#scores = 빈 리스트 선언
scores = []
# scores[1] = 99 error
# scores.append() 로만 추가 가능

#난수 선언(0<=x<=100)
import numpy as np
for i in range(10):
    i = np.random.randint(0, 100)
    scores.append(i)
print(scores)

#list에 저장된 시험점수 10개의 평균을 계산, 출력
print(sum(scores) / len(scores))

#list에 저장된 시험점수 10개의 최대값/최소값 출력
print(max(scores))
print(min(scores))

#list 에 저장된 시험 점수의 표준편차 계산, 출력
from math import sqrt
std = []

for i in scores:
    for j in range(10):
        j = (i - np.mean(scores))**2
        std.append(j)

print(sqrt(sum(std) / len(std)))
print(np.std(scores))
