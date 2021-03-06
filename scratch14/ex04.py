import numpy as np

# numpy.c_ (column bind)와 numpy.r_ (row bind) 의 비교
a = np.array([1, 2, 3])
print('a is \n', a, type(a), a.shape)  # (3,) -> 1차원 array~ 원소의 갯수 3, 행개수가 아니다!
b = np.array([4, 5, 6])
print('b is \n', b, type(b), b.shape)

c = np.c_[a, b]
print('c is \n', c, type(c), c.shape)
# [[1 4]
#  [2 5]
#  [3 6]] <class 'numpy.ndarray'> (3, 2)
#  -> 첫번째 원소가 첫번째 컬럼, 두번째 원소가 두번째 컬럼 -> 컬럼별로 묶기 때문에 a, b의 원소의 갯수가 같아야 한다.
# R 에서는 cbind()

d = np.r_[a, b]
print('d is \n', d, type(d), d.shape)
# [1 2 3 4 5 6] <class 'numpy.ndarray'> (6,)
# 행을 붙이는 기능이기 때문에 a, b의 원소의 갯수 같지 않아도 된다.
# R 에서는 rbind()

e = np.array([[1, 2, 3],
              [4, 5, 6]])

f = np.array([[10, 20],
              [30, 40]])

# row 갯수는 맞으므로 옆으로 붙이는 c_ 가능 (column 방향으로 붙일 수 있음)
# 컬럼갯수가 안맞으므로 밑으로 붙이는 r_ 불가능. (row 방향으로 붙일 수 없음 - e 는 컬럼 3개, f 는 컬럼 2개)
print('e & f column bind : \n', np.c_[e, f])
# print(np.r_[e, f])

g = np.array([100, 200, 300])
# print(np.c_[e, g])
# print(np.r_[e, g])  # 1차원이라서 안된다~! 2차원 array 는 2차원 array 끼리 붙여주어야 함!
g = np.array([[100, 200, 300]])
print('e & g column bind : \n', np.r_[e, g])  # 같은 차원끼리 합쳐야 해용


# numpy 의 여러가지 array 만드는 함수 정리 ************************************* 중요~

# (2, 3) shape의 모든 원소가 1인 array를 생성해서 출력: A
A = np.ones((2, 3), dtype=np.int)  # 원래는 실수가 기본타입!
print('A : ', A)

# (2, 3) shape의 모든 원소가 0인 array를 생성해서 출력: B
B = np.zeros((2, 3), dtype=np.int)
print('B :', B)

# (3, 2) shape의 원소는 1 ~ 6인 array를 생성해서 출력: C
C = np.arange(1, 7).reshape((3, 2))
print('C :', C)

# (3, 2) shape의 난수들로 이루어진 array를 생성해서 출력: D
D = np.random.random((3, 2)).reshape((3, 2))
print('D : ', D)


"""다음과 같은 결과가 나올 수 있도록 
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현 # for 문 사용
|1 2| + |5 6|= |6  8 | 
|3 4|   |7 8|  |10 12|

|1 2| - |5 6|= |-4 -4| 
|3 4|   |7 8|  |-4 -4|

|1 2| * |5 6|= |5  12| 
|3 4|   |7 8|  |21 32|

|1 2| / |5 6|= |0.2   0.333| 
|3 4|   |7 8|  |0.428 0.5  |

|1 2| @ |5 6|= |19 22| 
|3 4|   |7 8|  |43 50|
@ : dot
위의 결과와 같은 결과를 주는 numpy 코드를 작성
"""


def add(x, y):
    """
    np.array 행렬끼리 더하기
    x : np.array
    y : np.array
    """
    row = x.shape[0]
    col = x.shape[1]
    combined_matrix = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            combined_matrix[i, j] = x[i, j] + y[i, j]
    return combined_matrix


def subtract(x, y):
    """
    np.array 행렬끼리 빼기
    x : np.array
    y : np.array
    """
    row = x.shape[0]
    col = x.shape[1]
    subtract_matrix = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            subtract_matrix[i, j] = x[i, j] - y[i, j]
    return subtract_matrix


