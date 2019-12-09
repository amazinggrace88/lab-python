# coding=utf-8
"""
.unstack
as_index = False
"""
import pandas as pd

if __name__ == '__main__':
    # csv 파일에서 데이터 프레임을 생성
    emp_df = pd.read_csv('emp_df.csv')
    print(emp_df.head())
    print(emp_df.iloc[0:5])  # 같은 내용
    
    # 부서별, 직책별 직원 수 출력
    grouped = emp_df.groupby(['DEPTNO', 'JOB'])
    # print(grouped['EMPNO'].count())
    emp_by_dept = grouped['EMPNO']
    result_df = emp_by_dept.agg('count')
    print(result_df)  # 컬럼 1개짜리 df(series)

    # .unstack() 으로 df 풀어주기
    # -> 2 개짜리 그룹으로 묶였던 것들의 1개 기준이 컬럼으로 왔다. (행의 인덱스에서 열의 인덱스로)
    # -> 정수는 실수로 바뀌었다 (NaN 이 생겼기 때문)

    print(result_df.unstack())
    print(result_df.unstack().shape)  # 3행 5열

    # as_index=False : 인덱스가 아니라 컬럼 이름으로 job 을 주고 싶을 때
    # 즉, grouping 기준이 되는 컬럼의 값들이 index(행의 이름)으로 사용되지 않고, 컬럼으로 사용하려면 as_index=파라미터를 전달~
    grouped = emp_df.groupby('DEPTNO', as_index=False)
    print(grouped['EMPNO'].count())  # index 는 자동으로 0, 1, 2가 되었고, deptno가 컬럼이 되었다.

    grouped = emp_df.groupby(['DEPTNO', 'JOB'], as_index=False)
    print(grouped['EMPNO'].count())

