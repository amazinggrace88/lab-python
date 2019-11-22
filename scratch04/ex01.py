'''
데이터 과학 4장 - 선형대수(Libear Algebra)

< vector space 를 다루는 학문 >
 선형대수는 점들의 연산을 다룬다.
 vector : 2차원 공간에 있는 점(x, y) - x, y 는 각각 성분
 ~차원   : 점 하나를 표시하기 위한 차원 갯수 -> 일반화 n 차원  : (x_1, x_2 .. x_n) 차원의 갯수를 나타낸다.
 하나의 데이터타입으로 나타내는 row 들의 모임 -> row 수만큼의 벡터 공간 (table)
 column 별로 계산하는데 선형대수가 필요하다.

# 곱의 종류 in 선형대수
# dot product (내적)
# vector product (외적)
'''
import math as mt

math = [99, 90, 85, 97, 80]
science = [100, 85, 60, 90, 70]
# 리스트간의 합, 곱, 차, -> 5차원 공간의 벡터


# 1. 함수 정의

def add(v, w):
    """
    주어진 두 개의 벡터에서 성분별로 합을 구하여 새로운 n차원 벡터를 만든다.
    (서로 차원이 같아야 정의된다)

    :param v: n차원 벡터(성분이 N개인 벡터)
    :param w: n차원 벡터(성분이 N개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 합니다.')
    return [v_i + w_i for v_i, w_i in zip(v, w)]  # v_i : v의 i번째


def subtract(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 차를 구하여 새로운 n차원 벡터를 만든다.
    (서로 차원이 같아야 정의된다)

    :param v: n차원 벡터(성분이 N개인 벡터)
    :param w: n차원 벡터(성분이 N개인 벡터)
    :return: 각 성분별로 빼기 결과를 갖는 벡터
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 합니다.')
    return [v_i - w_i for v_i, w_i in zip(v, w)]
# or


def subtract(v, w):
    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result


def vector_sum(vectors): # vectors : 관습적으로 vectors 여러개
    """
    모든 벡터들에서 각 성분별 합을 더하기를 수행한다.
    ex) vector_sum([1,2], [3,4], [5,6]) = [9, 12]를 반환한다

    :param vectors: n차원 벡터들의 리스트 (2차원 리스트 [[], []])
    :return: n차원 벡터
    """
    # sum1 = v1[0] + v2[0] + v3[0] 이중반복문
    # sum2 = v1[1] + v2[1] + v3[1]
    num_of_elements = len(vectors[0]) # 서로 같은지 확인하기 위해서 [1, 2]의 원소의 갯수를 센다.
    for vector in vectors[1:]:
        if num_of_elements != len(vector):
            raise ValueError('모든 벡터는 길이가 같아야 함.')

    result = vectors[0]  # [] 첫번째 리스트 전체
    for vector in vectors[1:]:
        result = add(result, vector)  # result += 와 같은 격..
    return result


def vector_sum(vectors):  # vectors : 관습적으로 vectors 여러개
    """
    모든 벡터들에서 각 성분별 합을 더하기를 수행한다.
    ex) vector_sum([1,2], [3,4], [5,6]) = [9, 12]를 반환한다

    :param vectors: n차원 벡터들의 리스트 (2차원 리스트 [[], []])
    :return: n차원 벡터
    """
    num_of_elements = len(vectors[0])  # 서로 같은지 확인하기 위해서 [1, 2]의 원소의 갯수를 센다.
    for vector in vectors[1:]:
        if num_of_elements != len(vector):
            raise ValueError('모든 벡터는 길이가 같아야 함.')

    result = [0 for _ in range(num_of_elements)]  # 0부터 더해나가야 하기 때문에 list에 0을 준다.
    for i in range(num_of_elements):
        for vector in vectors:
            result[i] += vector[i]
    return result


'''
벡터의 곱 두가지
1) 스칼라곱
c*(x1, y1)
: 방향은 바뀌지 않고 그 크기만 변한다.
2) 내적 (dot product)
(x1, y1)dot(x2, y2) = x1*x2 + y1*y2
: projection (사상, 투영) -> 그림자가 생기는 과정
(x1, y1)dot(1, 0) = x1
즉, (x1, y1)에서 x축으로 1만큼의 크기를 가지는 그림자는 x1이다.
(x1, y1)dot(0, 1) = y1
즉, (x1, y1)에서 y축으로 1만큼의 크기를 가지는 그림자는 y1이다.
'''
# 1) scalar product


def scalar_multiply(c, vector):
    """
    c * [x1, x2, x3,..] = [c*x1, c*x2, c*x3,...]

    :param c: 숫자(스칼라)
    :param vector: n차원 벡터 (length가 n인 1차원 리스트)
    :return: n차원 벡터
    """
    return [c * i for i in vector]


def scalar_multiply(c, vector):
    result = []
    for i in vector:
        result.append(c*i)
    return result


def dot(v, w):
    """
    [v1, v2, v3, ...] @(dot) [w1, w2, w3, ...] = v1*w1 + v2*w2 + v3*w3,...

    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자
    """
    # 두 벡터가 같은 크기를 가져야 함
    if len(v) != len(w):
        raise ValueError('두 벡터의 길이는 같아야 함')
    sum = 0
    for v_i, w_i in zip(v, w):
        sum += v_i*w_i
    return sum # for + sum 조합 : sigma 역할 \sum_{i}{x_i}*{y_i}


def vector_mean(vectors):
    """
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터
    각 항목별로 평균을 구한 리스트 1개를 만든다.

    :param vectors: n차원 벡터들의 리스트
    ( 길이가 n인 1차원 리스트를 아이템으로 갖는 이차원 리스트 ) [[x_1,x_2,..x_n], [], [], .. [x_n_n]]
    :return: n차원 벡터(길이가 n인 1차원 리스트)
    """
    # 리스트 안 리스트가 몇개가 있는지
    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))
#   함수 안에서 함수를 쓸 수 있어야 함
#   table 안에서 property = column = 성분 ex_국어점수.. 등등
#   합계/평균은 각 변수별로 계산한다 ex_국어점수의 평균
#   성분별 평균 = step1 성분별 합계 함수 만들기 step2 곱 함수 만들기 step3 두개 곱하여 평균 구하기 (과정 쪼개 생각)


'''
벡터의 크기
: 직선의 길이 (2차원의 경우)
= sqrt(x**2 + y**2) (2차원의 경우)
'''
# step1. sum_of_squares


def sum_of_squares(vector):
    """
    vector = [x1, x2, ... , xn] n차원 벡터일 때
    x1 ** 2 + x2 ** 2 + .. + xn ** 2을 리턴

    :param vector: n차원 벡터
    :return: 숫자
    """
    return dot(vector, vector)


def sum_of_squares(vector):
    s_sum = 0
    for i in vector:
        s_sum += i**2
    return s_sum


def magnitude(vector):
    """
    벡터의 크기를 리턴하는 함수
    math.sqrt(sum_of_squares)

    :param vector:
    :return:
    """
    return mt.sqrt(sum_of_squares(vector))


def squared_distance(v, w):
    """
    v = [v1, v2, .. , vn]
    w = [w1, w2, .. , wn]
    (v1 - w1)**2 + (v2 - w2)**2 + .. + (vn - wn)**2 리턴

    :param v: n차원 벡터 (길이가 n인 1차원 리스트)
    :param w: n차원 벡터 (길이가 n인 1차원 리스트)
    :return: 숫자
    """
    sfd = subtract(v, w)
    return sum_of_squares(sfd)


def distance(v, w):
    """
    두 벡터 v와 w 사이의 거리를 리턴 - sqrt(squared_distance)

    :param v: n차원 벡터 (길이가 n인 1차원 리스트)
    :param w: n차원 벡터 (길이가 n인 1차원 리스트)
    :return: 숫자
    """
    return mt.sqrt(squared_distance(v, w))


if __name__ == '__main__':
    result1 = add(math, science)
    result2 = subtract(math, science)
    print('add = ',result1)
    print('subtract = ', result2)
    # 벡터가 다를 때 에러가 나는지도 테스트해봐야 함
    v = [1, 2]
    w = [1, 2, 3]
    result3 = add(v, w)
    print(result3)  # 우리가 원하는 결과가 아님! why? zip이라는 공통된 벡터까지만 뽑아내고 멈춰 에러를 발생시키지 않는다.
    # result4 = subtract(v, w)
    # print(result4) # solution : 에러 생성
    z = [[1,2], [3,4], [5,6]]
    v = [10, 20]
    w = [15, 25]
    unit_x = [1, 0]  # x축 단위 벡터
    unit_y = [0, 1]  # y축 단위 벡터
    dl = [[1, 2], [3, 4]]
    sum_list = [1, 1]

    result3 = vector_sum(z)
    print('vector_sum = ', result3)

    result4 = scalar_multiply(2, w)
    print('a = ', result4)

    x = dot(v, unit_x)
    y = dot(v, unit_y)

    print('x = ', x)
    print('y = ', y)

    result5 = vector_mean(dl)
    print('vector_mean = ', result5)
    result6 = sum_of_squares(sum_list)
    print('sum_of_squares = ', result6)
    norm = magnitude(sum_list) # vector 크기 : norm ||v vector ||
    print('magnitude = ', norm)

    result7 = squared_distance(v, w)
    print('squared_distance = ', result7)

    result8 = distance(v, w)
    print('distance = ', result8)