# 외울 것
import numpy as np

age = 28
name = 'grace'
print('age : {}, name : {}'.format(age, name))
# print(str(input()))

# 연산자 (operator) : 계산을 해주는 기능
# 연산자를 할당한다 : 변수 = 연산자
x = 1
y = 100
print(x is y)  # ? is 연산자 뭐지..?
print(float('3.1') + 1.2)  # float 으로 형태 변화를 주었다

# 문자열 타입
s = 'hello'
print(s[:-1])  # -1 인 o 빼고 리턴함

# list (원소와 인덱스로 나누어져 있음)
numbers = np.random.randint(1, 10, 5)  # np.ndarrray ! -> list 가 아니자나~
numbers_list = numbers.tolist()
print(numbers_list)
print(numbers_list[2:5])
numbers_list.extend([7, 8, 9])
print(numbers_list)

# list decomposition : 분해 *****
n1, n2, n3, n4, n5, n6, n7, n8 = numbers_list
print(n1, n2, n3)

# 2 차원 list
two_dimension_list = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]
print(two_dimension_list[1][2])
print(two_dimension_list[0][1])

# dict
person = {'name': 'ohsam', 'age': 16, 'height': 170.5}  # 중괄호 key:value - 1개의 데이터타입
print(person.keys())
print(person.values())
print(person.items())

# set
s1 = {1, 2, 2, 4, 5, 6}
print('s1 : \n', s1)
s1.add(100)
print('again s1 : \n', s1)
s1.remove(100)
print('again s1 : \n', s1)
