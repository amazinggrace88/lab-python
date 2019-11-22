'''
Review for lec01
'''

# ex01
# ctrl+shift+f10 파이썬 코드 실행 : 파이썬 인터프리터가 컴파일함.

"""
블록주석
"""

# 변수 사용 : 프로그램에 필요한 데이터를 저장하는 공간
# python : 변수 이름 = 값('<-'안됨)
age = 16
name = 'ohsam'
company = 'itwill'
# print(age, name, company)

# 문자열 : '' & "" 모두 사용 ('' many)
str1 = 'he said "yes!"'
str8 = "he said 'yes!'"
# print(str1, str8)

# \' : 같은 따옴표 안에서 문자열 안에 포함되어 있는 따옴표 만들기
str1_re = "he said \"yes!\""
# print(str1_re)



# ex02
"""
print() 방법들
"""

age = 16
name = '오쌤'
# age :  16 name :  오쌤 # 쉼표와 쉼표 사이 하나의 공백 **
print('age : ', age, 'name : ', name)
# age : 16, name : 오쌤 #formatted string : 중괄호 {변수이름} **
print(f'age : {age}, name : {name}')
# 나이 : 16, 이름 : 오쌤 {},{} / format(변수1, 변수2) **
print('나이 : {}, 이름 : {}'.format(age, name))
# 나이 : 16, 이름 : 오쌤 # 1번째 %자리에 1번째 변수, 2번째 %자리에 2번째 변수
print('나이 : %d, 이름 : %s' %(age, name))
# %d : 정수, %f : 실수, %s : 문자열 - c programming 언어 중 %변수(검색해볼 것, 더 있음)


"""
사용자 입력(키보드입력) 처리
"""
# 사용자가 입력할 수 있도록 함 : input()
# print('put your names please')
# name = input()
# print(f'name = {name}')
#
# # print문을 input 안에 넣어도 된다. 줄바꿈 안됨 / 키보드로 입력한 것들은 무조건 문자열
# a = input('>>>put your name ')
# print(f'name = {a}')
# print(age + 1) #문자열이므로 사칙연산 불가능
# ctrl + / : 주석 토글 (주석 단축키)
# mac: command + / : 주석 토글 (주석 단축키)



# ex03
"""
python datatype
변수가 어떤 타입을 저장하는가?

1. 숫자타입 : int(정수) - 4byte 사용함, float(실수) = 8 byte 사용함, complex(복소수) - complex는 파이썬의 특징! 실수와 허수의 합
2. 논리타입 : bool
3. 문자열 : str
4. 시퀀스(sequence) : list, tuples
5. 매핑(mapping) : dict
6. 집합 : set
7. none : 값이 없음을 나타내는 데이터 타입 (값을 저장하지 않는다는 의미 - stack에 주소값이 없다.(0000) : null값과 같다.
"""
# python datatype : int/bool/str/list/tuple/dict/set/none

intval = 123
print('intval\'s type : ',type(intval))
print('intval\'s id : ', id(intval))
complexval = 2 + 1j
print('complexval\'s type : ', type(complexval))
print('complexval\'s id : ', id(complexval))
strval = 'grace'
print('str\'s type : ', type(strval))
print('str\'s id : ', id(strval))
boolean = 10 > 2
print('bool\'s type : ', type(boolean))
print('bool\'s id : ', id(boolean))
no = None  # None은 대소문자를 구분한다.
print('none\'s type : ', type(no))  # class NoneType
print('none\'s id : ', id(no))



# ex04
"""
연산자(operator)
: 계산을 해주는 기능
- 할당(assignment) : =
- 산술연산(numerical operator) : +,-,*,**(거듭제곱),/(소수점까지 나누기),//(몫만 반환),%(나머지)
- 복합 할당 연산 : +=, -=, *=, /=, .. 나머지 산술연산 모두 가능
- 비교연산 : >, >=, <, <=, ==(왼쪽과 오른쪽이 같은가, sql은 =, r ==), != / TRUE / FALSE로 결과 나옴
- 논리연산(logical operator) : and, or, not
- identity 확인 : is, is not (id()함수의 리턴값이 같은지,다른지 확인 : 즉, 참조하는 객체가 같은지 다른지 확인)
"""



# ex05
"""
명시적 데이터 타입 변환(casting)(명시적 형 변환) : int(), float(), str()
"""
# int()
x = input('>>> 숫자(x)을 입력하세요.: ')
y = input('>>> 숫자(y)을 입력하세요.: ')
print(int(x) + int(y))  # 문자열을 실수로 변환하였음.
# float()
print(float('3.1') + float('4.1'))
# str() ------------------> str() 문제가 안됨. why? 위에 변수가 str로 설정되어 있었음. 조심하쟈~
a = str(2)
print(a + '점')



# ex06
"""
문자열 (str) 타입
"""
# \n과 \t : n - new line, t - tab
print('hello \n ariana grande \tyou are beautiful girl')
ariana = 'hello \n ariana grande \tyou are beautiful girl'
print(ariana[0:5])



# ex07
"""
list : 여러개의 값들을 하나의 변수에 저장하기 위한 데이터 타입
원소(element) : list 에 저장된 값
인덱스(index) : list 에 값이 저장된 위치(번호)
숫자, 문자, 리스트,, 등 서로 다른 유형 저장 가능
elements 를 변경 (추가.삭제) - mutable(ok)
"""
