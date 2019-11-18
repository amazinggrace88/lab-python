'''
Database - oracle (1)
'''
# cx_Oracle 설치 순서
# 1) pip install cx_Oracle in cmd
# 2) file - settings - project - project interpreter - +(package install)
import cx_Oracle
print(cx_Oracle.version)

# sql developer 실행 - 계정 scott / hr ..
# 파이썬에서 필요한 정보(데이터베이스 정보 - DSL / URL): scott계정이름	scott@계정이름//localhost ip주소(pc에 설치된 오라클 데이터베이스 서버):1521 포트/orcl (sid)