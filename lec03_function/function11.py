'''
< function is first-class object! >

함수는 1급 객체이다.
- 함수를 변수에 저장할 수 있음 in python
- 매개변수(parameter)에 함수를 전달할 수 있음
- 함수가 다른 함수를 return 할 수 있음
- 함수 내부에서 다른 함수를 정의할 수 있음
- 원리 : 함수 코드 자체가 object와 같은 형태여서 heap 상에서 주소값을 가지므로, stack 상에서 주소값을 주는 원리

'''


# 실습 1 함수 자체를 변수에 저장하기
def twice(x):
    return 2 * x

result = twice(100) # 함수 호출 : return값인 200이 result에 저장됨 (함수 리턴값 저장)
print(result) # 리턴값을 출력

double = twice # 함수 자체를 변수에 저장
print(double) # <function twice at 0x00000182CCB60F78> twice라는 함수가 주소 0x00000182CCB60F78에 있다. double은 주소를 저장하였음.
# 변수에 저장하고 다른 함수에 파라미터로 저장하는 것이 가능함.

result = double(11) # 함수 호출
print(result) # double이라는 함수를 호출하면 twice라는 함수가 실행됨


# 실습 2 매개변수에 함수 저장하기
# 매개변수는 변수이기 때문에 - 실습 1 활용
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def calculate(x, y, operator):
    return operator(x, y) # 함수를 호출함 (값을 return)
# 설명 : x, y, operator라는 파라미터, operator는 함수 자체를 넣어주어 함수 역할을 하게 한다. (like double = twice -> operator = plus)
# result = calculate(1, 2, plus()) # plus():함수를 호출했음 : return값을 넣어주었다
result = calculate(1, 2, plus)
print(result)
result = calculate(1, 2, minus)
print(result)
# 활용 : 라이브러리의 함수 계산 과정을 이해함과 상관없이 함수를 가져다 써서 다른 함수를 만들 수 있다.


# 실습 3 함수 내부에서 함수를 정의하기
def decorate(func):
    print('decorate 함수 내부 :', func.__name__)
    # decorate 함수 내부에서 wrapper_function 함수를 정의
    def wrapper_function(*args):
        print('다음 함수를 실행 :', func.__name__)
        return func(*args)
    # decorate 함수에서 다른 함수(wrapper_function)을 리턴
    return wrapper_function

# 내부함수는 바깥쪽 함수를 모두 사용할 수 있다.
# 함수 디자인 중 decorate 패턴이라고 함(찾아보기)
wrappeer = decorate(print)
wrappeer('a')

