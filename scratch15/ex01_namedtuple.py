"""
named tuple

#  행 = row = observation = record = example
#  열 = col = 변수 = 특성
"""
from collections import namedtuple
from typing import NamedTuple

# tuple
# 번호, 이름, 수학점수, 과학점수, 컴퓨터점수 -> 컬럼은 특성을 나타내는 거야~
student_1 = (1, 'grace', 10, 20, 30)
print(f'번호 : {student_1[0]}')
print(f'과학점수 : {student_1[3]}')


# tuple type 단점:
# 해당 인덱스의 원소가 무슨 값을 의미하는지 파악하기 어렵다.
# (0번이 무엇인지? 3번 무엇인지? DF의 구조를 알기전에는 파악 x)
# 특정 원소에 접근(값을 read, write)하기 위해서는 인덱스만 사용하여야 한다.

# 해결책 : key, value 를 사용하는 dict + tuple = named_tuple!
# (dict는 key 가 있어서 key 값을 기준으로 value 찾거나 value 값을 기준으로 key 값을 찾을 수 있음)


# namedtuple 사용방법
# 정수 인덱스가 아니라 문자열 인덱스로도 접근 가능~! 각 원소들의 특성 구분이 쉽다!
# 대신 dict 처럼 바뀌지 않아 tuple 성질을 가진다.
# step1. 프로토 타입 지정
# (단점 - 변수 이름과 tuple 이름이 같게 지정)
# (단점 - field 이름을 ''쓴다, abc-d 라고는 못쓴다, 기본값 못씀)
# python ver 3.6 ~ 단점을 보완하기 위해 NamedTuple 을 class 처럼 선언하는 방식이 만들어짐
Student = namedtuple('Student', ('no', 'name', 'math', 'science', 'cs'))  # import 및 구조 지정!


# step1. (python ver 3.6 ~) 클래스 선언 방식으로 프로토함수 지정
# (장점 - 클래스가 가지고 있는 여러가지 메소드도 사용 가능)
# (장점 - '' 안써도 됨, field 쓸 때 - error 알려줌)
# (장점 - field 에 기본값 쓸 수 있음)
class Student2(NamedTuple):
    # NamedTuple 임포트, Student2 클래스는 NamedTuple 클래스를 상속받는다는 의미
    # NamedTuple 만의 특징 : field 선언 - 변수 타입 annotation 을 반드시 추가해야 해요~
    no: int
    name: str
    math: int
    science: int
    cs: int


# step2. Student 프로토타입을 함수처럼 쓰기
student_2 = Student(3, '허균', 100, 100, 100)
print(student_2)  # (key=value, key=value, key=value.. )
print(f'번호 : {student_2[0]}, {student_2.no}')  # student_2.(field no 선택)
print(f'수학점수 : {student_2[2]}, {student_2.math}')
# self.field 찾아서 쓰는 것이 하나의 인덱스 타입이 되었다~

student_3 = Student2(4, '허균2', 90, 90, 100)  # 생성자 호출
print(student_3)
print(f'번호 : {student_3[0]}, {student_3.no}')
print(f'수학점수 : {student_3[2]}, {student_3.math}')
