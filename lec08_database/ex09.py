'''
실습
1) 부서번호를 입력받아서 emp 테이블에서 해당 부서의 직원들의 사번/이름/부서번호 출력
2) 이름을 입력받아서 emp 테이블에서 입력받은 글자가 이름에 포함된 직원들의 사번/이름/급여 출력
'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

# 1) 부서번호를 입력받아서 emp 테이블에서 해당 부서의 직원들의 사번/이름/부서번호 출력
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:

        sql1   = '''select empno, ename, deptno 
                    from emp 
                    where deptno = :deptno'''

        deptno = int(input('부서 번호 입력 >> '))

        cursor.execute(sql1, deptno = deptno)
        # for row in cursor: # tuple로 출력됨
        #     print(row)
        for empno, ename, deptno in cursor: # 성분분해 (=unpacking) : tuple을 각 변수에 값들을 넣는 방식으로 바꾼다.
            print(empno, ename, deptno)

# 2) 이름을 입력받아서 emp 테이블에서 입력받은 글자가 이름에 포함된 직원들의 사번/이름/급여 출력
        # 들여쓰기를 잘 지켜서 작성해주면 with as /with as 에 포함된다.
        print('================================================')

        sql2 = '''select empno, ename, sal
                  from emp
                  where upper(ename) like :keyword''' # 어떤 값이 올지 모르기 때문에 :ename를 넣는다.

        name = input('이름 입력 >> ')
        name = name.upper()          # 입력한 문자열을 소문자로 변환
        name = '%' + name + '%'      # like 검색 위해 %

        cursor.execute(sql2, keyword = name)

        for empno, ename, sal in cursor:
            print(empno, ename, sal)
