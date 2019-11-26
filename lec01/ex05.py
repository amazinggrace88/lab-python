"""
명시적 데이터 타입 변환(casting)(명시적 형 변환) : int(), float(), str()
"""

# "3.1" + 1.2 error: string과 integer를 더할 수 없다.
print(float('3.1') + 1.2)  # '3.1' 문자(string)타입을 숫자타입float으로 변환하고 산술연산 실행

# 문자열 + 문자열 : concatenate (문자열 이어붙이기)
print('3.1' + str(1.2))

# 실습 : 계산기 만들기
x = input('>>> 숫자(x)을 입력하세요.: ')
y = input('>>> 숫자(y)을 입력하세요.: ')
print(int(x) + int(y))  # 문자열 -> 실수 변환
# or
x = input('>>> 숫자(x)을 입력하세요.: ')
y = input('>>> 숫자(y)을 입력하세요.: ')
x = float(x)
y = float(y)
print(x + y)
# 파일에서도 마찬가지 : 파일에 저장된 숫자 = 문자열
# or
# x = input('>>> 숫자(x)을 입력하세요.: ')
# y = input('>>> 숫자(y)을 입력하세요.: ')
x = float(input('>>> 숫자(x)을 입력하세요.: '))
y = float(input('>>> 숫자(y)을 입력하세요.: '))
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x + y}')
print(f'{x} * {y} = {x + y}')
print(f'{x} / {y} = {x + y}')
# ctrl + d : 커서가 있는 줄을 복사

