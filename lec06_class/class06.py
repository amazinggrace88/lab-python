# coding=utf-8
"""
원 만들기
"""
from math import pi

class Circle:
    # field : 반지름(radius)
    # method :
    # __init__(): 초기화 (객체 생성) 함수
    # area() : 원의 넓이를 리턴
    # perimeter() : 원의 둘레 길이를 리턴
    # __str__() : Circle(r=123) 형식
    # __eq__() : 반지금이 같으면 True

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0: # 음수가 들어온 경우에만 error 출력! str 일 경우에는 < 연산자를 쓸 수 없어 typeerror 출력
            raise ValueError('반지름은 0 또는 양수')


    def area(self):
        return self.radius**2 * pi


    def perimeter(self):
        return 2 * self.radius * pi


    def __str__(self):
        return f'r = {self.radius}'


    # sorting 을 위한 method
    def __eq__(self, other):
        print('__eq__ 호출')
        return self.radius == other.radius # 같은 종류의 circle


    def __ne__(self, other):
    # not equal : __eq__의 반대함수로 != 연산자를 사용하면 자동으로 호출되는 메소드이다.
    # 주의: __eq__함수를 만들면 != 연산자는 __eq__의 반대값을 자동으로 준다. 즉, __ne__는 필요없는 함수이다.
    # 가능하면 eq, ne 둘 중 하나의 함수만 만들고, 둘 다 만드는 경우 서로 반대의 값을 return하도록 해주어야 한다.
        print('__ne__ 호출')
        return self.radius != other.radius


    def __gt__(self, other):
        # grater than : > 연산자를 사용하면 자동으로 호출되는 메소드
        print('__gt__ 호출')
        return self.radius > other.radius


    def __ge__(self, other):
        # grater than or equal to : >= 연산자를 사용하면 자동으로 호출되는 메소드
        # return self.radius >= other.radius : 계산이 간단한 경우 추천
        return self.__gt__(other) or self.__eq__(other) # 비교해야 할 대상 많은 경우 추천


    #__lt__ : less than (<)
    #__le__ : less than or equal to (<=)

    # representation : 못들었음. 다시 복습하기
    def __repr__(self):
        return f'원({self.radius})'




if __name__ == '__main__' :
    cir1 = Circle(8)
    print(cir1)
    print('cir1 area:', cir1.area())
    print('cir1 perimeter: ', cir1.perimeter())
    print(type(cir1))
    print(id(cir1))  # 주소값 2058278017480

    cir2 = Circle(8)
    print(id(cir2)) # 주소값 1670209881544

    print(cir1 == cir2) # 주소값은 다르나 같다고 호출됨 why? cir1.__eq__(cir2) 라는 함수의 return값이 호출되므로
    # 왜 중요한가 : 리스트에 값을 저장하고 정렬하기 위해, 비교해야 같은지 다른지 알 수 있다. (원의 크기를 어떻게 비교할건지 기준을 마련하기 위해서 - sort를 사용하기 위해서)
    print(cir1 != cir2) # !=는 ==의 반대이기 때문에 cir1.__eq__(cir2) return값의 반대를 호출
    # __ne__ 메소드가 있는 경우, != 연산자는 __ne__ 메소드의 리턴값을 사용
    # 비교하고 싶을 때 __eq__는 필수로 만들어야 한다. *****
    print(cir1 > cir2)
    print(cir1 >= cir2)
    print(cir1 < cir2)  #gt > 의 반대
    print(cir1 <= cir2) #gt > 의 반대 or eq = 의 합집합

    circles =[ # 리스트 형태로 circle 저장
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(0)
    ]
    print(circles)


