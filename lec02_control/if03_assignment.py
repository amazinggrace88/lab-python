"""
가위(1)바위(2)보(3) - 과제
"""
import numpy as np

print('가위바위보 게임 start')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('------------------')
print('선택하세요~')

user = int(input())  # 입력받은 것을 정수로 변환해서 user 에 저장

# 난수 생성 함수
computer = np.random.randint(1, 4)  # 1, 2, 3 중 하나 (1보다 크거나 같고, 4보다 작은 random variable 생성)
print(computer)

# 승부내기 by if문 (using &)
if user < computer:
    if user == 1 and computer == 3:
        print('user is win')
    else:
        print('computer is win')
elif computer < user:
    if computer == 1 and user == 3:
        print('computer is win')
    else:
        print('user is win')
else:
    print('fair~')

print('done')

# using result
result = user - computer
if result == 0:
    print('fair~')
elif result == 1 or result == -2:
    print('user is win')
else:
    print('computer is win')
