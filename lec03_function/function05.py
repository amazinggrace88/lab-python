'''
가변길이 인수(variable length argument)
함수를 호출할 때 번달하는 argument 의 갯수가 다양하게 변하는 것
*이 앞에 있는 인수들이 해당된다.
'''


# def test2(x = 1, y): #error : default argument(기본값)들이 있는 default argument 를 갖지 않는(파라미터는 기본값이 없는) 파라미터보다 뒤쪽에 있어야 함.
#     return x +y      # why? positional argument 때문에
# 첫번째 argument의 기본값을 주었으면, 그 뒤의 argument 의 기본값들도 모두 주어야 한다.
# 가변 길이 인수 (함수를 호출할 때 전달하는  argument 의 가변길이가 변할 수 있을 때
print("a")
print('a', 'b', sep = ':') #변수 선언 *표, 몇개가 와도 상관없다.
# print() : ctrl + q 로 문자를 보면, *value 이 있다.


# example 1
def fn_vararg(varargs):
    print(varargs)
# fn_vararg(1, 2) : argument를 2개 주었음. tuple 처리되어 출력


# example 2
def fn_vararg(*varargs):
    print(varargs)
    for arg in varargs:
        print(arg) #하나씩 출력하도록: for문 만든다. for문을 만들어도 여러개의 변수는 tuple처리 되어 하나씩 꺼내서 함수 만들 수 있다.
fn_vararg(1, 2, 4) #argument를 몇개를 주어도 상관이 없음.

# *varags 의 위치 비교

def fn_vararg(*varargs):
    print(*varargs) #print(1, 2, 4)와 같음, 공백으로 처리됨(*의 역할 : 묶여 있는 값을 풀어주어서 하나씩 꺼내는 것!)
    for arg in varargs:
        print(arg) #하나씩 출력하도록: for문 만든다. for문을 만들어도 여러개의 변수는 tuple처리 되어 하나씩 꺼내서 함수 만들 수 있다.
fn_vararg(1, 2, 4) #argument를 몇개를 주어도 상관이 없음.


# example 3
def summation(*args):
    """
    임의의 갯수의 숫자들을 전달받아 그 숫자들의 총합을 리턴하는 함수

    :param args: 합계를 계산할 숫자들(갯수 제한 없음)
    :return: 숫자들의 합
    """
    sum = 0
    for arg in args:
        sum += arg
    return sum

result = summation(1,2,3,4,5,6,7,8,9,10)
print(result)
print(summation()) # 0 실행됨.


# example 4
def fn_vararg2(a, *b):
    print(f'a = {a}')
    print(f'b = {b}')

# fn_vararg2() # positional argument: 'a'가 빠져있음. 기본값이 없으므로 반드시 값 주어야 함.
fn_vararg2(1) # b는 가변길이 parameter이므로 인수를 저장하지 않아도됨. 원소의 갯수가 하나도 없는 tuple이 된다.


# example 5
def fn_varargs3(*a, b):
    print(f'a = {a}')
    print(f'b = {b}')

# fn_varargs3() #TypeError: a의 값은 주지 않아도 되지만, b의 값을 주어야 하기 때문에 오류이다. keyword-only argument: 'b'
# keyword-only argument: 'b'의 의미 : keyword 방식으로만 b를 줄 수 있다 why? a가 가변길이 변수이므로!
# fn_varargs3(1) #TypeError: b를 표시하지 않아서..
# fn_varargs3(1, 2) #TypeError: b를 표시하지 않아서..
fn_varargs3(1, b=2) #b= 로 명시한다. : 가변길이 파라미터 뒤에 선언된 파라미터에 값을 전달할 때는 keyword-only argument 방식으로만 값을 전달 가능하다.


# example 6
def calculator(*values, operator):
    """
    operator가 '+'인 경우에는 values들의 합계를 리턴하고,
    operator가 '*'인 경우에는 values들의 곱을 리턴하는 함수

    :param values:
    :param operator:
    :return:
    """
    if operator == '+':
        result = 0
        for x in values:
            result += x  # result = result + x
        return result
    elif operator == '*':
        result = 1
        for x in values:
            result *= x  # result = result * x
        return result

result = calculator(1, 2, 3, 4, 5, operator = '+')
result2 = calculator(1, 2, 3, 4, 5, operator = '*')
result3 = calculator(1, 2, 3, 4, 5, operator = '-') # why none 일까?
print(result, result2, result3)


# example 7
def calculator2(*values, operator):
    """
    operator가 '+'인 경우에는 values들의 합계를 리턴하고,
    operator가 '*'인 경우에는 values들의 곱을 리턴하는 함수
    operator가 '+', '*'가 아닌 경우에는 None을 리턴.

    :param values:
    :param operator:
    :return:
    """
    result = None #해결방법
    if operator == '+':
        result = 0
        for x in values:
            result += x  # result = result + x
        # return result
    elif operator == '*':
        result = 1
        for x in values:
            result *= x  # result = result * x
        # return result

    return result

result = calculator2(1, 2, 3, 4, 5, operator = '-')
print(result)
# UnboundLocalError: local variable 'result' referenced before assignment
# 변수 x가 값을 찾아가는 것을 reference 라고 한다. (heap 에 있는 메모리를 찾아간다)
# result 라는 값이 if문 안에서 할당되었음.(개념이 생겨남). operator = '-'일때에는 변수 자체가 없는 상태이므로 (result 에 값이 없음) 리턴되지 않는다.


