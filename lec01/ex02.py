"""
print() 방법들
"""

print('hello, python!')

age = 16
print('age : ', age)  # 문자열과 숫자 사이에는 하나의 공백이 들어간다.
name = '오쌤'
print('age : ', age, 'name : ', name)  # age :  16 name :  오쌤 # 쉼표와 쉼표 사이 하나의 공백 **
print(f'age : {age}, name : {name}')  # age : 16, name : 오쌤 #formatted string : 중괄호 {변수이름} **
print('나이 : {}, 이름 : {}'.format(age, name))  # 나이 : 16, 이름 : 오쌤 {},{} / format(변수1, 변수2) **
print('나이 : %d, 이름 : %s' % (age, name))  # 나이 : 16, 이름 : 오쌤 # 1번째 %자리에 1번째 변수, 2번째 %자리에 2번째 변수
# %d : 정수, %f : 실수, %s : 문자열 - c programming 언어 중 %변수(검색해볼 것, 더 있음)

print('나이 : {}, 이름 : {}'.format(age, name))

"""
사용자 입력(키보드입력) 처리
"""
# 사용자가 입력할 수 있도록 함 : input()
print('>>> put your name please:')
name = input()
print(f'name: {name}')

# print문을 input 안에 넣어도 된다. 줄바꿈 안됨 / 키보드로 입력한 것들은 무조건 문자열
age = input('>>> put your age :')
print(f'age: {age}')
# print(age + 1) #문자열이므로 사칙연산 불가능
#ctrl + / : 주석 토글 (주석 단축키)


