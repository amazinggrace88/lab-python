'''
실습 : table(table, cursor):

csv 파일을 합쳐주는 두 가지 방법
1 concat : 컬럼 이름들이 동일하다는 가정하에 테이블을 밑으로 합치는 방법(위+아래)
2 merge : 겹치는 컬럼을 찾아서 테이블을 옆으로 합치는 방법(왼쪽+오른쪽)
'''
import cx_Oracle
import pandas as pd


def get_column_names_of(table, cursor):
    # 바깥쪽은 ""로 묶자! why? sql은 ''로 문자열을 묶기 때문에
    sql_insert = f"""select column_name, column_id 
    from user_tab_columns 
    where table_name = '{table.upper()}' 
    order by column_id"""
    # cursor.execute()를 넣어도 되는 이유? with as 에 속해있기 때문!
    cursor.execute(sql_insert)
    emp = [row for row in cursor]
    col_names = [col_name for col_name, i in emp]  # tuple의 첫번째 원소이다.
    return col_names


# 오라클 권장 방법
def get_column_names_of(table, cursor):
    sql_insert = """select column_name, column_id
    from user_tab_columns
    where table_name = :tbl_name
    order by column_id"""
    # 차이점:
    # 1) f"""이 아니다~
    # 2) :tbl_name 으로 콜론(:)으로 시작하는 데이터타입에 맞춰 자동으로 들어가도록 cursor.execute()가 작동한다.
    cursor.execute(sql_insert, tbl_name=table.upper())  # data binding 방식 : tbl_name=table.upper()
    # cursor 가 sql 문장의 :변수 위치에 데이터 타입에 맞게끔 값을 치환해 줌. (ex 값이 문자열이면 '문자열' 형태로 :변수 위치에 치환됨 )
    col_names = [row[0] for row in cursor]  # tuple의 첫번째 원소라는 뜻
    return col_names


def select_all_from(table, cursor):  # 함수 정의할때 선언하는 변수 - 파라미터!
    select_insert = f"""select * from {table.upper()}"""
    cursor.execute(select_insert)
    # from 옆에 table 있는 경우는 formative string 을 쓸 수밖에 없다 (data binding nono)
    # why? 문자열은 ''주어야 하는데, execute()안에 들어가는 select문은 ''가 이미 존재함 (또 ''로 감쌀 수 없음)
    # t = [row for row in cursor]  # cursor는 oracle의 datatype을 python의 datatype으로 변환시켜준다(ex_ hiredate 의 type 변환)
    t = cursor.fetchall()  # cursor 의 list 를 리턴해주는 함수
    table_body = pd.DataFrame(t)
    table_body.columns = get_column_names_of(table, cursor)
    return table_body


def select_all_from(table, cursor):  # 함수 정의할때 선언하는 변수 - 파라미터!
    select_insert = f"""select * from {table.upper()}"""
    cursor.execute(select_insert)
    table_body = pd.DataFrame(cursor)  # cursor 자체를 pandas DataFrame 에 주어도 테이블 만들어짐
    table_body.columns = get_column_names_of(table, cursor)
    return table_body
    # table_body = pd.DataFrame(cursor, get_column_names_of(table, cursor)) 은 작동이 되지 않는다 !
    # - 작동원리 : cursor가 get_column_names_of(table, cursor)에서 column만 가진 cursor로 변경된다. -> cursor는 반복되지 않아서~(일회성이어서)
    # table_body = pd.DataFrame(cursor.fetchall(), get_column_names_of(table, cursor)) 은 작동이 된다 !
    # - 작동원리 : cursor가 위에서 fetchall()까지 해서 cursor.fetchall()이 []가 된다. 그 후 get_column_names_of(table, cursor) 작동된다.
    # - 결론 : 함수에서 cursor 를 두 번 쓰는 것(뜻이 다른 cursor들을 쓴다)은 위험하므로 cursor 는 따로 따로 써주자!

