# coding=utf-8
"""
pandas groupby, aggregate, apply 작업 개요
<groupby>
"""

import pandas as pd
import numpy as np

# DataFrame 생성 (pd.DataFrame()에 들어갈 수 있는 datatype: 1.dict(key 가 컬럼이름) 2.list)
df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randint(0, 10, 5),  # 0~ 10까지, 5개 랜덤으로 추출
    'data2': np.random.randint(0, 10, 5)
})
print(df)

# 1.
# <분리> by='key1': 'key1'기준으로 group 을 나눈다.
grouped1 = df.groupby(by='key1')
print(grouped1)  # DataFrameGroupBy 객체: df를 쪼개놓은 임시 df로 그룹 연산 함수(평균, 분산, 최소, 최대 ..등)를 주어서 print 를 할 수 있다.

# <적용> 그룹함수 연산 : count, sum, mean, median, var, std, min, max
# 1) groupby
cnt = grouped1['data1'].count()
print(type(cnt))  # Series 라는 class
print(cnt)  # a, b는 label, 3, 2는 data
print(cnt['a'], cnt['b'])  # data 출력
print(grouped1['data1'].mean())
# key1
# a    2.666667
# b    3.000000
print(grouped1.mean())  # mean 함수가 column 별로 적용 된다. - ***숫자열인 컬럼만 알아서 계산해줌. 문자열 계산 안함.(key2 출력 안했어요!)***
#          data1  data2
# key1
# a     2.666667    6.0
# b     3.000000    5.0
print(grouped1[['data1', 'data2']].mean())  # 같은 결과 출력

grouped2 = df.groupby('key2')
print(grouped2.mean())

# 1) -2 groupby 의 기준(by)이 2 개 이상의 컬럼일 때 : 리스트를 전달하면 된다~
grouped3 = df.groupby(['key1', 'key2'])  # by 자리(첫번째)에 놔주어야 한다~
print(grouped3)  # DataFrameGroupBy객체라고만 나온다.
print(grouped3['data1'].count())  # 그룹끼리 그룹 연산을 수행한다.
# key1  key2  --> 4 개 그룹이 나왔다.
# a     one     2  --> a 인 것 중 one 은 2개
#       two     1
# b     one     1
#       two     1
# Name: data1, dtype: int64
print(grouped3['data2'].count())  # 결과 같다. ( = print(grouped3['data1'].count())
print(grouped3.count())
#            data1  data2
# key1 key2
# a    one       2      2
#      two       1      1
# b    one       1      1
#      two       1      1
print(grouped3.mean())
#            data1  data2
# key1 key2
# a    one       4      2
#      two       5      1
# b    one       7      4
#      two       5      8

# 1) -3
people = pd.DataFrame(np.random.randint(0, 10, (5, 5)),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jimmy', 'Travis'])

# np.random.randint(0, 10, (5, 5)) 0~10까지 (5,5) size 로 랜덤 숫자 만듬
# np.random.randn(5,5) : 5행5열만큼 랜덤 숫자 만듬
# columns = 컬럼 이름
# index = label (loc 방식)
# index 는 숫자로도 존재해요 (iloc 방식)
print(people)
print(people.groupby(len).sum())  # len 으로 그룹을 만들겠다! (3, 5, 6)
print(people.groupby(lambda x: x.startswith('J')).sum())  # x.startswith('J') J로 시작하면 true, 그렇지 않으면 false





