'''
실습

sql 문장 만들기
deptno 를 입력받아서 해당 부서의 loc 를 update 문장 만들어 실행
'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg


with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력 >> '))
        loc    = input('수정할 부서 위치>> ')

        sql1   = 'update dept2 set loc = :10 where deptno = :21' # 변수는 중요하지 않다. (숫자 아무거나 써도 됨) 그렇지만 매칭 순서는 중요하다.
        cursor.execute(sql1, [loc, deptno])
        connection.commit()

        print('==============================================')

        deptno = int(input('부서 번호 입력 >> '))
        loc = input('수정할 부서 위치>> ')

        sql2 = 'update dept2 set loc = :loc where deptno = :dept_no'
        cursor.execute(sql2, dept_no = deptno, loc = loc)
        connection.commit()