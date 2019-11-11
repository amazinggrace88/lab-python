'''
람다 표현식(lambda expression)
함수의 이름 없이, 함수의 매개변수 선언과 리턴 값으로만 표현하는 방법
lambda 표기법 : f:x -> ax + b ( = f(x) = ax + b )
(이름이 없는 함수라고도 이야기하기도 함)

---구조---
lambda [parameter1, parameter2..]: 식(expression)
---------
https://dojang.io/mod/page/view.php?id=2359 참고
'''


# 실습 1 함수 만들기
multiplication = lambda x, y: x * y # (이름이 없는 함수라고도 이야기하기도 함) -> 이름을 주기 위해 변수에 저장함
r = multiplication(11, 11)
print(r)

devision = lambda x, y: x / y
r = devision(1, 2)
print(r)


# 실습 2 람다 표현식 용도 -> 함수의 매개변수로 주기 위함 / 함수의 매개변수에 함수를 전달할 때 많이 사용함
def calc(x, y, op):
    return op(x, y)

r = calc(1, 2, lambda x, y: x + y) # lambda 표현식으로 함수를 그 자리에서 바로 만들어 매개변수로 주었다.
print(r) # 1, 2가 x, y에 대입됨

r = calc(1, 2, lambda x, y: x / y)
print(r)


# 실습 3 응용 : 리스트를 받아 새로운 리스트를 만드는 함수를 만들 때 (why? 반복하지 않는 함수들인 일회용 함수들을 만들어 filtering 하기 위함)
def my_filter(values, func):
    """
    values 라고 하는 리스트의 원소들 중 필터링 조건을 만족하는 원소들만으로 이루어진 새로운 리스트를 생성하여 리턴
    
    :param values: 리스트
    :param func: 함수(True/False를 리턴하는 함수)
    :return: 필터링된 새로운 리스트
    """
    result = []
    for item in values: #리스트에서 원소를 하나씩 뺀다.
        if func(item): # 필터링 조건 함수 func의 리턴값을 검사
            result.append(item) # 조건이 참일 때만 item의 원소를 새로운 리스트 result 에 추가
    return result # 새로운 리스트 출력

numbers = [1, -2, 3, -4, -5, 6, -7, 8]
positives = my_filter(numbers, lambda x: x >0) # parameter 1개, x>0이면 true/false인 bool함수
print(positives)

evens = my_filter(numbers, lambda x: x % 2 == 0) # 2로 나눈 나머지
print(evens)

# 문자열의 리스트도 상관없음(숫자/문자 리스트 상관없다)
lang = ['python', 'r', 'pl/sql', 'java', 'c/c++']
more_than_5 = my_filter(lang, lambda x: len(x) > 5)
print(more_than_5)


# 실습 4 : list comprehension 을 이용하여 실습 3의 my_filter 함수 만들어 list를 가지고 dictionary를 리턴하기
def my_filter2(values, func):
    return [x for x in values if func(x)] #if func(x) : if func(x)가 true 라면

print(my_filter2(numbers, lambda x: x>0)) #positive와 똑같은 함수


# 실습 5
def my_mapper(values, func):
    """
    리스트의 아이템들을 함수의 파라미터에 전달해서, 리스트의 아이템을 key, 함수의 리턴값을 value로 하는 dictionary를 리턴

    :param values: 리스트
    :param func: 파라미터가 1개인 함수
    :return: dict
    """
    result = {} # 비어있는 dict를 만든다.
    for item in values: #values에 있는 모든 item을 하나씩 꺼낸다(반복)
        result[item] = func(item) # 함수가 리턴해주는 값을 result의 value로, item은 result의 key로 만든다
    return result


result = my_mapper(lang, lambda x: len(x)) # lambda x: len(x) : x의 문자 길이를 value로 return한다
print(result)


def my_mapper2(values, func):
    return{k: func(k) for k in values} # lambda 식을 이용함

result = my_mapper2(lang, lambda x: len(x)) # 같은 값을 준다.
print(result)
