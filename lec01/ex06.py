"""
문자열 (str) 타입
"""
# 1. '''의 역할
s = """
hi python
"""  # 주석이 아니고 문자열
print(s)
# or
s = '''
hi python
'''  # 주석이 아니고 문자열

# 2. \n과의 비교
"""
hi python
"""  # 주석

s = """
    def my_function(x: int) -> int:
        return x + 1
"""
print(s)  # """다음 줄바꿈 인식, tab 공백 인식, 문자열 넣은 그대로 인식
s = """\
    def my_function(x: int) -> int:
        return x + 1
"""
print(s)  # \ backslash로 줄바꿈이 들어가지 않음.

# 줄바꿈 문자열 \n
s = '안녕하세요\npython'
print(s)
s = '\thello\n\tpython'
print(s)
# \t : tab \n : new line,줄바꿈


# 3. 문자열(sequence)의 인덱스, 자르기(slicing) 0 h 1 e 2 l 3 l 4 o / 5는 해당 깃발의 문자열 없음
s = 'hello'
print(s[0])  # index 0 부터 시작 : h의 앞,
print(s[1])
# print(s[5]) # IndexError: string index out of range

# slicing
print(s[0:2])  # 범위 연산자 ':'
print(s[1:5])
print(s[0:])  # 끝 인덱스 없는 경우 : 배열의 끝까지 *****
print(s[:3])  # 앞 인덱스 없는 경우 : 배열의 처음부터 *****
print(s[-3:-1])  # -5 h -4 e -3 l -2 l -1 o 0 / 뒤에서부터 0 깃발도 있음
# x:y  - from x(포함, include) to y (미포함, exclude)
