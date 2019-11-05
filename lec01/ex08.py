"""
tuple : 원소들의 값들을 변경할 수 없는 리스트
(why?
"""

numbers = [1, 2, 3]  # 소괄호 사용
print(numbers)
print(numbers[0])
print(numbers[0:2])
one, two, three = numbers
print(one, two, three)
print(one)

numbers[0] = 100  # TypeError: 'tuple' object does not support item assignment : 아이템을 할당하는 것이 안된다.
