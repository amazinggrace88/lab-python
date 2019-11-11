'''
raise
사용자 정의 오류를 발생시키는 방법
error 를 고의로 발생시킬 경우 : raise 사용
'''

age = int(input('나이를 입력>>'))
print(f'입력한 나이는 {age}')
# ValueError: invalid literal for int() with base 10: '12.3' 발생 가능
# 해결방법
try:
    age = int(input('나이를 입력>>'))
    print(f'입력한 나이는 {age}')
except ValueError:
    print('나이를 잘못 입력하셨습니다')
# 나이를 입력>>-212
# 입력한 나이는 -212
# Process finished with exit code 0 -> 음수가 발생하면 막을 수 없음
# 해결방법 : raise
try:
    age = int(input('나이를 입력>>')) # error 발생시 except문으로 바로 이동
    if age < 0:             # 조건 만족한다면 에러 발생시킴
        raise ValueError('나이는 0 또는 양의 정수여야 합니다')  # 밑에 있는 print() 실행될 수 없게 함
    print(f'입력한 나이는 {age}')
except ValueError as e:
    print(e.args)