if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')  # localhost 대신 ip주소로 줄 수도 있음! ip주소로 접속하면 다른 사람의 서버도 가능하다.
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # cursor 객체 생성
        with connection.cursor() as cursor:
            # 1)
            emp_columns = get_column_names_of('emp', cursor)  # 함수(table이름, select문장 등을 실행하기 위해 cursor)
            print(emp_columns)  # ['empno', 'ename',.. ] : 리스트 형태로
            # 2)
            emp_df = select_all_from('emp', cursor)  # pandas의 DataFrame 형태로
            print(emp_df)  # DataFrame 은 컬럼 이름(인덱스)가 포함되어 있어야 함.
            # mgr : NaN이 들어있어 실수 타입으로 변환(원래는 정수 타입으로 변환)
            # 3)
            dept_df = select_all_from('DEPT', cursor)
            print(dept_df)
            # 4)
            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            # DataFrame['새로운 컬럼 이름'] = 값(list, pandas.series) : DataFrame 에 새로운 column 을 추가 (dict 와 비슷)
            # emp_df 에 salgrade 컬럼을 추가 : 모든 행마다 sal을 가지고 salgrade 테이블에 비교해서 grade 매기기
            # 1) emp_df['sal'] 갯수만큼 반복
            # 2) emp_df의 sal 이 어느 grade 에 속하는 지를 찾음 (반복문 만들기)
            # 3) salgrade_df의 행 갯수만큼 반복하면서 LOSAL, HISAL와 비교
            # DataFrame.iterrows() 함수 필요 (행 반복) <-> DataFrame.iteritems() (열 반복)
            # 적용 : 분류를 위한 컬럼 붙이기 *****
            sal_grade = []
            for i in emp_df['SAL']:
                # print(i, end=' ')
                # DataFrame.iterrows() 함수: 데이터 프레임의 (행이름, 행)을 반복문 안에서 사용할 수 있도록 함. *****행 별로 반복*****
                # 성분 분해 전) for j in salgrade_df.iterrows():  # j는 tuple(행이름, 행) 자체
                # 성분 분해 후)
                # for name, row in salgrade_df.iterrows():
                for _, row in salgrade_df.iterrows():  # 최종본 : for in 문에서 사용하지 않는 변수 _ 처리
                    # To preserve dtypes while iterating over the rows, it is better to use itertuples
                    # print(name, row)  # (row 의 인덱스=name, row 에 들어가있는 행 자체=row) 를 tuple 로 리턴
                    # 성분 분해 전) if row[1]['LOSAL'] <= i <= row[1]['HISAL']:
                    # 성분 분해 후)
                    if row['LOSAL'] <= i <= row['HISAL']:
                        # 원하는 범위를 찾은 경우
                        sal_grade.append(row['GRADE'])
                        break  # salgrade_df 반복을 중지 - 더 찾을 필요가 없다~ 두 번째 if 문을 나가는 것일 뿐
            emp_df['SAL_GRADE'] = sal_grade  # DataFrame 에 새로운 컬럼을 추가(있으면 새로운 컬럼 내용으로 수정되)
            print(emp_df)

            # pandas.merge: join in pandas
            ''' sql 문장
            select e.empno, e.ename, e.deptno, d.dname
            from emp e join dept d
            on e.deptno = d.deptno;'''
            emp_dept = pd.merge(emp_df, dept_df, on='DEPTNO')  # how=join 방식, on=join 의 기준컬럼
            print(emp_dept)  # [14 rows x 11 columns]
            # pandas.merge(left, right, how, on, left_on, right_on, ...)
            # left, right: 조인할 데이터 프레임
            # how: 조인 방식(inner, left, right)
            # on: 조인할 때 기준이 되는 컬럼 이름
            # 조인할 때 기준 컬럼 이름이 두 DataFrame마다 다르면
            # left_on=left_df의 컬럼이름, right_on=right_df의 컬럼이름

            # emp_df, dept_df 데이터 프레임의 left, right join 결과 비교
            emp_dept_left = pd.merge(emp_df, dept_df, how='left', on='DEPTNO')
            print('emp_dept_left====================\n')
            print(emp_dept_left)

            emp_dept_right = pd.merge(emp_df, dept_df, how='right', on='DEPTNO')
            print('emp_dept_right====================\n')
            print(emp_dept_right)  # [15 rows x 11 columns]

            # emp 테이블에서 mgr 과 empno 가 일치하는 join(self join)
            # 1) inner 2) left 3) right join -> 결과 다 다르다 why? mgr = NaN 있어서
            print('emp_emp_inner====================\n')
            emp_emp = pd.merge(emp_df, emp_df, left_on='MGR', right_on='EMPNO')
            print(emp_emp)

            emp_emp_left = pd.merge(emp_df, emp_df, how='left', left_on='MGR', right_on='EMPNO')
            print('emp_emp_left====================\n')
            print(emp_dept_left)

            emp_emp_right = pd.merge(emp_df, emp_df, how='right', left_on='MGR', right_on='EMPNO')
            print('emp_emp_right====================\n')
            print(emp_emp_right)
            # merge 에서 select 를 바로 할 수는 없다
            # sql - select 와 같은 문장: df['column_name']
            # left table - x, right table - y 가 된다.
            print(emp_emp_right[['EMPNO_x', 'ENAME_x', 'MGR_x', 'EMPNO_y', 'ENAME_y']])

'''
<대문자 변환 방법 - python> 
string.upper() ex_table.upper()
string.capitalize() ex_table.capitalize()
string.title() ex_table.title()
or 
string.upper(table)도 가능하당~
'''

