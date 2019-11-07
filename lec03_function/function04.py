'''

'''

# 함수 정의
def test(x, y):
    print(f'x = {x}, y = {y}')
    return x + y, x - y


# 함수 호출
# test() : TypeError 발생
# python 함수의 파라미터 타입은 검사하지 않지만, 파라미터 갯수는 검사함.(파라미터 갯수에 맞게 값을 넣어야 한다)
# 호출방식 1 ) positional argument : 함수를 호출할 때 전달하는 값들(argument)이 함수 정의에 선언된 파라미터 순서대로 전달되는 방식
pls, minus = test(1, 2)
# pls, minus = test(1) : TypeError 발생
pls, minus = test(2, 1)


# 호출방식 2 ) keyword argument : 함수를 호출할 때 argument 를 파라미터 = 값 형식으로 전달하는 방식
# 변수이름들이 이해하기 쉽게 길게 되어 있을 때, 어떤의미로 저장되는지 명시하기 위해 키워드 쓴다.
pls, minus = test(x=1, y=2)
pls, minus = test(y=1, x=2) # y와 x를 바꿔도 실행됨. 파라미터의 이름을 명시하면 keyword 대로 들어간다.
print(minus)


# 함수 정의
# default argument : 함수를 정의하는 시점에 파라미터의 기본값을 설정하는 것
# 문자열 + 문자열(이어붙이기) / 문자열 * 숫자(만큼 반복)
def show_msg(msg: str = 'hi', times: int = 1) -> None: # 파라미터(변수)에 값 저장 : times: int = 1
    print(msg*times)

show_msg('sleepy?', 5)
show_msg('yes.... ') # error 나지 않음.  why? 기본값이 있어서!
show_msg()