def multiply(x, y):
    """

    """
    row = x.shape[0]
    col = x.shape[1]
    multiply_matrix = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            multiply_matrix[i, j] = x[i, j] * y[i, j]
    return multiply_matrix


def divide(x, y):
    """

    """
    row = x.shape[0]
    col = x.shape[1]
    divided_matrix = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            divided_matrix[i, j] = x[i, j] / y[i, j]
    return divided_matrix

# 나의 정답 (Amazing!)
def dot(x, y):
    """
    두행렬 A와 B의 dot 연산 결과를 리턴
    dot_ij = sum(e)[x_ie * y_ej]
    """
    x_row = x.shape[0]  # dot 의 결과행렬 row 갯수
    x_col = x.shape[1]  # 각 원소들끼리 곱한 결과를 더하는 횟수
    y_row = y.shape[0]  # if 문에서 shape 이 같은지 확인하기 위함
    y_col = y.shape[1]  # dot 의 결과행렬 col 갯수
    if x_col != y_row:
        raise ValueError('X의 column 과 Y의 row 갯수는 같아야 합니다!')
    else:
        dot_matrix = np.zeros((x_row, y_col), dtype=int)
        for x_i in range(x_row):
            for y_j in range(y_col):
                dot_matrix_element = 0  # 여기서 reset 해주어야 해요!~ element 1 개 reset
                for element in range(x_col):
                    dot_matrix_element += x[x_i, element]*y[element, y_j]
                    print(f'dot_matrix_element += {x[x_i, element]}*{y[element, y_j]}')
                dot_matrix[x_i, y_j] = dot_matrix_element
        return dot_matrix


# 오쌤 정답
def my_dot(A, B):
    """두 행렬 A와 B의 dot 연산 결과를 리턴
        dot_ik = sum(j)[a_ij * b_jk]
    """
    print('A shape:', A.shape)
    print('B shape:', B.shape)
    if A.shape[1] != B.shape[0]:
        raise ValueError('A의 column과 B의 row 개수는 같아야 함!')
    n_row = A.shape[0]  # dot 결과 행렬의 row 개수
    n_col = B.shape[1]  # dot 결과 행렬의 column 개수
    temp = A.shape[1]  # 각 원소들끼리 곱한 결과를 더하는 회수
    numbers = []  # 결과값들을 저장할 리스트
    for i in range(n_row):
        for k in range(n_col):
            n = 0
            for j in range(temp):
                n += A[i, j] * B[j, k]
            numbers.append(n)
    return np.array(numbers).reshape(n_row, n_col)  # append 후 다시 shape 만들어주었다.


# 오쌤 정답 2
def dot_1d(X, Y):
    if len(X) != len(Y):
        raise ValueError('len(X) != len(Y)')
    result = 0
    for i in range(len(X)):
        result += X[i] * Y[i]
    return result


def dot_2d(X, Y):
    n_row = X.shape[0]
    n_col = Y.shape[1]
    if X.shape[1] != Y.shape[0]:
        raise ValueError('X.shape[1] != Y.shape[0]')
    result = np.zeros((n_row, n_col))
    for i, row in enumerate(X):
        for j, col in enumerate(zip(*Y)):
            print(f'i={i}, row={row}, j={j}, col={col}')
            result[i, j] = dot_1d(row, col)
    return result


# test
e = np.array([[1, 2],
              [4, 5]])

e1 = np.array([[2, 4],
               [8, 10]])

print('add test :\n', add(e, e1))
print('subtract test :\n', subtract(e1, e))
print('mutiply test :\n', multiply(e1, e))
print('divide test :\n', divide(e1, e))
print('dot test :\n', dot(e, e1))
print('dot test :\n', e.dot(e1))
print('dot test :\n', e @ e1)  # numpy 의 array 에서만 사용할 수 있는 기호 @
# numpy 에서는 e.dot(e1) 의 .을 못써서..

"""
선형대수 용어 정리 -- numpy 함수를 활용하여 만들어보기!
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족 (숫자 1의 역할, A 의 순서를 바꿔도 됨!)
역행렬(Inverse matrix): A @ A^{-1} = A^{-1} @ A = I를 만족하는 행렬 (역수의 역할)
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬
"""



