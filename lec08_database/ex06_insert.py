'''
insert - prompt 사용자 입력 받아 oracle에 저장

사용자 입력을 받아서 데이터베이스에 insert - case 1. f'' 사용
'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

# case 1. f'' 사용
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서번호를 입력>> '))
        dname  = input('이름 입력>> ')
        loc    = input('위치 입력>> ')
        # 이 세가지 정보를 가지고 sql 문장(insert문)을 만들자
        # sql_insert = f"insert into dept2 values({deptno}, {dname}, {loc})" # sql의 문자열은 따옴표로 묶어야 해서 error.
        sql_insert = f"insert into dept2 values({deptno}, '{dname}', '{loc}')"
        # case 1의 문제 : 이름 입력>> I'm a girl
        # f"insert into dept2 values('I'm a girl') 이 되어서 전혀 엉뚱한 문장이 되어버림
        # 사용자가 입력한 문자열에 따옴표가 포함되어 있는 경우 sql 에러가 발생할 수 있어 권장하지 않는 방법
        # -> data binding 방법을 권장.
        cursor.execute(sql_insert)
        connection.commit()

