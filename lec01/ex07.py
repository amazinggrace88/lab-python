"""
list : 여러개의 값들을 하나의 변수에 저장하기 위한 데이터 타입
원소(element) : list 에 저장된 값
인덱스(index) : list 에 값이 저장된 위치(번호)
숫자, 문자, 리스트,, 등 서로 다른 유형 저장 가능
elements 를 변경 (추가.삭제) - mutable(ok)
"""

numbers = [1, 2, 3, 4, 5] # list : 대괄호로 구분
print(numbers)
print(numbers[0])
# print(numbers[5]) indexerror
print(numbers[1:3])

# 배열의 원소(배열에 저장된 값) 변경
numbers[0] = 100
print(numbers)

# 배열에 원소 추가
numbers.append(6) # 제일 마지막 추가..
print(numbers)
# numbers.append(7, 7) 여러개 추가 불가
numbers.extend([7, 8, 9]) #extend : 확장됨, []이라는 새로운 list를 각각 append해준다.
print(numbers)

# append vs extend
numbers.append([7, 8, 9])
print(numbers) # [100, 2, 3, 4, 5, 6, 7, 8, 9, [7, 8, 9]]라는 list 자체가 1개의 원소로 취급된다. (2차원 list)

# 원소 삭제
numbers.remove(100) # 원소의 값으로 삭제 (list 안에 어떤 원소가 있는지 알아야함)
print(numbers)
del numbers[1] # 원소의 인덱스로 삭제(인덱스만 알면 삭제 할 수 있음) / 함수가 아니어서 () 쓰지 않는다.
print(numbers)

# 비어있는 배열 만들기(원소가 아무것도 없는 list)
empty = []
print(empty)

# 여러가지 타입의 값 함께 저장하기
person = ['ohsam', '16', '170.5', True]
print(person[0], type(person[0]))
print(person[2], type(person[2]))

# list decomposition : 분해
name, age, height, marriage = person #person을 변수 4개에 저장하겠다.
print(name, age, height, marriage)
print(marriage) # 변수를 이해하기 쉽게 하기 위해서, 이름을 붙여주면 편리해진다.

# 2차원 list
matrix = [
    [1, 2, 3], #index 0번 원소
    [4, 5, 6], #index 1번 원소
    [7, 8, 9]  #index 2번 원소
]
print(matrix) #크기가 3 = 원소의 갯수가 3개
print(matrix[0], type(matrix[0]))
print(matrix[0][0], type(matrix[0][0]))
print(matrix[0][2], type(matrix[0][2]))

# 2차원 list sclicing
print(matrix[0:2])
print(matrix[0][0:2], matrix[1][0:2])
