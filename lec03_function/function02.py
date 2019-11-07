'''
function making
함수 정의 / 선언(정의_define or 선언_declare) - 의미는 다르지만 혼용해서 많이 쓴다.

--구조--
def 함수이름(파라미터1 선언, 파라미터2 선언, .. ): *괄호() 반드시 있어야함
    함수의 기능 작성
    [return 값] - 값 반환한다는 뜻
-------
'''


# 함수 예제(함수의 정의는 윗줄과 2줄 떨어뜨리기)
def say_hello():                         # : 이후에 함수 기능 작성하기 위해 들여쓰기 한다.
    """                                  # "" :  함수 의 설명을 문서로 만들어주기
    'hi~ beautiful senorita!' 를 호출해준다.
    :return: None                        # :return : 리턴시 어떤 값을 보여줄건지 쓴다.
    """
    print('hi~ beautiful senorita!')


# 함수는 호출해야만 실행됨(호출하기 전에는 실행되지 않음)
say_hello()                            # process: 함수 호출해주면 함수 정의로 점프하고 :안의 문장 실행 후 호출된 곳으로 와서 실행됨


# another example
def print_msg(msg):
    """
    인수(argument) msg를 화면에 출력하는 함수
    :param msg: 출력할 메세지(str 타입)
    :return: None
    """
    print(msg)

# str라고 명시해도 숫자타입을 주어도 error나지 않는다.(python은 타입 검사를 하지 않기 때문) - 개발자가 결정할 문제이다.
print_msg('20191107')


# another example2
def add(x, y): #function header
    """
    숫자 2개를 전달받아 숫자들의 합을 리턴하는 함수

    :param x: int
    :param y: int
    :return: x + y를 리턴(int)
    """
    return x + y


result = add(3,5) #return값이 있는 함수인 경우
print(f'add 결과 = {result}')


# another example3 : return 값 2개 리턴하는 함수 - python 의 특징 : 여러개의 값을 한꺼번에 리턴하는 것이 가능하다.
def sum_and_product(x, y):
    """
    두 수 x와 y의 합(summation)과 곱(product)을 리턴하는 함수

    :param x: int
    :param y: int
    :return: x+y, x*y 순서로 리턴(int)
    """
    return x + y, x * y

# 원리 : sum, product = 1, 2 처럼 생각

# 각각 저장
sum, product = sum_and_product(3, 5)
print(f' sum = {sum}, product = {product}')
# 하나에 저장
result = sum_and_product(3, 5)
print(result) # 하나로 저장될 때는 tuple 로 저장됨 (하나의 리턴이지만 tuple 형태로 리턴한 것)
print(result, result[0], result[1]) # 각각은 인덱스로 꺼내면 된다. (for 문으로 반복하고 싶을 때)


# another example4 : dict 을 만들어 리턴
def make_person(name, age):
    """
    이름(name), 나이(age)를 전달받아서 dict 타입을 리턴하는 함수

    :param name: 이름(str)
    :param age: 나이(int)
    :return: {'name' : name, 'age' : age}
    """
    return {'name' : name, 'age' : age}

person = make_person('오쌤', 16)
print(person)