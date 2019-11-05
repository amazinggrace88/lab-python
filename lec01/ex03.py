"""
python datatype
변수가 어떤 타입을 저장하는가?

1. 숫자타입 : int(정수) - 4byte 사용함, float(실수) = 8 byte 사용함, complex(복소수) - complex는 파이썬의 특징! 실수와 허수의 합
2. 논리타입 : bool
3. 문자열 : str
4. 시퀀스(sequence) : list, tuple
5. 매핑(mapping) : dict
6. 집합 : set
7. none : 값이 없음을 나타내는 데이터 타입 (값을 저장하지 않는다는 의미 - stack에 주소값이 없다.(0000) : null값과 같다.
"""

# 숫자타입
intVal = 123
print(type(intVal))
# 메모리에 데이터타입에 따라 저장 크기를 정하여 준다. ex_메모리 주소값(우편함, intVal) - stack에 저장 / 메모리(편지, 123) - heap에 저장 in python
print(id(intVal)) # id(주소) : 140709657149520

floatVal = 3.141592
print(type(floatVal))

complexVal = 1 + 2j # 허수 i 대신 j 사용 : i를 변수 이름으로 많이 써서
print(type(complexVal))
print(1j**2) # 허수^2 = -1


# 2. 논리타입 : bool()
result = 10 > 2 # 오른쪽에 있는 식이 계산되어서 저장 (TRUE), 변수 이름은 항상 왼쪽에! 등호는 연산 우선순위에서 맨 마지막..
print(result)
print(type(result))


# 3. 문자열 : str()
name = 'abc'
print(type(name))


# 4.5.6 나중에 자세히!


# 7. none
name = None
print(type(name))

