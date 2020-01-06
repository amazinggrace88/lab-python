# coding=utf-8
"""
for 구문
for 변수 in iterable:
    반복할 문장들

*iterable : 반복 가능한 변수 ex_list / tuple / set / dict / str (문자열).. slicing 가능한 데이터 타입들!
"""

# range(to) : 0부터 (to - 1)까지 범위의 숫자들을 만들어주는 함수
# range(from, to) : from 부터 (to - 1)까지 범위의 숫자들을 만들어주는 함수
# range(from, to, step) : from 부터 (to - 1)까지 step 만큼씩 증가 또는 감소하는 범위를 만들어주는 함수

# 0 ~ 4 까지 출력 range(to)
for i in range(5):  # (0, 1, 2, 3, 4)
    print(i)

# 줄바꿈을 넣지 말고, i 출력 후 뒤에 줄바꿈 대신 '공백'을 i 끝에 출력
for i in range(5):
    print(i, end=' ')
print()  # 줄바꿈만 출력한다는 의미


# 1 ~ 4 까지 출력 range(from, to)
for i in range(1, 5):  # (1, 2, 3, 4)
    print(i, end=' ')
print()


# range(from, to, step)
for i in range(1, 5, 2):  # (1, 3)
    print(i, end=' ')
print()


# str is iterable for 'for 문'
for s in 'hello python!':
    print(s, end=' ')
print()


for s in 'ariana grande':
    print(s, end=' ')
print()


# list is iterable for 'for 문' (set/tuple 사용도 동일함)
lang = ['pl/sql', 'r', 'python', 'java']
for l in lang:
    print(l, end=' ')
print()

# index, list for 문 출력 (using range)
for i in range(4):
    print(i, lang[i])
print()

# list 의 길이를 구하는 함수를 range 로 준다. (중간에 추가/삭제 된 list 도 변경 없이 사용 가능)
for i in range(len(lang)):
    print(i, lang[i])
print()

# dict is iterable for 'for 문'
alpha = {1: 'a', 2: 'b', 3: 'c'}
print(alpha.keys())  # dict 의 key -> 이름
print(alpha.values())

# key 를 찾고 싶을 때 : using .keys()
for key in alpha.keys():
    print(key, alpha[key])

# key 를 찾고 싶을 때 2 : in dict 는 딕셔너리의 key 들만을 반복함
for item in alpha:
    print(item)

# (key, value)의 쌍을 찾고 싶을 때 -> ()tuple 로 출력
for item in alpha.items():
    print(item)

# key, value = (1, 'a') : ***** 변수를 두 가지 선언하여 decomposition 해준다. *****
for key, value in alpha.items():
    print(key, value)

