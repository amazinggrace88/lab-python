'''
try 문 실습 가위바위보 게임

- 몇번을 반복해야 할 지 모를 때 while true & break(혹은 return)을 통해 해결 가능하다.
'''

def user_input_answer():
   """
   가위바위보 게임으로 사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내.
   사용자가 입력한 숫자를 리턴
   사용자가 문자열을 입력한다면(숫자로 변환 불가), 안내문 출력 후 다시 입력받음.
   사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력 후 다시 입력받음.

   :return: 1, 2, 3 중 하나
   """
   while True:
       try:
           n = int(input('1, 2, 3 which one?'))
           if n in (1, 2, 3):
               return n # 함수 종료인 break와 같다, 함수 종료 & 값 return
           else:
               raise ValueError()
       except ValueError:
           print('1, 2, 3 which one? input again')
# 함수는 들여쓰기가 되어 있어야 한다.

user = user_input_answer()
print('입력값 : ', user)


# 이해하지 못함. 다시 복습해보기 (일부러 error를 발생시키는 경우)
def user_input():
    """
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내.
    사용자가 입력한 숫자를 리턴.
    사용자가 숫자로 변환할 수 없는 문자를 입력하면, 안내문 출력 후 다시 입력받음.
    사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력 후 다시 입력받음.

    :return: 1, 2, 3 중의 하나
    """
    while True:
        try:
            try:
                n = int(input('1, 2, 3 중에 숫자 하나를 입력>>'))
            except ValueError:
                raise ValueError('문자는 입력하면 안되요~')
            if n in (1, 2, 3):
                return n  # break
            else:
                raise ValueError('1, 2, 3만 가능')
        except ValueError as e:
            print(e.args)
    # return n


user = user_input()
print('입력 값 =', user)
