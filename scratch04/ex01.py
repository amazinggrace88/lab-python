'''
데이터 과학 4장 - 선형대수(Libear Algebra)

< vector space 를 다루는 학문 >
 선형대수는 점들의 연산을 다룬다.
 vector : 2차원 공간에 있는 점(x, y) - x, y 는 각각 성분
 ~차원   : 점 하나를 표시하기 위한 차원 갯수 -> 일반화 n 차원  : (x_1, x_2 .. x_n) 차원의 갯수를 나타낸다.

# 곱의 종류 in 선형대수
# dot product (내적)
# vector product (외적)
'''

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
    return [v_i + w_i for v_i, w_i in zip(v, w)] # v_i : v의 i번째


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
'''
    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result
    
# vector의 수가 다른 경우 v[i] 순서까지만 출력됨
'''

def vector_sum(vectors): #vectors : 관습적으로 vectors 여러개
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

    #
    # result = [0 for _ in range(num_of_elements)] # 0부터 더해나가야 하기 때문에 list에 0을 준다.
    # for i in range(num_of_elements):
    #     for vector in vectors:
    #         result[i] += vector[i]
    # return result
    result = vectors[0] #[] 첫번째 리스트 전체
    for vector in vectors[1:]:
        result = add(result, vector) #result += 와 같은 격..
    return result


if __name__ == '__main__':
    result1 = add(math, science)
    result2 = subtract(math, science)
    print(result1)
    print(result2)
    # 벡터가 다를 때 에러가 나는지도 테스트해봐야 함
    v = [1, 2]
    w = [1, 2, 3]
    # result3 = add(v, w)
    # print(result3) # 우리가 원하는 결과가 아님! why? zip이라는 공통된 벡터까지만 뽑아내고 멈춰 에러를 발생시키지 않는다.
    # result4 = subtract(v, w)
    # print(result4) # solution : 에러 생성
    z = [[1,2], [3,4], [5,6]]
    result5 = vector_sum(z)
    print(result5)

