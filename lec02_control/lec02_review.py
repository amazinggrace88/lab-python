'''
<<<<<<< HEAD
lec02.review
'''

# ex01
# iterable : 반복 가능한 변수 ex_list / tuple / set / dict / str 문자열,, slicing 가능한 데이터 타입들
# # 1)
# for i in range(10):
#     print(i, end= ' ')
# # print()
# # 2)
# for i in range(1, 10):
#     print(i, end=' ')
# print()
# # 3)
# for i in range(1, 5, 2):
#     print(i, end=' ')
# print()
# # 4)
# for i in 'ariana grande':
#     print(i, end=' ')
# print()
# # 5)
# data_list = ['a', 'r', 'i', 'a','n','a', 'g','r','a','n','d','e']
# for i in range(len(data_list)):
#     print(i, data_list[i])
# print()
# # 6)
# # dict is iterable for 'for 문'
# alpha = {1:'a', 2:'b', 3:'c'}
# print(alpha.keys())
# print(alpha.values())
#
# for k, v in alpha.items():
#     print(k, v)
#
# for item in alpha.items():
#     print(item)
#

# ex02
# import numpy as np
# from math import sqrt
#
# # 0 ~ 100까지의 범위를 가지는 난수 생성하고 for 문으로 scores[]에 input
# scores = []
# for i in range(10):
#     scores.append(np.random.randint(0, 101))
# print(scores)
#
# total = 0
# for score in scores:
#     total += score
# print(f'총점 : {total}')
# print(f'총점 2 : {sum(scores)}')
#
# # ex03
# for i in range(10):
#     for j in range(10):
#         print(f'{i} * {j} = {i * j}')
#     print('================')
#
# # ex04
# # if in for
# for i in range(1, 10):
#     if i == 5:
#         continue  # for loop 시작점으로 올라감.(if문 안에 있는 밑의 구문들을 건너뛰고 다시 시작점으로 올라가서 계속 한다 - print 하지 않음)
#     print(i, end=' ')
# print()
#
# # 소수(prime number) : 1과 자기자신으로만 나누어지는 정수
# for i in range(1, 11):
#     prime_number = True
#     for d in range(2, i):
#         if i % d == 0:
#             prime_number = False
#             break
#     if prime_number:
#         print(f'{i} is prime number')
#
# # for/while 반복문과 else 가 함께 사용되는 경우 : python의 특수 기능
# # 반복문이 break 를 만나지 않고, 범위 전체를 반복했을 때 else 가 실행됨
# # 반복문 중간에 break 를 만나면 else 는 실행되지 않음.
# # continue 를 만날 때는 else 를 실행한다.
# for i in range(1, 10):
#     if i == 2:
#         continue
#     print(i, end=' ')
# else:
#     print('모든 반복을 끝냄')

