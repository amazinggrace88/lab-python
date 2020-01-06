"""
python if 구문(statement)
if 조건식:
   조건식이 참일 때 실행할 문장

if 조건식:
   조건식이 참일 때 실행할 문장
else:
   조건식이 거짓일 때 실행할 문장
**들여쓰기 중요**
"""

# if
# ex 숫자를 입력받아서 양수인 경우에만 출력
num = int(input(">>>정수를 입력하세요 : "))
if num > 0:
    print(f'num = {num}')

print("프로그램 종료")
# number < 0이면 들여쓰기 된 부분을 전부 건너뛴다. (if 조건에 맞지 않기 때문)
num = int(input(">>>정수를 입력하세요 : "))
if num > 0:
    print(f'num = {num}')

    print("프로그램 종료")
# 들여쓰기 된 부분은 if 문에 종속된다.

# if-else
num = int(input(">>>정수를 입력하세요 : "))
if num > 0:
    print("양수")
else:
    print("0 또는 음수")
print("프로그램 종료")

# if-elif
"""
if 조건식:
    조건식이 참일 때 실행할 문장
elif 조건식2:
    조건식2이 참일 때 실행할 문장
else:
    모든 조건식이 거짓일 때 실행할 문장
"""
score = 90
if score >= 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
else:
    print("F")

print("프로그램 종료")

# if 안 if
if num % 2 == 0:  # 짝수이면
    pass  # 짝수이면 실행문 나중에 구별하겠다. : 아무일도 안하지만 error나지 않도록 하는 문장
else:  # 홀수이면
    print('odd')

print("프로그램 종료")

if num % 2 == 0:  # 짝수이면
    if num % 4 == 0:
        print('four')
    else:
        print('not four even')
else:  # 홀수이면
    print('odd')

print("프로그램 종료")

