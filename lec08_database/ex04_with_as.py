'''
connection/cursor 간단히 using with as

with.. as 구문을 사용하면
cursor.close()와 connection.close()가 자동으로 호출됨
'''
# 기본 반복문 in database
'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
cursor = connection.cursor()
cursor.close()
connection.close()
'''
# with as를 사용한 기본 반복문 in database
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn: #함수의 실행결과를 conn 에 저장한 뒤, 모두 끝나면 connection.close() 호출
    with conn.cursor() as cursor: # 이 안에서 해야 할 일들 작성
        cursor.execute('select empno, ename, deptno from emp')
        for row in cursor:
            print(row)
# cursor.close 생략
# connection.close 생략
