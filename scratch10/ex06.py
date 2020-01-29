"""
agg 함수 정리
"""

import numpy as np
import pandas as pd


def squared_mean(data):
    """데이터의 제곱의 평균"""
    squared_sum = 0
    for x in data:
        squared_sum += x ** 2
    return squared_sum / len(data)


def my_func(x):
    """값이 4개인 튜플을 리턴"""
    return x.min(), x.max(), x.mean(), squared_mean(x)


if __name__ == '__main__':
    df = pd.DataFrame({
        'pop': np.random.randint(1, 10, 4),
        'income': np.random.randint(1, 10, 4),
    }, index=['a', 'b', 'c', 'd'])  # 생성자(파라미터) 2개: 1) {}, 2) index)
    print(df)

    # 1. agg 정리
    # agg(aggregate): Dataframe 의 축(axis)를 기준으로 통계량을 집계하기 위한 함수
    # 통계량(statistics) - sum, mean, var, stddev, min, max, median, .. (len 도 들어가는지 여쭙기)
    # 집계가 목적이므로 데이터가 여러개 있어야 한다. / 데이터 타입이 숫자 타입인 행/열에만 함수를 적용시켜 계산한다.
    # agg 함수는 pandas 나 numpy 에서 제공하는 집계함수 이외에도 사용자 정의 함수를 사용할 수 있음.
    # (단, 조건 - 함수는 series 를 파라미터에 전달하면 숫자(스칼라)를 리턴하는 함수여야 한다)  -> 보충이 필요하닷
    print('===agg by column(axis = 0)')
    print(df.agg('mean'))
    # 작동원리 : '함수'를 agg 하는 데이터에 각각 적용하여 축 1개 당 값을 하나 만들어낸다.
    print(df.agg('mean', axis=0))

    # 기본값 axis = 0이 열 기준인 이유: 같은 컬럼에 같은 데이터가 들어가기 때문에
    print('===agg by row(axis = 1)')
    print(df.agg('mean', axis=1))

    # 사용자 정의 함수 적용하기
    print(df.agg(squared_mean))
    # 설명 : pop 이라는 컬럼의 첫번째 행을 squared_mean 이라는 함수의 파라미터로 준다.
    print(df.agg(squared_mean, axis=1))
    # 설명 : a 이라는 행의 첫번째 열을 squared_mean 이라는 함수의 파라미터로 준다.
    print(df.agg(my_func))  # ???? 보충이 필요하닷 - pandas 공식 문서에서 가져옴.

    # 2. apply 정리
    # apply: DataFrame 의 축(axis)을 기준으로 함수를 적용(apply)하기 위한 함수
    # 적용하려는 함수는 pandas 객체(DataFrame, Series, 스칼라) 만 리턴하면 됨
    # ( <-> agg : 적용하려는 함수는 숫자 1개를 리턴하는 함수(스칼라))
    # agg 함수는 숫자 타입의 스칼라만 리턴하는 함수를 적용하는 apply 의 특수한 경우이며, apply 함수가 더 큰 개념!
    # apply 함수를 더 일반적으로 사용하지만, 집계와 같은 특수한 목적인 경우에는 agg 함수보다 성능이 느리다. (check 사항이 많을 것이므로 더 느림)
    print('===apply by column(axis = 0)')
    print(df.apply('mean'))
    print('===apply by row(axis = 1)')
    print(df.apply('mean', axis=1))



