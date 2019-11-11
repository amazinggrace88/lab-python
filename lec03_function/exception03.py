'''
try-except 구문 활용

'''

# input(): 사용자가 정수를 입력할 수도 있고 아닐 수도 있다 (ex 3.0)
# code를 고쳐서 에러 안나게 고칠수는 없으며, try: except를 써야 한다.
try:
    n = int(input('정수 입력>>>'))
    print('n = ', n)
except ValueError:
    print('입력값은 정수여야 합니다!')
# Process finished with exit code 0 : 정상적으로 끝남


# 입력할 때까지 실행하도록 함
while True:
    try:
        n = int(input('정수 입력>>>'))
        print('n = ', n)
        break
    except ValueError:
        print('입력값은 정수여야 합니다!')

print('프로그램 정상 종료')


# try문을 함수로 만들 수 있음

