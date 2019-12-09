# coding=utf-8
'''
실습 : 
집계 함수(pandas.Series 또는 pandas.DataFrame 클래스가 가지고 있는 메소드들: count, mean, sum.. ) 사용하여
DataFrame 에서 grouping 하여 특정한 열 추출
'''
import csv
import pandas as pd
import cx_Oracle

from lab_python.scratch09.ex10 import select_all_from


def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    # with~as 구문을 사용, oracle db server 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # with~as 구문을 사용, cursor 객체 생성
        with connection.cursor() as cursor:
            emp_df = select_all_from('emp', cursor)
            # cursor.execute('select * from emp')
            # emp = [row for row in cursor]
    # scratch09 패키지에서 테이블 전체 검색 함수를 사용해서(import) emp_df 데이터 프레임을 생성
    # file_path = 'emp.csv'

    # emp_df 를 csv 파일로 저장 (오라클 연결 안해도 읽어올 수 있도록)
    # with open(file_path, mode='w', encoding='UTF-8', newline='') as f:
    #     writer = csv.writer(f)
    #     for item in emp:
    #         writer.writerow(item)
    emp_df.to_csv('emp_df.csv', index=False)
    # emp_df = pd.read_csv('emp.csv', header=None)
    # emp_df.columns = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']
    # print(emp_df)

    # emp_df 에서 부서별 평균 급여를 출력
    g1 = emp_df.groupby(by='DEPTNO')
    emp_sal = g1['SAL']
    print(emp_sal.mean())  # 가능!
    # emp_df 에서 부서별 인원수를 출력 (primary key)
    dept_cnt = g1['EMPNO'].count()
    print(dept_cnt)
    # emp_df 에서 부서별 급여 최솟값 출력
    min_sal = g1['SAL'].min()
    print(min_sal)
    # emp_df 에서 부서별 급여 최댓값 출력
    max_sal = g1['SAL'].max()
    print(max_sal)

    # 1) DataFrame 으로 만들기! -> deptno는 index! (label)
    all_df = pd.DataFrame({
        'count': dept_cnt,
        'mean': emp_sal.mean(),
        'min': min_sal,
        'max': max_sal
    })
    print(all_df)
    print(all_df.shape)

    # 2) agg(), aggregate() 사용
    # 2) - 1 : ['함수이름', '함수이름', .. ]
    # agg(), aggregate() 두 개 다 똑같은 함수: 파라미터에 함수 이름을 전달하면 groupby 객체에 함수를 적용한다.
    all_df2 = emp_sal.agg(['count', 'mean', 'min', 'max'])
    print(all_df2)
    # 함수가 집계 함수(pandas.Series 또는 pandas.DataFrame 클래스가 가지고 있는 메소드들: count, mean, sum.. )인 경우에 함수 이름을 문자열로 전달한다.
    # g1.mean() = g1.agg('mean')
    print(emp_sal.agg(pd.Series.mean))  # <->  print(emp_sal.agg(mean)) error! mean 이라는 함수를 정의할 수 없어서 (pd.Series.mean)
    # 모든 함수 이름을 문자열로 주는 것은 아니니 주의하자 : 정확히는 함수의 이름을 주어야 하는 것 원칙! - 직접 작성한 함수는 함수 이름을 그냥 파라미터에 전달해요~ ('' 없음)
    # ex
    # all_df2 = emp_sal.agg(['count', 'mean', 'min', 'max', 'peak_to_peak']) error!
    # peak_to_peak : 함수 이름만 써준다. peak_to_peak()는 바로 호출하는 함수이므로 여기서 실행하면 안됨!
    all_df2 = emp_sal.agg(['count', 'mean', 'min', 'max', peak_to_peak])

    # 위의 모든 작업을 직책별로 직원수, 급여 평균, 최소, 최댓값 출력
    grouped_by_job = emp_df.groupby('JOB')
    sal_by_job = grouped_by_job['SAL']
    # grouped_by_job = emp_df.groupby('JOB')['SAL'] 로도 쓸 수 있음
    print(sal_by_job.agg(['count', 'mean', 'min', 'max', peak_to_peak]))
    print(sal_by_job.agg(['count', 'mean', 'min', 'max', lambda x: x.max() - x.min()]))
    # lambda 식 가능! 대신 <lambda_0>으로 컬럼명 나와서 고쳐야됨
    # agg 함수가 만드는 DataFrame 의 컬럼 이름을 설정하는 방법: keyword argument 방식 or dict 를 파라미터로 전달한다.

    # 2) - 2 : keyword argument
    # keyword argument: 컬럼이름 = 함수 (DataFrame)
    print(sal_by_job.agg(Count='count', Average='mean', Minimum='min',  Maximum='max', Range=lambda x: x.max() - x.min()))

    # 2) - 3 : dict {'key':'value'}
    # emp_df 에서 부서별, 직책별 직원수, 급여 평균, 최소, 최댓값 출력
    # { '컬럼이름': '함수이름' }
    # -  future warning : pandas 패키지가 업그레이드 될 때 없어질 수 있는 기능(deprecated), dict 방식보다는 keyword argument 방식을 쓰는 것이 좋다
    grouped = emp_df.groupby(['DEPTNO', 'JOB'])
    sal_by_dept_job = grouped['SAL']
    df = sal_by_dept_job.agg({
        'Count': 'count',
        'Average': 'mean',
        'Minimum': 'min',
        'Maximum': 'max',
        'Range': lambda x: x.max() - x.min()
    })
    print(df)

    # 2) - 4 : [('컬럼이름', '함수이름')]
    # 리스트 안에 튜플 형식으로 쓰는 방법
    # print(result_day_2.agg([('average', 'mean'), ('stddev', 'std'), ('range', peak_to_peak)]))  -- ex04 에 예시 있음
