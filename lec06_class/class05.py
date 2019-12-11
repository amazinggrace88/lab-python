# coding=utf-8
"""
클래스 만들기 연습 : 직사각형 만들기
"""

class Rectangle:
    """
    직사각형 클래스
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def info(self):
        print(f'Rectangle(w = {self.width}, h = {self.height})')

    def area(self):
        return self.width * self.height

    # ==연산자를 사용했을 때 자동으로 호출되는 메소드
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    # 객체의 내용을 print 할 때 자동으로 호출되는 메소드
    def __str__(self):
        # return f'<{__name__}.Ractangle object at {self}>' # 기본 형태
         return f'<{__name__}.직사각형 객체>'  # 주소를 접근, 변경하지 못하기 때문에 주소값 써주지 않았음


if  __name__ == '__main__':
    rect1 = Rectangle(3, 2)  # 이 파일에서만 생성자 호출
    # rect1 = Rectangle() # 기본값 없으면 error!
    # 파라미터에 기본값 넣어주어야 함 (why? __init__은 함수이므로 self를 제외한 파라미터를 반드시 넣어야함 -> 해결방법 : default argument)
    print(type(rect1)) # 타입
    print(id(rect1)) # 주소값
    rect1.info()
    print(rect1.info()) # info의 return값 = none -> rect1.info() & none이 출력됨

    rect2 = Rectangle(1) # positional argument & default argument
    rect2.info()

    rect3 = Rectangle(height=3) #keyword argument
    rect3.info()

    rect4 = Rectangle(2,3) # positional argument
    print('rect 넓이 : ', rect4.area())
    rect4.info()

    rect5 = Rectangle(width=2, height=3)
    rect5.info()
    print(id(rect5)) # 숫자와 문자열이 아니면, 객체는 항상 만들때마다 생성된다.


    # 연산자 동작방식을 위한 예시
    print(rect4 == rect5) # rect4와 rect5를 출력하면, 같지 않다 (heap 내에 두개의 객체 생성되었다)고 출력됨
    # 두개의 객체의 주소를 비교하고, object가 2개 생겨나기 때문에
    # 만약, 두개의 객체가 다른 주소에 있는 것은 신경쓰지 않고, 모양이 같으면 같다고 이야기하고 싶을때는? eq라는 함수를 만들자. (bool함수)
    print(rect4 == rect5) # eq라는 함수를 class에 만든 후


    # 연산자의 동작방식 (obj1 == obj2 비교 방법)
    # == 연산자는 클래스의 __eq__ 함수를 호출 -> 즉, obj1 == obj2가 obj1.__eq__obj2가 되고, obj1이 self, obj2가 other 가 된다.
    # 개발자가 클래스를 정의할 때 __eq__ 메소드를 정의하지 않아도 모든 클래스는 __eq__ 메소드를 가지고 있음
    # 기본 __eq__ method는 개체들의 주소값(id)를 비교함
    # 개발자는 __eq__ 메소드를 주소값 비교가 아니라 다른 방식으로 작성하여 바꿀 수 있고, ==연산자는 개발자의 의도대로 True/False를 리턴하게 된다.

    print(rect5)
    # 숫자나 문자를 제외하고 (예시_직사각형일 때) 프린트할때의 기본포맷
    # <__main__.모듈 Rectangle클래스이름 object객체 at 0x0000015456584388주소값>
    # 숫자나 문자가 아닌 객체를 16진수로 만들어주는 함수 __str__

