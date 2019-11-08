# 1부터 n까지의 숫자들의 합을 리턴하는 함수
# 1 + 2 + 3 + ... + n
def sum_to_n(n: int) -> float:
    return n * (n + 1) / 2

result = sum_to_n(9)
print(result)

def sum_to_n2(n: int) -> int:
    _sum = 0
    for x in range(1, n + 1):
        _sum += x
    return _sum

result = sum_to_n2(9)
print(result)

def sum_to_n3(n: int) -> int:
    numbers = [x for x in range(1, n + 1)]
    print(numbers)
    return sum(numbers)

result = sum_to_n3(9)
print(result)

# 1부터 n까지 숫자들의 제곱의 합을 리턴하는 함수
# 1**2 + 2**2 + 3**2 + ... + n**2
def sum_to_squares(n: int) -> float:
    return n * (n + 1) * (2 * n + 1) / 6

def sum_to_squares2(n: int) -> int:
    _sum = 0
    for x in range(1, n + 1):
        _sum += x ** 2
    return _sum

print(sum_to_squares(3))
print(sum_to_squares2(3))

# 숫자들의 리스트를 전달받아서 최댓값을 찾아서 리턴하는 함수
def find_max(values: list) -> float:
    # return max(values)
    _max = values[0]
    # for x in values:
    #     if x > _max:
    #         _max = x
    for i in range(1, len(values)):
        if values[i] > _max:
            _max = values[i]
    return _max

numbers = [1, 2, 100, 99, 1000, 0]
print(find_max(numbers))

def find_max2(values: list) -> float:
    # sorted(list): list를 정렬한 새로운 리스트 리턴
    # 원본 리스트(list)는 순서가 그대로 유지됨
    # list.sort(): 원본 리스트를 정렬해서 순서를 바꿈.
    # None을 리턴함(값을 리턴하지 않음)
    sorted_values = sorted(values, reverse=True)
    print('values:', values)
    print('sorted_values:', sorted_values)
    # return sorted_values[0]
    values.sort(reverse=True)
    print('values:', values)
    return values[0]

print(find_max2(numbers))

# 숫자들의 리스트를 전달받아서 최댓값의 인덱스를 리턴하는 함수
def find_max_index(values: list) -> float:
    max_id, max_val = 0, values[0]
    for i, v in enumerate(values):
        print(f'i = {i}, v = {v}')
        if v > max_val:
            max_id, max_val = i, v
    return max_id


# 숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수
