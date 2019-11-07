'''
함수 정의:
def 함수이름(파라미터 선언):
    함수 기능(body)
-------- python 2.0&3.0 공통

함수 정의:
def 함수이름(파라미터: 타입, 파라미터:타입, ..) -> 리턴타입:
    함수 기능(body)
-------- python in 3.0~ 반드시 지켜야 하는 것은 아니고, 개발자들 편의를 위해 만들었다
# python 은 함수를 호출할 때 함수 파라미터 타입과 리턴타입을 검사하지 않음(& .. python 3.0에서 여전히 검사하지 않기 때문)
*cf. ctrl 키를 누른 상태로 커서를 클릭하면 클릭한 곳으로 간다.
'''


# example1
def subtract(x:int, y:int) -> int:
    return x - y


result = subtract(1, 2) #ctrl+q를 통해 문서를 봐도 없을때, 힌트를 주는 용도로 활용할 수 있다.
print(result)
result = subtract(1.1, 2.2)
print(result) # int 아닌 것을 넣어도 실행 잘 됨..


# example 2
def my_sum(numbers:list) -> float:
    """
    숫자들(int/float..)이 저장된 리스트를 전달받아 모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 합
    """
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        i += 1
    return sum
# or
def my_sum2(numbers:list) -> float:
    """
    숫자들(int/float..)이 저장된 리스트를 전달받아 모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 합
    """
    sum = 0
    for i in numbers:
        sum += i
    return sum


result = my_sum([1,2,3,4,5,6,7,8,9,10])
result2 = my_sum2([1,2,3,4,5,6,7,8,9,10])
print(result)
print(result2)


# example 3
def my_mean(numbers:list) -> float:
    """
    숫자들이 저장된 리스트를 전달받아 모든 원소들의 평균을 리턴하는 함수
    >>> my_mean([1,2,3,4,5])
    3

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 평균
    """
    sum = 0
    for i in numbers:
        sum += i
    mean = sum / len(numbers)
    return mean
# or
def my_mean2(numbers:list) -> float:
    """
    숫자들이 저장된 리스트를 전달받아 모든 원소들의 평균을 리턴하는 함수
    >>> my_mean([1,2,3,4,5])
    3

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 평균
    """
    return my_sum(numbers) / len(numbers)
# 함수 만들었으면, 언제든지 필요한 곳에서 사용할 것! 함수의 목적은 재사용.


result = my_mean([1,2,3,4,5,6,7,8,9,10])
print(result)

