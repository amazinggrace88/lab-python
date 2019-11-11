'''

try 구문-----------
try:
    실행할 문장들
except 에러 종류 [as 별명]:
    에러가 발생했을 때 실행할 문장들
[except 다른 에러: 코드]
[else:
    에러 없이 try 블록 안의 모든 문장이 정상적으로 실행됐을 때 실행할 코드들]
[finally:
    에러 발생 여부와 상관없이 반드시 실행할 문장들]
------------------
cf. : 썼으면 들여쓰기 해야함!

ex) 에러 없을 때
try -> else -> finally
ex2) 에러 발생
try 안의 문장을 실행하다가 에러 발생(에러 발생 전까지 실행하다가 건너뜀) -> except 실행 -> finally

# try 구문의 효과
에러가 발생해도 프로그램이 종료되지 않아 다른 일들을 할 수 있다.

'''


# 실습 1 : 에러 없을 때 (가장 간단한 try 구문)
try:
    numbers = [1, 2, 3]
    for i, v in enumerate(numbers): #enumerate : list의 index와 value를 출력하는 함수이므로 절대 에러 발생하지 않음
        print(i,':', v)
except ValueError: # 에러가 없더라도 except 구문을 try 밑에 써주어야 한다.
    print('인덱스 에러 발생')


# 실습 2 : 에러 없을 때 try -> else -> finally
try:
    numbers = [1, 2, 3]
    for i, v in enumerate(numbers): #enumerate : list의 index와 value를 출력하는 함수이므로 절대 에러 발생하지 않음
        print(i,':', v)
except IndexError: # 에러가 없더라도 except 구문을 try 밑에 써주어야 한다.
    print('인덱스 에러 발생')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally:
    print('finally 블록')
# or
try:
    numbers = [1, 2, 3]
    for i in range(1, 4):
        print(i,':', numbers[i])
    print('try의 모든 내용을 정상적으로 실행')
except ValueError:
    print('값 에러 발생')
except IndexError:
    print('인덱스 에러 발생')
finally: # 에러가 있든 없든 출력
    print('finally 블록') # 여쭙기

# 실습 3 : try 안의 문장을 실행하다가 에러 발생(에러 발생 전까지 실행하다가 건너뜀) -> except 실행 -> finally
try:
    numbers = [1, 2, 3]
    for i in range(1, 4): #enumerate : list의 index와 value를 출력하는 함수이므로 절대 에러 발생하지 않음
        print(i,':', numbers[i])
except IndexError:
    print('인덱스 에러 발생')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally: # 에러가 있든 없든 출력
    print('finally 블록')


# 실습 4 : Error를 잘못 넣은 경우 : try 안의 문장을 실행하다가 에러 발생(에러 발생 전까지 실행하다가 건너뜀) -> except 실행되지 못함 (비정상 종료) -> finally
# except 구문 추가 이유 : 여러개의 error 종류를 잡아내려고
# try:
#     numbers = [1, 2, 3]
#     for i in range(1, 4): #enumerate : list의 index와 value를 출력하는 함수이므로 절대 에러 발생하지 않음
#         print(i,':', numbers[i])
# except ValueError: # 맞지 않는 에러를 넣으면 -> exit code 1으로 비정상 종료되고 / IndexError라고 알려줌
#     print('인덱스 에러 발생')
# else:
#     print('try의 모든 내용을 정상적으로 실행')
# finally: # 에러가 있든 없든 출력
#     print('finally 블록')


# 실습 5 : 실습 4 고침 -> try -> except -> finally
try:
    numbers = [1, 2, 3]
    for i in range(1, 4):
        print(i,':', numbers[i])
except ValueError:
    print('값 에러 발생')
except IndexError:
    print('인덱스 에러 발생')
else:
    print('try의 모든 내용을 정상적으로 실행')
finally: # 에러가 있든 없든 출력
    print('finally 블록')
