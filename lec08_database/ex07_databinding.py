'''
insert - prompt 사용자 입력 받아 oracle에 저장

사용자 입력을 받아서 데이터베이스에 insert - case 2. DATA binding : 권장 방법

--data binding의 2가지 방법--
1)
2)

'''
import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

# case 2. DATA binding : 권장 방법
# 1)
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>> '))
        dname  = input('부서 이름 입력>> ')
        loc    = input('부서 위치 입력>> ')

        sql1 = 'insert into dept2 values(:0, :1, :2)'
        # : 을 사용한다 = 비어있다는 표시, 순서대로 쓰지 않아도 상관없다. (oracle방식)
        cursor.execute(sql1, [deptno, dname, loc]) # 두번째 매개변수로 list를 만들어 변수들을 넣어준다.
        # :0, :1, :2 = deptno, dname, loc 매치된다. 자동으로 따옴표 들어가서 문자열로 만들어줌
        connection.commit()

# 부서 번호 입력>> 12
# 부서 이름 입력>> LA's startup ---> 입력 가능!
# 부서 위치 입력>> maiami


# case 2. DATA binding : 권장 방법
# 2)
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>> '))
        dname  = input('부서 이름 입력>> ')
        loc    = input('부서 위치 입력>> ')

        sql2 = 'insert into dept2 values(:dept_no, :dept_name, :loc)'
        cursor.execute(sql2,
                       dept_no   = deptno,
                       dept_name = dname,
                       loc       = loc
                       ) # parameter 이름 = 변수 이름 : 장점 파라미터와 변수의 정확한 일치 눈으로 확인 가능
        connection.commit()

