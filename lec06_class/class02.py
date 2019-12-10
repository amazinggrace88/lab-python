"""
class = 데이터(필드, field) + 기능(메소드, method) => 데이터 타입
"""


class Score:
    # 생성자를 호출했을 때 필드들을 초기화하는 함수 -> 초기화의 의미 : 변수에 값을 저장
    def __init__(self, korean, english, math):
        self.korean = korean  # field = self.korean
        self.english = english
        self.math = math

    # method : 기능을 넣기 : 데이터를 가지고 무슨 일을 할 것인가?
    def calc_total(self):
        return self.korean + self.english + self.math
        # korean 이라고 쓰면 안됨 => 객체인 self 가 korean 을 가지고 있으므로

    def calc_average(self):
        return self.calc_total() / 3
        # method 안에 위에 만든 method 넣어도 됨 -> self.calc_total() = self.korean + self.english + self.math 값 나옴(호출)


# score 클래스의 객체를 생성
score1 = Score(99, 90, 99)
# score 클래스의 객체 과정
# 1. 생성자 호출 (init이 객체를 만든다 (=instanciate))
# 2. 데이터 + 메소드 여러개를 저장하는 메모리를 확보, init 호출하여 self 에 주소를 준다
# 3. score1(변수_stack 에 존재)이 객체(객체_heap 에 존재)을 참조한다. (score1 -> 참조변수, reference variable)
score1.math = 100
print(score1.calc_total())  # score1의 self 를 argument 로 자동으로 주므로 ()안의 파라미터 넣을 필요 없음.
print(score1.calc_average())


score2 = Score(30, 40, 70)  # 객체가 만들어진다.
print(score2.calc_total())
print(score2.calc_average())  # 대부분 이렇게 쓴다.
Score.calc_average(score1)  # 참고. print(score2.calc_average())와 같은 뜻.
