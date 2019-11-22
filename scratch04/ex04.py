'''
numpy 의 행렬 관련 함수
'''
import numpy as np

# numpy는 np.array가 기본타입 객체
from IPython.core.tests.test_formatters import B
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print(A.shape)


# shape 을 따로 만들 수 있다.
nrows, ncols = B.shape
print(nrows, '*', ncols)



# slicing : 부분집합
# 행렬의 특정 행 / 열을 뽑아내는 방법
# list[i][j] <-> ndarray[i,j]
print('1*2 = ', A[1, 2])
# 2차원 slicing은 ndarray만 된다. (list는 가능)
print('0row 0:2col = ', A[0, 0:2])
print('0:2 * 0:2 = ', A[0:2, 0:2])
print('column', A[:, 0])  # 모든 행을 다 꺼낼 때에는, :로 구분 -> column을 가지고 온다.(인덱스 0번 컬럼의 원소들로 이루어진 array)
print('row', A[0, :])  # row 를 가지고 온다.(인덱스 0번 row의 원소들로 이루어진 array)


# identity_matrix (항등행렬 : 행과 열의 갯수가 같다)
identity_matrix = np.identity(3)
print('identity = ',identity_matrix)  # float
identity_matrix = np.identity(3, dtype=int)
print('identity int = ',identity_matrix)  # int


# Transpose_matrix
print('transpose A = ',A.transpose())


# dot in matrix
# 벡터의 내적을 확장한 개념
# 그냥 행렬의 곱셈..
print('A dot B = ', A.dot(B))
print('B dot A = ', B.dot(A))
