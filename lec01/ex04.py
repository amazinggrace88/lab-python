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

x = 1  # 연산자 공식 : 변수(왼쪽) = 값(오른쪽)
# 1 = x no!
print(2 ** 3)
print(3 / 2)
print(10 // 3)
print(10 % 3)

x = 1
print('x =', x)
x += 10  # x = x + 10
print('x =', x)

print(1 == 2)
print(1 != 2)

x = 50
print(0 < x < 100)  # alt+enter : 마법키 (맥 option+enter) : 최적화해서 코드를 바꿔준다. 밑줄 : 경고의 의미 (더 최적화될 수 있다)
print(x < 0 or x > 10)  # 한쪽 조건만 true 면 true

# is 연산자 : 나중에..
y = 100
print(x is y)
