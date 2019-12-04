'''
ex05_insert.py

'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

# db server와 연결 설정
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    # SQL 문장 실행, 결과 분석할 수 있는 cursor 객체를 생성
    with connection.cursor() as cursor:
        sql_insert = "insert into dept2(deptno, dname, loc) values(91, '강의장10', 'Seoul')"  # 안에 작은 따옴표 있으므로 바깥쪽은 큰 따옴표
        # or sql_insert = "insert into dept2 values(91, '강의장10', 'Seoul')"
        cursor.execute(sql_insert)
        # DML (Data Manipulation Language) : INSERT UPDATE DELETE
        # DML 결과를 영구적으로 반영하기 위해서는 commit을 해야 함.
        connection.commit()

        sql_select = "select * from dept2" # 변수 선언해서 문자열 만들고
        cursor.execute(sql_select)         # 함수에 넣는다. why? sql문이 길어지면 이러한 방식이 더 편리
        for row in cursor:
            print(row)
            
# cf
# python에서 insert한 결과는 commit하지 않으면 oracle에 저장되지 않는다.
# why? 각 프로그램은 커넥션으로 이어지고 있다. insert는 변경사항을 commit해야 하드디스크에 저장 -> sql developer에 저장 가능하다
# server에 있는 하드디스크에 영구적으로 저장 = commit
