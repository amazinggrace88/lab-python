'''
Database - oracle (3) : 검색 select - using for - in 구문

Oracle 데이터베이스 서버에서 select 구문 실행, 결과 확인 - using for - in 구문

for in 구문을 이용한 select 결과 처리
for 변수 in 커서:
    실행문
=> for-in 구문에서 cursor.fetchone()의 결과를 변수에 전달
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
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg


# connection connect
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)


# cursor
cursor = connection.cursor()


# sql 문장 실행
cursor.execute('select * from dept')


# select 결과 처리
for row in cursor: # select문의 결과가 cursor가 저장되어 cursor는 1줄씩 읽는다.(fetch - 이동하면서 읽는 기능)
    print(row)

# cursor close
cursor.close()


# connection close
connection.close()

