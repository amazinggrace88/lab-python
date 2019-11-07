'''
함수 (function) : 기능을 수행한 후, 값을 반환(return)하는 코드 블록
인수 (argument) : 함수를 호출할 때 전달하는 값 (문자열, 숫자, 리스트 .. )
매개변수 (parameter) : argument 를 저장하기 위해서, 함수를 정의할 때 선언하는 변수 (값이 저장되는 곳 ex end = )
--구조--
함수 호출
argument 전달
함수(parameter = '인수_argument')
결과를 return
-------
cf. ctrl+q(맥 ctrl+j) : 함수/클래스의 document 보기 - 문서 보는 연습
'''


# 함수 호출(call, invoke)
print('hello, python!') # argument 1개
print() # argument 없음
print('hello', 'python', 2) # argument 3개 - 쉼표로 구분된다.
print('hello', end= ',') # argument 1개, parameter 1개
print('python')


# 함수의 값은 저장되지 않는다.
result = print('hello')
print(result) # print()가 값을 반환하지 않는 함수이기 때문. 모든 함수가 값을 반환하지는 않는다. (= none을 return한다.)


# Python 내장(built-in) 함수
result = sum([1, 2, 3]) # result : 함수 sum(summation) 의 리턴값(반환값)
print(result)
result = pow(2, 4, 3)
print(result)