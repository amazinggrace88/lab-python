'''
mymath1.py
'''
# 1. 함수 만들기
pi = 3.14 # test를 위한 변수 설정

def add(x:int, y:int) -> int:
    """
    두 정수가 주어졌을 때, x + y 를 리턴하는 함수

    :param x: 정수(int)
    :param y: 정수(int)
    :return: x+y
    """
    return x+y

def subtract(x:int, y:int) -> int:
    """
    두 정수가 주어졌을 때, x-y를 리턴하는 함수

    :param x: 정수(int)
    :param y: 정수(int)
    :return: x-y
    """
    return x-y

# 함수 test
if __name__ == '__main__':
    print(__name__)
    # mymath1에서는 __main__이라고 출력됨 / 다른파일(module3)에서는 다른 파일이 __main__이므로 utils.mymath1(자신의 파일 이름) 으로 출력됨
    # -> 어떤 파일에서 출력되는지에 따라 달라지는 변수
    print('pi = ', pi)
    print('add = ', add(1, 2))
    print('subtract =', subtract(1, 2))
    # 함수 출력 과정
    # 콘솔창에서 python.exe 라는 프로그램을 실행해서 C:/dev/lab_python/lab_python/utils/mymath1.py 전체를 실행시킨다.
    # 메모리에는 변수/add/subtract 라는 객체가 만들어져 있다.(생성했으므로)
# if 문을 써서 이 파일이 main 이면 함수를 동작시키고, 다른 파일에서 열 때 (main 이 아니면) 실행할 필요 없으므로 실행시키지 않는다.
