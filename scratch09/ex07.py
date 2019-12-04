"""
pandas 데이터 타입
series 1차원 리스트. 인덱스 한 개만 갖음.
DataFrame: 2차원 리스트, 인덱스가 행과 열 두개를 갖음
"""
import pandas as pd
import numpy as np

a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(a))  # <class 'pandas.core.series.Series'>
# Series 라는 클래스 (데이터와 기능을 한꺼번에 가지고 있는 데이터 타입)
print(a)  # 인덱스 + 데이터출력

# Series 에서 특정 인덱스의 아이템 선택 : Series[index]
print(a[0])
# a[0]의 데이터 타입: float64
# 인덱스 연산자([]) 안에서 번위 연산자를 사용할 수도 있음
print(a[0:3])
# 데이터 타입: series
# 인덱스 연산자 ([]) 안에서 리스트 연산자([])를 사용할 수도 있음
# print(a[0,2,4])
# 이건 안됨, 시리즈는 인덱스 1개가 오는 것
print([[0,2,4]])
# 데이터타입: series

# dict type : {key: value,..}의 데이터에서 DataFrame 생성!
df = pd.DataFrame({
    'no': [3, 13, 23],
    'name': ['김영광', '이은지', '조유경'],
    'gender': ['M', 'F', 'F']
})
print(df)  # dict의 key값이 column의 name이 된다!

# 2차원 리스트([[], [], []]) 타입의 데이터에서 DataFrame을 생성
students = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
], columns=['번호', '이름', '성별'])
# columns 이라는 property 를 사용하여 칼럼의 이름 변경
# .columns: 컬럼의 이름 부여하는 함수
print(students)
# 2차원 리스트 -> df 로 출력됨 컬럼의 이름이 없으면 index가 자동 부여된다.

# Dataframe.iloc[row_index, column_index(생략 가능)]
# 머신러닝에서 데이터 분할 시 사용
print(students.iloc[0, 0])  # index 0행의 0열 : 4
print(students.iloc[0,0:3])
# 0번 행, 0, 1, 2 열에 있는 item
# 번호      4
# 이름    김재성
# 성별      M
# Name: 0, dtype: object
print(type(students.iloc[0,0:3]))  # series: 여러가지 타입을 함께 쓸 수도 있음.(출력형태 기억)
# <class 'pandas.core.series.Series'>
print(students.iloc[0:2, 0:2])  # df: 2차원 형태
print(type(students.iloc[0:2, 0:2]))
# <class 'pandas.core.frame.DataFrame'>
print(students.iloc[:, 1:2])  # ':' : 전체 행/열 - 자리에 따라 다르다. 연산자 제외할 때 사용
print(students.iloc[1:2, :])  # test/train data 나눌 때 사용
print(students.iloc[1:2])  # 모든 컬럼 선택시 컬럼 인덱스 생략 가능.


# boolean indexing
# DataFrame[[boolean들의 리스트]] : 리스트에서 true 인 값의 인덱스를 행 인덱스로 선택하여 부분집합으로 만든다.
print(students[[False, True, False]])  # 행 번호/행의 이름을 list로 준다. - boolean 값으로 준다. 0열 - False, 1열 - True, 2열 - False
condition = (students['성별'] == 'M')  # students에서 성별만 뽑은 series == M
condition =  students['성별'] == 'M'  #  series의 원소와 M을 비교하는 것이다.(series 갯수만큼 true/false 나옴)
print(condition)  # series로 출력
print(students[condition])


# df 합치기
# 1) 옆으로 합치기 : join
# 2) 위아래로 합치기 : concat


# 2) 위아래로 합치기 : concat
# df 컬럼 이름이 일치가 되는 것이 좋다
students.columns = ['no', 'name', 'gender']
stu_df = pd.concat([df, students])  # 안에 []로 넘길 것
print(stu_df)
#    no name gender
# 0   3  김영광      M
# 1  13  이은지      F
# 2  23  조유경      F
# 0   4  김재성      M  # 문제점 : 새로 indexing 하지 않는다. label로 0, 1, 2 가 나왔다.
# 1  14  이재경      M
# 2  24  조지원      F
print(stu_df.iloc[0])  # index
print(stu_df.loc[0])  # label
stu_df2 = pd.concat([df, students], ignore_index=True)  # label을 중복되게 하지 않기 위해서
print(stu_df2)
#    no name gender
# 0   3  김영광      M
# 1  13  이은지      F
# 2  23  조유경      F
# 3   4  김재성      M
# 4  14  이재경      M
# 5  24  조지원      F


# data에서 sorting(정렬)하는 방법: DataFrame.sort_values(정렬 기준 컬럼 이름)
print(stu_df2.sort_values('no'))
print(stu_df2.sort_values('name'))
print(stu_df2.sort_values('gender'))

# 두 개 이상의 조건으로 boolean indexing
cond1 = stu_df2['no'] % 2 == 1  # 조건: no 컬럼의 값이 홀수
print(cond1)  #
cond2 = stu_df2['gender'] == 'F'  # 조건: gender 컬럼의 값이 'F'
print(cond2)
subset = stu_df2[cond1 & cond2]  # & o / and x -> and 안됨! why? series와 series 사이에는 and 정의 안되어 있음. &만 정의
# boolean 인덱싱에서는 and, or 연산자 사용 불가능, 각 성분별로 연산을 하는 (bitwise 연산자) &, |을 사용해야 함
print(subset)
