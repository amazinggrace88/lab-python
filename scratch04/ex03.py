'''
2차원 리스트를 이용한 행렬
'''
# 모듈을 만들어 import하기 위해 함수 부분과 테스트 부분을 나눈다.
# module function


def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple형태로 리턴

    :param matrix: 행렬(행의 갯수가 n개 이고, 열의 갯수가 m개인 2차원 리스트)
    :return: tuple (n, m)
    """
    # matrix[0]~matrix[n]까지 원소가 서로 같은지 비교해서 아니면 raise error 문 만들기!
    num_rows = len(matrix)  # list 의 갯수 ex_ len(A) = A의 원소의 갯수[],[] 2개
    num_cols = len(matrix[0])  #if matrix else 0 ? 첫번째 원소[]안의 length
    return num_rows, num_cols  # 파이썬만 가능 변수 2개 한꺼번에 쓰기


def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴

    :param matrix: n*m 행렬
    :param index: 선택하고 싶은 행 번호(0 부터 시작)
    :return: 벡터(원소가 m개인 1차원 리스트)
    """
    return matrix[index]


def get_column(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 column을 리턴

    :param matrix: n*m 행렬
    :param index: 선택하고 싶은 열 번호(0 부터 시작)
    :return: 벡터(원소가 n개인 1차원 리스트)
    """
    # result = []
    # for x in matrix:
    #     result.append(x[index])
    # return result

    return [x[index] for x in matrix]


def make_matrix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows * ncols 행렬을 만들어주어 list 들의 list 형태로 리턴
    pseudo-code 프로그램의 뼈대를 보여주기 위한 코드 - 의사(유사)코드
    
    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수 (함수안에 함수를 넘길 수 있기에 쓸 수 있다)(f(nrows, ncols)= 숫자(스칼라))
    :return: nrows * ncols 행렬
    """
# basic
    # m= [] # 빈 리스트 생성 for matrix
    # for i in range(nrows):  # 행의 갯수만큼 반복
    #     row = []  # 빈 리스트 생성 -> matrix에 추가될 행(1차원 리스트)
    #     for j in range(ncols):  # 열의 갯수만큼 반복
    #         row.append(fn(i, j))  #(parameter i, j) 파라미터~
    #     m.append(row)
    #
    # return m
# or
    return [[fn(i, j) for j in range(ncols)] for i in range(nrows)]
    # [[값 for j in range(열개수)] for i in range(행개수)] 리스트의 리스트


def add(x, y):
    return x + y


def identity(x, y):
# 방법1
    # result = 0
    # if x == y:
    #     result = 1
    # else:
    #     result = 0
    # return result
# 방법2 : 3항 연산자 - else 0 why? 항이 세개라서.. -> result에  1 0 둘중 한 값이 들어감.(변수 result 1 0)
    # result = 1 if x == y else 0
    # return result
# c, java 에서는 -> 변수 = if 조건 ? 값 : 값
# 방법3
    return 1 if x ==y else 0


def transpose(matrix):
    """
    주어진 matrix에 대해 행이 열로, 열이 행으로 전치된 행렬을 리턴

    :param matrix: n*m 행렬
    :return: m*n 행렬
    """
# 방법1
    # m = []
    # num_rows = len(matrix)
    # num_cols = len(matrix[0])
    # for i in range(num_cols): # row 만들기 : column을 row로
    #     r = []
    #     for j in range(num_rows): #column 만들기 : row를 column으로
    #         r.append(matrix[j][i])
    #     m.append(r)
    # return m
# 방법2
#   return [[matrix[j][i] for j in range(len(matrix))]  for i in range(len(matrix[0]))]
# 방법3
    nrows, ncols = shape(matrix)
    t = make_matrix(ncols, nrows, lambda x, y: matrix[y][x])
    return t


# 방법4
def transpose(matrix):
    """
    2번째 함수 -> 전의 transpose 함수는 죽는다.

    :param matrix:
    :return:
    """
    # nrows = len(matrix)
    # ncols = len(matrix[0])
    # t = [] # 전치 행렬
    # for j in range(ncols):  # 원본 행렬의 열 개수만큼 반복
    #     # 원본 행렬의 열(column)을 전치행렬의 행으로 추가
    #     t.append(get_column(matrix, j))
    # return t
# 방법5
    return [get_column(matrix, j)for j in range(len(matrix[0]))]


# 방법6
def transpose(matrix):
    # print('unpacking 연산자 *을 사용한 transpose')
    # t = []
    # for col in zip(*matrix): # col이 튜플이다. *A = [<1>, 2, 3] [<4>, 5, 6]
    #     t.append(list(col))
    # return t  # list 안에 튜플이 들어감. list()로 바꿀 수 있다.
# or
    return [list(col) for x in zip(*matrix)]

# module test
if __name__ == '__main__':
    # 2*3 행렬
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3*2 행렬
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    # 첫번째 행은 행 0/첫번째 열은 열 0으로 표기(python에서만)
    print(A) # list로 출력되었기 때문에, 많은 행열을 포함하면
    print(B)
    result1 = shape(A)
    print('shape of A = ', result1)
    result2 = shape(B)
    print('shape of B = ', result2)
    result3 = get_row(A, 0)
    print('index row A = ',result3)
    result4 = get_row(B, 0)
    print('index row B = ', result4)
    result5 = get_column(A, 0)
    print('index column A = ', result5)
    result6 = get_column(B, 0)
    print('index column B = ', result6)
    result7 = make_matrix(2, 2, lambda x, y : x * y) # 함수를 lambda 식으로 표현해주었다.
    print('matrix = ', result7)
    result8 = make_matrix(3, 2, add)
    print('matrix2 = ', result8)  # ()주면 안됨! make_matrix 안에서 실행되어야 한다. add() = 값 / add = 소스
    result9 = make_matrix(2, 2, lambda x, y: 1 if x ==y else 0) #identity 함수를 람다 식으로 구현
    print('identity matrix = ', result9)
    result10 = transpose(A)
    print('transpose A matrix = ', result10)
    result11 = transpose(B)
    print('transpose B matrix = ', result11)

    # zip의 용도 for transpose
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for x, y, z in zip(a, b, c):
        print(x, y, z)

    # 연산자 설명
    # 2항 연산자 : 피연산자가 2개, 즉 값이 2개 들어가야 함
    # cf. ~항 : 피연산자를 의미함


    # unpacking 연산자 : *
    # fn(*args) => tuple처럼 취급하면 된다
    print('A = ', A)
    print('*A = ', *A)
    print('B = ', B)
    print('*B = ', *B)
    # *A =  [1, 2, 3] [4, 5, 6] : []를 꺼내준다. 리스트를 풀어서 원소를 꺼내준다.
    # zip(*A) => argument 2개 [],[]를 준 것과 같다.