'''
DataFrame의 NA 처리
1) NA 를 평균값으로 대체
2) groupby 를 하여 그룹별 평균값으로 대체
'''
import numpy as np
import pandas as pd


def fill_group_mean(df):
    group_mean = df['data'].mean()  # DataFrame 객체를 가지고 mean 출력
    print('division\'s group mean is \n', group_mean)  # group이 알파벳 순서대로 출력됨
    return df.fillna(group_mean)  # group_mean : Series


if __name__ == '__main__':
    # Series 객체 생성
    print('Series 객체 생성===========')
    s = pd.Series(np.random.randint(1, 10, 5))
    print(s)
    s[3] = np.nan  # NA로 변경
    print(s)

    # 1) NA 를 평균값으로 대체
    # 평균에 영향을 끼치지 않는 값으로 만들기 위해 평균값으로 대체
    # NA 를 평균값으로 대체하기 위해서, 평균을 먼저 계산
    print('1) NA 를 평균값으로 대체===========')
    m = s.mean()  # numpy, pandas 의 집계함수들은 NA 를 제거하고 계산함.
    print('평균 = ', m)
    s = s.fillna(m)
    # .fillna(p): 모든 NA를 한꺼번에 p으로 바꿔준다.
    print(s)  # 평균에 영향을 끼치지 않는 값이 되었다.

    # 2) groupby 를 하여 그룹별 평균값으로 대체
    # DataFrame 객체 생성
    print('DataFrame 객체 생성===========')
    df = pd.DataFrame({
        'province': ['서울', '경기', '충청', '전라', '강원', '경상', '부산'],
        'division': ['west'] * 4 + ['east'] * 3,  # ['서울', '경기', '충청', '전라' / west , '강원', '경상', '부산' / east]
        'data': np.random.randint(1, 10, 7)
    })
    print(df)
    # 설명 : ['west'] * 4 + ['east'] * 3 = 'west'를 4번 반복
    # ['west', 'west', 'west', 'west'] + ['east', 'east', 'east'] 리스트끼리 합치기
    # ['west', 'west', 'west', 'west', 'east', 'east', 'east']

    # 데이터 2개를 NA로 대체
    # df.iloc[0, 2] = np.nan
    # df.iloc[6, 2] = np.nan
    df.iloc[[0, 6], 2] = np.nan  # 한 번에
    df.loc[[0, 6], 'data'] = np.nan  # label 사용 -> 행 번호는 자동으로 레이블이 숫자 인덱스가 되니까 사용 가능
    print(df)

    # DataFrame의 NA를 각 그룹별 평균으로 대체
    grouped = df.groupby('division')  # DataFrameGroupBy 객체 생성
    cleaned = grouped.apply(fill_group_mean)  # DataFrameGroupBy 객체에 apply 함수 적용
    # 작동원리 : dataframe 자체를 apply에 넘겨버림 (원래는 row 1개, col 1개씩 줬었는데)
    # 즉, GroupBy.apply(fn)는 함수 fn의 첫번째 파라미터에 DataFrameGroupvy 객체를 동작함
    # 사용자 정의 함수 또한 DataFrame 이 파라미터로 들어간다고 가정하고 만든다~
    # groupby 가 되어 있는 컬럼의 평균을 출력하는 것!
    print(cleaned)