# ex05
# import random
#
# import numpy as np
#
# # 쓸모 : 일정하게 list 초기화 or 배열을 만들 때
# n = []
# for i in range(1, 6):
#     n.append(i)
# print(n)
#
# # list comprehension
# n1 = [i for i in range(1, 6)]
# print(n1)
#
# even = [2*i for i in range(1, 6)]
# print(even)
#
# squares = [n**2 for n in range(1, 11)]
# print(squares)
#
# random.seed(1126)
# # 시드
# # 경우에 따라서(보통 디버깅 등을 위해) 동일한 순서로 난수를 발생시켜야 할 경우가 있다.
# # 난수 발생을 위해서는 적절한 시드(seed)를 난수발생기에 주어야 한다.
# # 만약 시드가 같다면 동일한 난수를 발생시키게 된다.
# # random.seed(a=None)을 통해 시드를 설정할 수 있다.
# rand = [np.random.randint(0, 101) for _ in range(10)]
# print(rand)
#
# rand = [np.random.randint(1, 101) for _ in range(10)]
# print(rand)
#
# ex05
# 짝수 배열
# import random
# import numpy as np
#
# even3 = [n for n in range(1, 11) if n % 2 == 0]
# print(even3)
# # 홀수 배열
# odd = [i for i in range(1, 11) if i % 2 == 1]
# print(odd)
# # 주사위 2개 던졌을 때 경우의 수
# for i in range(1, 7):
#     for j in range(1, 7):
#         print(f'({i}, {j})')
# print()
#
# dice1 = []
# for x in range(1, 7):
#     for y in range(1, 7):
#         dice1.append((x, y))  # (x, y)로 묶는 것 만으로도 tuple을 만들 수 있다. why? tuple 을 변수 = ()로 받아들이기 때문에,
# print(dice1, end=' ')
# print()
#
# dice2 = [(x, y) for x in range(1, 7) for y in range(1, 7)]
# print(dice2, end=' ')
# print()
# # 주사위 (x, x)이면 멈추는 경우의 수 ex) (2, 2)이면 (3, 1)로 넘어감
# # (x, y) if x >= y
# for i in range(1, 7):
#     for j in range(1, 7):
#         print(i, j)
#         if i == j:
#             print('주사위가 똑같습니다!')
#             break
#
# dice3 = []
# for x in range(1, 7):
#     for y in range(1, 7):
#         if x >= y:
#             dice3.append((x, y))
#         # else:
#         #     continue 넣지 않아도 된다.
# print(dice3)
#
# dice4 = [(x, y) for x in range(1, 7)
#             for y in range(1, 7)
#                 if x >= y]
# print(dice4)
#
# dice5 = []
# for x in range(1, 7):
#     for y in range(1, x+1):  # x+1까지만 범위를 잡았다.
#         dice5.append((x, y))
# print(dice5)
#
# # 실습 : 시험점수(0~100) 10개를 가지고 있는 list
# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# # 평균보다 높은 점수들의 리스트
# above_mean = [i for i in a
#                 if i > np.mean(a)]
# print(above_mean)
#
# a_mean = []
# for i in a:
#     if i > np.mean(a):
#         a_mean.append(i)
# print(a_mean)
#

# if01
# n = int(input('input your better day counts'))
# if n > 0 :
#     print(f'your better day count is = {n}')
# print('프로그램 종료')
#

# if02
# 1) 숫자 타입인 경우              0 False,                                    0 이외의 숫자는 True 취급
# 2) 숫자 이외의 타입인 경우,       비어있는 값('', "", [], {}, (),..)은 False,    그 이외의 다른 값들은 True 취급
# if in / if not in

#
=======
lec02 - review
for 변수 in iterable:
    iterable statements
'''
import numpy as np
from math import sqrt


# for01
for i in range(20):
    print(i, end=' ')
print()  # 줄바꿈

# list is iterable for 'for 문' (set/tuple 사용도 동일함)
data_list = ['a', 'r', 'i', 'a', 'n', 'a']
for i in data_list:
    print(i)
print()

for i in range(len(data_list)):
    print(i, data_list[i])  # data_list[i]를 주는 것을 잊지 말것!
print()

# dictionary for statements
data_dict = {1:'a', 2:'r', 3:'i'}
print(data_dict.keys())  # key 의 list 가 나온다.
print(data_dict.values())  # value 의 list 가 나온다.
for key in data_dict.keys():
    print('data_dict\'s key  = ', key)
print()
for value in data_dict.values():
    print('data_dict\'s value = ', value)
print()
for item in data_dict.items():
    print('data_dict\'s key & value together = ', item)
print()
# 최종 = dict decomposition
for key, value in data_dict.items():
    print('data_dict\'s key, value separately = ', key, value)
print()



# for02
'''
assignment
'''
#난수 선언(0<=x<=100)
for i in range(10):
    x = np.random.randint(0, 101) #100까지 나와야 하므로
    scores.append(x)
print(scores)
# i 는 for 문에서 사용되지 않지만 문법 때문에 필요하다. (비워둘 수는 없으니 _를 쓰는 것을 허용함)
# x를 합쳐주자.
for _ in range(10):
    scores.append(np.random.randit(0, 101))
print(scores)
>>>>>>> f7c0a88c89558090ee97eec3875f3c100c77ba46
