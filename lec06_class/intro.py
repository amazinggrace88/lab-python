'''
class 사용 예
'''
# 1) 객체 생성
s = 'hello'
# 객체 생성의 과정
# stack : python interpreter 가 관리
# s - 주소값 저장

# heap : 메모리 주소 + 객체 저장
# 'hello' - 생성된 객체


# 2) 객체 메소드 호출
# stack에서 heap을 참조할 수 있다.
# 클래스 안에 들어가 있는 변수 - 메소드
print(s.capitalize())
# method - m으로 도움말에 나타남
print(s.upper())
# 클래스를 사용하는 목적 : str라는 클래스 안 변수 선언 (데이터) + 기능(함수)를 합쳐 데이터 타입(객체)로 저장하여 바로 실행할 수 있음
print(type(s)) # <class 'str'>
print(s.find('l')) # 문자열 안에서 소문자 l을 찾아라



# 2) 비교

s2 = 'python' # python 이라는 객체의 주소를 저장한다.
print(type(s2))
print(s2.capitalize())
print(s2.upper())
print(s2.find('l')) # s2에서 l이라는 문자를 찾아라 : -1 음수리턴의미: 찾을 수 없음


# 정리
# str라는 class 타입은 똑같지만, s와 s2는 서로 다른 객체이다.
# ex_설계도는 같지만, 만들어진 물건은 다름
# data가 다르기 때문에 self가 달라져서 같은 함수를 주어도 결과는 달라진다.
