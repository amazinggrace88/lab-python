'''
numpy 패키지를 사용한 벡터 연산
'''
import math
import numpy as np
# 원리는 똑같이 동작하고 성능은 더 좋다.


# 버전 확인
print('numpy version: ', np.__version__)  # __version__
print('numpy version2: ', np.version)  # np.version 버전의 주소를 알려줌

# 기존 - 파이썬 list 데이터 타입의 연산
v = [1, 2]  # list 라고 하는 class
print(type(v))
print('v= ', v)

w = [2, 3]
print(type(w))
print('w= ', w)

print(v + w)  # v 그대로, 새로운 리스트가 만들어짐
# 결과 : [1, 2, 2, 3] -> 리스트를 합쳐서 하나의 리스트로 만든다.(like extend) 덧셈의 기능은 아님!
v.extend(w)
print(v)  # 완전히 같지는 않다. why? v 자체가 바뀐다.

# print(v - w)
# 결과 error : 뺄셈 연산 사용할 수 없음


# numpy 패키지의 ndarray 타입을 사용
v = np.array([1, 2])
print('type: ', type(v))  # type : <class 'numpy.ndarray'>
# ndarray (n-dimensional array n차원 배열: 배열안에 배열이 있으면 2차원, 배열 안에 배열 안에 배열이 있으면 3차원, ..)
print(v)  # list 처럼 생겼지만, class type이 다르다. (= 함수 다름/연산과정 다름)
print('dimension: ', v.ndim)  # 배열의 차원(number of dimension)
print('shape: ', v.shape)  # 1차원 배열인 경우 : 원소의 갯수를 의미함 (원소갯수, 생략)


v = np.array([
    [1, 2],  # 행과 열을 가지고 있음
    [3, 4]
])  # [] 배열
print('type: ', type(v))
print('dimension: ', v.ndim)
print('shape: ', v.shape)  # 배열이 (행2,열2) 모양.


v = np.array([
    1,
    [1, 2],  # 행과 열을 가지고 있음
    [3, 4]
])
print('type: ', type(v))
print('dimension: ', v.ndim)
print('shape: ', v.shape)  # 원소의 갯수 3개 - 배열 취급하지 않는다.
# 큰 배열 안에 원소 3개, 1은 배열이 아니라 dimension을 가지지 않는다.
# 배열 안에 있는 모든 원소가 모두 배열이어야 2차원 이상의 배열이 될 수 있다.

# 배열 list : [] 안에 여러 값이 들어가는 것
l = [
    [1, 2],
    [3, 4]
]
print('list : ', l)
# array    : 배열과 다름
v = np.array([  # np.array()안에
    [1, 2],  # 파이썬의 기본타입인 list를 준다.
    [3, 4]
])
print('ndarray: ', v)  # -> for dataframe 데이터타입 바뀜/함수 바뀜/과정 바뀜
# 배열과 array는 둘 다 차원이 있다.

# ndarray 타입을 이용한 벡터 연산
v = np.array([1, 2, 3])
w = np.array([3, 4, 5])


# 1. 덧셈
vector_add = v + w  # 두 벡터가 모양(shape)이 같을 때에만 연산
print('vector add = ', vector_add)  # column별로 계산하여 array 만듬


# 2. 뺄셈
vector_subtract = v - w
print('vector subtract = ', vector_subtract)


# 3. 2차원 배열의 sum / mean / scalar product
vectors = np.array([
    [1, 2],
    [3, 4]
])
# 모든 원소의 합
np_sum = np.sum(vectors)
print('np sum = ', np_sum) # 모든 원소들의 합을 숫자로 출력 -> for 문을 쓰지 않아도 된다.
# np.array 는 반복하는 기능이 숨어있음

# sum - 축에 의해 분류
np_sum_by_col = np.sum(vectors, axis = 0) # 축 : 0 column 방향 ! 1 row 방향
# sum ctrl+q : `sum(a -> array, axis=None, dtype=None, out=None, keepdims=np._NoValue, initial=np._NoValue, where=np._NoValue)` on docs.scipy.org
print('np_sum_by_col = ', np_sum_by_col) # [1+3 = 4, 2+4 = 6] like vector summation
np_sum_by_row = np.sum(vectors, axis = 1)
print('np_sum_by_row = ', np_sum_by_row) # [1+2 = 3, 3+4 = 7]

# 모든 원소의 mean
np_mean = np.mean(vectors)
print('np_mean = ', np_mean)

# mean - 축에 의해 분류
np_mean_by_col = np.mean(vectors, axis=0)
print('np_mean_by_col = ', np_mean_by_col) # [2. 3.] 2.0 3.0이다.
np_mean_by_row = np.mean(vectors, axis=1)
print('np_mean_by_row = ', np_sum_by_row)

# ndarray를 이용한 스칼라곱
v = [1, 2, 3] # list
scalar_mul = 3 * v # list 를 세번 반복하여라
print('scalar multiplication = ', scalar_mul) #  [1, 2, 3, 1, 2, 3, 1, 2, 3]
v = np.array([1, 2, 3])
scalar_mul = 3 * v # v*3
print('scalar multiplication = ', scalar_mul) # [3 6 9]

# ndarray를 이용한 스칼라나누기 (나머지/몫도 스칼라 단위로 가능)
v = np.array([1, 2, 3])
scalar_div = v / 3
print('scalar division = ', scalar_div)

# 내적
v = np.array([1, 2])
w = np.array([3, 4])
print('dot = ', v.dot(w)) # 11 = 1*3 + 2*4 : (v)dot(w)형식
# 벡터 거리는 내적으로 구할 수 있다.

# numpy 중 내적을 사용한 벡터의 크기
def norm(v):
    return math.sqrt(v.dot(v))

v = np.array([1, 1])
print('norm = ', norm(v)) # magnitude in ex01 : 벡터의 크기

# numpy 중 내적을 사용한 두 벡터간의 거리 : v-w 빼야하므로
def squared_distance(v, w):
    # return math.sqrt((v-w).dot(v-w))
    return norm(v-w)

w = np.array([10, 10])
print('distance = ', squared_distance(v, w)) # 두 벡터 사이의 거리