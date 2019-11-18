'''
Oracle_config.py

Oracle 데이터베이스 서버에 접속(로그인)하기 위해 필요한 정보들을 정의
'''

# Oracle 데이터베이스 서버에 접속(로그인)하기 위해 필요한 정보
# 1) 사용자 이름
# 2) 비밀번호
# 3) 데이터베이스 서버 주소: DSN Data Source Name


# 1) 사용자 이름
user = 'scott'
# 2) 비밀번호
pwd = 'tiger'
# 3) 데이터베이스 서버 주소 : DSN
dsn = 'localhost:1521/orcl' # localhost:1521 ip주소 자신의 컴퓨터 번호 써야 함
