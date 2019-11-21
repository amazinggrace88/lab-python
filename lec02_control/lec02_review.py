'''
lec02 - review
for 변수 in iterable:
    iterable statements
'''
import numpy as np
from math import sqrt


# for01
for i in range(20):
    print(i, end=' ')
print()  # 줄바꿈

# list is iterable for 'for 문' (set/tuple 사용도 동일함)
data_list = ['a', 'r', 'i', 'a', 'n', 'a']
for i in data_list:
    print(i)
print()

for i in range(len(data_list)):
    print(i, data_list[i])  # data_list[i]를 주는 것을 잊지 말것!
print()

# dictionary for statements
data_dict = {1:'a', 2:'r', 3:'i'}
print(data_dict.keys())  # key 의 list 가 나온다.
print(data_dict.values())  # value 의 list 가 나온다.
for key in data_dict.keys():
    print('data_dict\'s key  = ', key)
print()
for value in data_dict.values():
    print('data_dict\'s value = ', value)
print()
for item in data_dict.items():
    print('data_dict\'s key & value together = ', item)
print()
# 최종 = dict decomposition
for key, value in data_dict.items():
    print('data_dict\'s key, value separately = ', key, value)
print()



# for02
