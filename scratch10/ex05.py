'''
 DataFrame.apply(function, axis)
    axis = 0 (기본값) : DataFrame 의 각 컬럼을 함수의 파라미터에 전달함.
    axis = 1 : DataFrame 의 각 행을 함수의 파라미터에 전달함.
    함수의 리턴 값을 돌려받음
    df의 행(axis=1)을 함수의 매개변수로 주거나, df의 열(axis=0)을 함수의 매개변수로 주는 것
'''

import numpy as np
import pandas as pd


# 숫자 1개를 기준으로 한 함수
def squares(x):
    return x ** 2


def doubles(x):
    return x * 2


if __name__ == '__main__':
    result1, result2 = squares(3), doubles(3)
    print(result1, result2)

    # np.array 를 기준으로 만들어진 것이 pd.Series
    # np.array 에는 **, * 연산자가 없다!  --> 다른 의미.
    array = np.array([1, 2, 3])
    result1, result2 = squares(array), doubles(array)
    print(result1, result2)

    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6],
    })

    print(df)
    print(squares(df))  # squares() 함수 적용이 잘 됨. why? df.series 가 np.array 를 기준으로 만들어진 것이기 때문에
    # [[]] list 의 list 로 만든 df는 squares() 함수 적용 안 됨
    df2 = [[1, 4], [2, 5], [3, 6]]
    # squares(df2) error

    # DataFrame.apply(function, axis)
    # axis = 0 (기본값) : DataFrame 의 각 컬럼을 함수의 파라미터에 전달함.
    # axis = 1 : DataFrame 의 각 행을 함수의 파라미터에 전달함.
    # 함수의 리턴 값을 돌려받음
    # df의 행(axis=1)을 함수의 매개변수로 주거나, df의 열(axis=0)을 함수의 매개변수로 주는 것
    result = df.apply(squares, axis=0)  # df에 파라미터로 squares 함수를 넣어주세요~
    print(result)
    print(np.sum([1, 2, 3]))
    result = df.apply(np.sum, axis=0)  # 각각의 column 을 np.sum(column -> 매개변수)로 준다.
    print(result)
    # a     6
    # b    15
    # dtype: int64
    result = df.apply(np.sum, axis=1)  # 각각의 row 를 np.sum(row -> 매개변수)로 준다.
    print(result)
    # 0    5
    # 1    7
    # 2    9
    # dtype: int64

    '''
     #  중요!
     agg(aggregate) 함수는 집계 함수들만 사용 가능 & 문자열은 집계함수의 파라미터로 넘겨주면 error
     apply 는 집계 함수 이외의 함수들도 사용 가능 & 문자열 또한 파라미터로 넘겨주게 됨
     1. apply 는 groupby 와 상관이 없다.
     2. groupby 에서 apply 는 사용될 수 있다.
     3. apply 가 더 큰 개념! 
    '''
    # agg(aggregate) 함수는 집계 함수들만 사용 가능
    # apply 는 집계 함수 이외의 함수들도 사용 가능

    emp = pd.read_csv('emp_df.csv')
    print(emp.agg(np.mean))  # 집계 함수는 숫자 타입의 컬럼만 자동으로 선택
    # emp.apply(np.mean)
    # apply 함수는 모든 컬럼 또는 행을 함수의 파라미터에 전달하기 때문에,
    # 집계 함수(mean, sum, ...)가 제대로 동작하지 않을 수도 있음.



