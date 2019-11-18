'''
실습 2
1) emp, dept 테이블에서 부서번호를 입력받아서 해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름을 출력

'''

# 1) emp, dept 테이블에서 부서번호를 입력받아서 해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름을 출력

import cx_Oracle
import lab_python.lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:

        # sql_oracle = '''select e.empno, e.ename, e.sal, e.deptno, d.dname
        #                 from emp e, dept d
        #                 where e.deptno = d.deptno
        #                       and e.deptno = :deptno'''

        sql_ansi = '''select e.empno, e.ename, e.sal, e.deptno, d.dname
                      from emp e join dept d
                      on e.deptno = d.deptno
                      where e.deptno = :deptno'''

        dept_no = int(input('부서 번호를 입력하세요 >> '))

        # cursor.execute(sql_oracle, deptno=dept_no)
        cursor.execute(sql_ansi, deptno=dept_no)

        for empno, ename, sal, deptno, dname in cursor:
            print(empno, ename, sal, deptno, dname)


