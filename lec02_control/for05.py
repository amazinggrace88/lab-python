'''
list comprehension ***
python 에만 있는 문법
코드를 간단하게 구현 가능
ex_ filtering 해서 새로운 list 를 만들고 싶을 때 (ex_시험점수 80점 이상을 sorting)
    데이터 전처리에 사용
'''
import numpy as np

# before
numbers = [1, 2, 3, 4, 5]
print(numbers)

# 쓸모 : 일정하게 list 초기화 or 배열을 만들 때
numbers2 = []
for i in range(1, 6):
    numbers2.append(i)
print(numbers2)

# n을 list 에 넣겠다. 범위는 1~5까지 #매우 많이 사용
numbers3 = [n for n in range(1, 6)]
print(numbers3)

# 2, 4, 6, 8, 10
even = [2 * n for n in range(1, 6)]
print(even)

# 1, 4, 9, 16, 25
squares = [n**2 for n in range(1, 6)]
print(squares)

# random number 로 10개 만들기
randoms = [np.random.randint(0, 101) for x in range(10)]  # x가 필요없는 변수이라도 for문을 맞춰야 하기 때문에 써주는 것
print(randoms)
# or
randoms = [np.random.randint(0, 101) for _ in range(10)]  #_: for문을 맞춰야 하기 때문에 써주는 것
print(randoms)


# 짝수 배열
even2 = []
for n in range(1, 11):
    if n % 2 == 0:
        even2.append(n)
print(even2)
# or
even3 = [n for n in range(1, 11) if n % 2 == 0]
print(even3)


# 주사위 2개 던졌을 때 경우의 수
for n in range(1, 7):
    for i in range(1, 7):
        print(f'({n}, {i})')
# or
dice1 = []
for x in range(1, 7):
    for y in range(1, 7):
        dice1.append((x, y))  # tuple 생성하여 tuple append
print(dice1)
# or (list comprehension)
dice2 = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(dice2)


# 주사위 (x, x)이면 멈추는 경우의 수 ex) (2, 2)이면 (3, 1)로 넘어감
# (x, y) if x >= y
# 나의 정답
for i in range(1, 7):
    for j in range(1, 7):
        print(i, j)
        if i == j:
            print('주사위가 똑같습니다!')
            break
# or
dice3 = []
for x in range(1, 7):
    for y in range(1, 7):
        if x >= y:
            dice3.append((x, y))
        # else:
        #     continue 넣지 않아도 된다.
print(dice3)
# or
dice3 = [(x, y) for x in range(1, 7)  # 줄바꿈도 가능
         for y in range(1, 7)
         if x >= y]
print(dice3)
# or
dice3 = []
for x in range(1, 7):
    for y in range(1, x+1):
            dice3.append((x, y))
print(dice3)


# 실습 : 시험점수(0~100) 10개를 가지고 있는 list
scores = [np.random.randint(0, 101) for _ in range(10)]
print(scores)
# 평균보다 높은 점수들의 리스트
above_mean = [s for s in scores
              if s > np.mean(scores)]
print(above_mean)
# or
above_mean = []
mean = np.mean(scores)
for s in scores:
    if s > mean:
        above_mean.append(s)
print(above_mean)