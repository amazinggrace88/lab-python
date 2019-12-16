"""
dictionary comprehension
"""

numbers = [1, 2, 3, 4, 5]
names = ['a', 'b', 'c', 'd', 'e']  # list 두개의 크기가 같아야함!

# for loop 로 dictionary 만들기
superman = {}  # empty dict
for i in range(len(numbers)):
    superman[numbers[i]] = names[i]  # 존재하는 키값은 value 바꿈, 존재하지 않는 키값은 value 생성
print(superman)
# or
# dictionary comprehension {key:value for loop}
superman2 = {numbers[i]: names[i]
             for i in range(len(numbers))}
print(superman2)

# zip : list 2 개를 묶어 하나로 만드는 역할
num_name = zip(numbers, names)
print(num_name)
for x in num_name:
    print(x)  # zip 을 반복문 안에 넣어주면 tuple 들을 넣어준다.
# or
for x in zip(numbers, names):
    print(x)  # zip은 for 문 안에서만 사용이 된다.

# zip 을 이용한 dictionary comprehension
superman3 = {}
for key, value in zip(numbers, names):
    superman3[key] = value
print(superman3)
# or
superman4 = {k: v
             for k, v in
             zip(numbers, names)}  # list 2개를 zip 으로 묶어서 tuple이 되고, tuple을 분해하여 for 문으로 각각 쌍을 dictionary 에 저장함.
print(superman4)

# if 문을 사용한 zip/dict comprehension
superman5 = {k: v
             for k, v in zip(numbers, names)
             if k % 2}  # k % 2 == 1(true 이므로 생략해도 됨) 홀수만 사용
print(superman5)
