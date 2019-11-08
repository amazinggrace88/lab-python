'''
sorting algorithm

# 선택정렬 알고리즘
# 1. 리스트 안에 최소값을 찾아 리스트2를 만든다.
# 2. 원래 리스트에서 최소값을 뺀다.
# 3. 리스트 안에 최소값을 찾아 리스트2에 추가한다.
# 4. 원래 리스트에서 최소값을 뺀다.
'''
import numpy as np


def find_min(numbers):
    """
    주어진 리스트에서 최솟값과 최솟값의 인덱스를 찾아서 리턴하는 함수

    :param numbers: 숫자들의 리스트
    :return: (최솟값의 인덱스, 최솟값)의 쌍(tuple)
    """
    min_id, min_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v < min_value:
            min_id, min_value = i, v
    return min_id, min_value

def find_max(numbers: list) -> tuple:
    """
    주어진 리스트에서 최댓값과 최댓값의 인덱스를 찾아서 리턴하는 함수

    :param numbers: 숫자들의 리스트
    :return: (최댓값의 인덱스, 최댓값)의 쌍(tuple)
    """
    max_id, max_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v > max_value:
            max_id, max_value = i, v
    return max_id, max_value

# 선택 정렬 알고리즘
def sel_sort(numbers: list, reverse: bool = False) -> list:
    """
    최솟값을 선택하여 다른 리스트에 넣어줌으로써 정렬하는 알고리즘 함수 (오름차순 정렬) #내림차순 정렬은 최댓값을 선택
    주어진 리스트(파라미터에 전달된 리스트)의 순서는 바뀌지 않음

    :param numbers:
    :param reverse: False 인 경우는 오름차순, True 인 경우는 내림차순, 기본값은 False
    :return:
    """
    numbers_copy = numbers.copy()
    result = [] # empty list 생성 (최솟값을 append 하기 위함)
    while numbers_copy: # numbers 의 원소가 있는 동안에 - while 문의 뜻 ([]. {}. 0. ''. "" => false)
        print('numbers =', numbers_copy)
        print('result =', result)
        if reverse == False :
            _, found = find_min(numbers_copy) # _, : 필요없지만 변수는 있어야 하기 때문에 # 최솟값을 찾음
        else:
            _, found = find_max(numbers_copy)
        result.append(found)
        numbers_copy.remove(found)

    return result

numbers =[np.random.randint(0, 100) for _ in range(10)]
ascending_numbers = sel_sort(numbers)
descending_numbers = sel_sort(numbers, reverse= True)
print('ascending = ', ascending_numbers)
print('descending = ', descending_numbers)


# 선택 정렬 알고리즘 2
def sel_sort2(numbers: list, reverse:bool = False) -> None:
    """
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고, 원본 리스트의 순서 자체를 바꿈 (리턴값 None)

    :param numbers:
    :return:
    """
    length = len(numbers) # 길이를 알아야 함
    for i in range(0, length - 1): # 마지막 바로 전까지만 비교하는 대상(주체, 처음은 index 0)를 정한다.
        for j in range(i + 1, length):  # 최소값을 찾는 대상(i) 이외의 비교 당하는 대상(처음은 index 1 = 0 + 1)를 정한다.
            if reverse:
                if numbers[i] < numbers[j]: # i번째 원소와 j번째 원소를 비교하여 j 가 더 크다면,
                    numbers[i], numbers[j] = numbers[j], numbers[i] # 서로의 원소를 바꿔준다. swap
            else: # 오름차순 정렬, 최솟값
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            print(numbers)


print('---------------------------------------')
numbers =[np.random.randint(0, 100) for _ in range(10)]
print(numbers)
sel_sort2('ascending = ', numbers)
print('---------------------------------------')
numbers =[np.random.randint(0, 100) for _ in range(10)]
print(numbers)
sel_sort2('descending = ', numbers, reverse=True)