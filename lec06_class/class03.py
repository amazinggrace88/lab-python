'''
클래스 작성, 객체 생성, 메소드 사용 연습
'''
class Employee:
    """
    field : empno, ename, salary, deptno # __init__()로 변수 초기화 필요
    method : raise_salary(self, pct) # percent 줄여서 pct
    """
    def __init__(self, empno, ename, salary, deptno): # __init__문에도 if 문 넣을 수 있다!
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno

    def raise_salary(self, pct):
        """
        인상된 급여를 리턴

        :param pct: 급여 인상율(0.1 = 10%, etc)
        :return: 인상된 급여
        """
        # self.salary = (1+pct)*self.salary
        self.salary *= (1 + pct)
        return self.salary


    def __repr__(self):
        return f'(사번 :  {self.empno}, 이름 : {self.ename}, 급여 : {self.salary}, 부서번호 : {self.deptno})' # 모든 사원을 모두 똑같은 모양으로 출력하여 table처럼 만들기 위함

gil_dong = Employee(1010, '홍길동', 1000, 10)
print(gil_dong.__repr__())
gil_dong.raise_salary(0.1)
print(gil_dong.__repr__())

scott = Employee(1011, 'Scott', 10000, 20)
print(scott.__repr__())
scott.raise_salary(-0.1)
print(scott.__repr__())

ohsam = Employee(1012, 'ohsam', 500, 30)


# list 만들기
employees = [ohsam, gil_dong, scott]
print(employees) # __repr__ :

# cf. refactoring : shift + F6
# do refactor -> 한번에 변수 모두 다 바꿔버리기.

# 정렬하기 : 기준을 주지 않았을 때 - 상황에 따라 정렬기준이 달라질 때
# print(sorted(employees)) # error
print(sorted(employees, key=lambda x: x.empno))
print(sorted(employees, key=lambda x: x.salary))
print(sorted(employees, key=lambda x: x.ename))
# 람다식 의미 : 기준은 사번 key를 기준으로 grater than (__gt__)함수를 적용한다.
# key=lambda x라는 사람이 있으면 : x.empno의 기준에 의해 정렬하라.
# reverse 는 오름차순 파라미터
# utf-8로 문자열을 저장하므로, 문자열 비교시 참고할 것

