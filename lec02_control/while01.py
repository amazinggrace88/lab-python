"""
while 반복문:
--구조--
[초기식] 생략 가능
while 조건식:
    조건식이 참일 동안에 실행할 문장
    [조건을 변경할 수 있는 식] 생략 가능하지만 많이 쓴다(중요함)

"""


# 1~10까지 옆으로 출력
n = 1                  # [초기식]
while n <= 10:         # while 조건식
    print(n, end=' ')  # 조건식이 참일 동안에 실행할 문장
    n = n + 1          # [조건을 변경할 수 있는 식]
print()                # 줄바꿈
# or
n = 1
while n <= 10:
    print(n, end=' ')
    n += 1
print()


# while 문 99dan (2dan) : 실행문장의 순서 중요함!!!
n = 1
while n <= 9:
    print(f'2 x {n} = {2*n}')
    n += 1
print()


# while 문 99 dan 2~9dan
n = 2
while n <= 9:
    m = 1
    while m <= 9:
        print(f'{n} x {m} = {n*m}')
        m += 1
    n += 1
    print('--------------')


# while 문 99 dan 2~9dan (break - n = m)
n = 2
while n <= 9:
    m = 1
    while m <= 9:
        print(f'{n} x {m} = {n*m}')
        if n == m:
            break
        m += 1
    n += 1
    print('--------------')


#