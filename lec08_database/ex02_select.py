'''
Database - oracle (2) : 검색 select - using cursor

Oracle 데이터베이스 서버에서 select 구문 실행, 결과 확인 - using cursor
(withline을 계속 호출하는 것과 동일한 절차)
'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

# 데이터베이스 서버와 연결 설정 - 접속! (로그인)
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
# 서버에 접속하기 위해 유저아이디,비밀번호,주소를 connect에 쓴다.
# 사용할 때 접속, 사용하고나서는 접속을 해제함(로그아웃)
# (DB를 당겨두기 때문에, connect가 여러 pc이고 connection 갯수는 제한되어 있다.)

print('DB version : ', connection.version)

# 해야 할 일들 작성
# SQL 문장을 실행시키기 위해서 cursor 객체를 생성
# cursor란? 실행결과를 가지고 있는 객체 in oracle (복습하기)
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')
# warning! 문장 끝에 ;(semicolomn)쓰면 안됨
# select문의 결과(table)에 cursor는 행 하나의 인덱스를 가리킨다.(읽어오겠다는 메소드 호출 -> 그 다음줄로 바뀐다)
# cursor : file pointer -> 결과 첫번째 줄, 두번째 줄,, 을 줄마다 읽을 수 있는 도구
# 무한루프를 사용하여 쉽게 table을 가져올 수 있다.
'''
# while True:
     row = cursor.fetchone()
     if row is None: #더이상 select의 결과가 없다면
         break
     print(row)
'''
# or
row = cursor.fetchone()     # 첫번째 row를 먼저 가져옴
while row:                  # row가 true일때만 fetchone()
    print(row)              # database의 한 row에 해당하는 record를 tuple로 출력
    row = cursor.fetchone() # 그 다음 row를 fetchone()


# cursor 객체 사용 후 리소스를 반환 (close 반환)
cursor.close()


# 데이터베이스 서버와 연결 종료
connection.close()



# oracle 기본 connection-close
'''
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
cursor = connection.cursor()
cursor.close()
connection.close()
'''



