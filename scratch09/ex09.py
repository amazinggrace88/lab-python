'''
- emp.csv파일을 읽어서 df생성
- boolean indexing 사용)
- 급여(sal)이 2000이상인 직원들의 모든 정보를 출력
- 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
- 급여가 전체 직원 급여의 평균보다 많은 직원의 사번, 이름, 급여(column)를 출력
- 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
- 20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호를 출력
- 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인 직원들의 모든 정보를 검색
- 사원 이름에 'E'가 포함된 직원들의 이름만 출력 (str.contains() 이용)
- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 실행
- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 데이터 프레임을 파일로 저장
'''
import pandas as pd

if __name__ == '__main__':
    file_path = 'emp.csv'
    # pandas.read_csv() 함수는 csv 파일의 첫번째 줄을 헤더(컬럼 이름)으로 취급.
    # csv 파일의 첫번째 줄이 헤더(컬럼 이름)이 아니고 실제 레코드인 경우, header=None 파라미터를 추가하자
    emp = pd.read_csv(file_path, header=None)
    print('shape = ', emp.shape)  # header = None 일때 : 14 명 / header=None 없으면 13 명(행), 8 명(열)
    print(emp.head)  # label 을 숫자로 자동 부여했다~
    # cf. pandas.read_csv() 가 텍스트 편집기보다 빠르기 때문에 텍스트 편집기를 열 때보다 판다스에서 불러오는 게 빠르다.

    # DataFrame 에 컬럼 이름을 설정
    emp.columns = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']
    print(emp.iloc[0:2])

    # - 급여(sal)이 2000이상인 직원들의 모든 정보를 출력
    print('\n급여(sal)이 2000이상인 직원들의 모든 정보를 출력')
    print(emp[emp['sal'] >= 2000])  # df[조건식]

    # - 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
    print('\n부서 번호(deptno)가 10인 직원들의 모든 정보를 출력')
    print(emp[emp['deptno'] == 10])

    # - 급여가 전체 직원 급여의 평균보다 많은 직원의 사번, 이름, 급여(column)를 출력
    print('\n급여가 전체 직원 급여의 평균보다 많은 직원의 사번, 이름, 급여(column)를 출력')
    # subset = emp[급여>평균] 단계를 나눠서 생각하자 - 코딩!
    subset = emp[emp['sal'] > emp['sal'].mean()]
    print('sal mean= ', emp['sal'].mean())
    print(subset[['empno', 'ename', 'sal']])
    # sql : select empno, ename, sal from emp where sal > (select avg(sal) from emp);

    # - 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
    print('\n30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력')
    c1 = emp['deptno'] == 30  # condition 1
    c2 = emp['job'] == 'SALESMAN'  # condition 2 - 문자열 비교는 대소문자 구분 잊지 말자~
    subset = emp[c1 & c2]  # boolean 조건식 - sql의 where 절과 유사함
    print(subset[['empno', 'ename', 'sal', 'deptno']])  # index에 [[]] 주의해요~
    # or
    subset = emp[(emp['deptno'] == 30) & (emp['job'] == 'SALESMAN')]  # 한 번에 할 때에는 괄호를 지정해서 & 로 묶어주기~
    # sql : select empno, ename, sal, deptno from emp where deptno == 30 and job == 'SALESMAN';

    # - 20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호를 출력
    print('\n20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호를 출력')
    # c1 = emp['deptno'] == 20
    # c2 = emp['deptno'] == 30
    c1 = emp['deptno'].isin([20, 30])  # oracle in() 연산자와 비슷한 역할: value 를 [list]로 보내주어야 한다.
    c2 = emp['sal'] > 2000
    subset = emp[c1 & c2]
    print(subset[['empno', 'ename', 'sal', 'deptno']])
    # sql : select empno, ename, sal, deptno from emp where (deptno = 20 or deptno = 30) and sal > 2000;
    # sql : select empno, ename, sal, deptno from emp where deptno in(20, 30) and sal > 2000;

    # - 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인 직원들의 모든 정보를 검색
    print('\n수당이 없는 직원들 중에서, 매니저가 있고, 직책이 \'MANAGER\' 또는 \'CLERK\'인 직원들의 모든 정보를 검색')
    c1 = emp['comm'].isna()  # == np.na 로 비교하면 안된다 why? 비교할 대상 자체가 없다 : .isna() = .isnull() = 컬럼의 값이 없는 컬럼들.(수당이 없는 직원들)
    c2 = ~emp['mgr'].isna()  # not 연산자: '~'
    # c3 = (emp['job'] == 'MANAGER') | (emp['job'] == 'CLERK') : |를 써야하는 이유 -> 모든 컬럼들을 한 조건씩 비교해야 하기 때문에 (bitwise : 각 비트에 적용된다)
    c3 = emp['job'].isin(['MANAGER', 'CLERK'])
    subset = emp[c1 & c2 & c3]
    print(subset)
    # sql: 내가 복습하면서 작성하기
    
    # cf. bitwise 연산자
    # {and:&} {or:|} {!:~}

    # 사원 이름에 'E'가 포함된 직원들의 이름만 출력 (str.contains() 이용)
    print('\n사원 이름에 \'E\'가 포함된 직원들의 이름만 출력')
    subset = emp[emp['ename'].str.contains('E')]  # sql: like '%E%'-> 문자열인 경우 '.str.'이 필요하다
                                                        # why? emp['ename']가 문자열을 item으로 갖는 series이기 때문에 하나씩 꺼내서 문자열로 만든다.
                                                        # .contains가 .str의 메소드
    ''' emp['ename'].str.contains('E') 의 작동원리
    r = []
    for x in list:
        if x.contains('E'):  # 문자열이 E를 가지고 있으면
            r.append(True)   # True
        else:
            r.append(False)'''
            
    print(subset['ename'])  # series: 위에 컬럼 이름이 없다 (1차원 리스트를 pandas에서는 series라고 부른다)
    print(subset[['ename']])  # DataFrame: 위에 컬럼 이름이 있다 (sub dataframe)

    # DataFrame.to_csv(file_path): DataFrame 을 csv 파일로 저장
    emp.to_csv('emp2.csv', index=False)
    # to_csv() 설명
    # column name 있음 -> ok good column name 원하지 않으면 : header= (문서 볼때에 우리가 쓰고 있는 버전과 같은지 고려하기)
    # row 인덱스 들어가 있음 -> index= : rowname 쓸 것인지 (기본값 True)
    # 파싱? 형 변환?
    # 데이터 전처리 -> 데이터 1개씩 for 문을 돌리면 가능! ex_ int(mgr) why? NULL값이 있기 때문에 정수로 변환되지 않았음.
    # 정규표현식 : 정규 표현식(regular expression, 간단히 regexp 또는 regex) 또는 정규식은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어이다.