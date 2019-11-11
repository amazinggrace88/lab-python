'''
재귀함수(recursive function)
'''

# factorial 만들기
# n!
# 0! = 1

def factorial1(n: int) -> int:
    result = 1
    for x in range(1, n+1): # 1 x 2 x .. n x 이므로
        result *= x # result = result * x (for 문 안의 x를 곱해야함)
    return result

for x in range(6):
    print(f'factorial {x} = ', factorial1(x))




# 재귀함수로 factorial 만들기
def factorial2(n: int) -> int:
    if n == 0:                 # 재귀함수는 언젠가는 재귀가 끝날 수 있도록 종료하는 코드가 있어야 한다.
        return 1
    elif n > 0:
        return factorial2(n-1) * n

for x in range(6):
    print(f'factorial {x} = ', factorial2(x))




# 재귀함수로 sum 만들기
def sum_recursive(n: int) -> int:
    if n == 1:
        return 1
    elif n > 1:
        return sum_recursive(n-1) + n

for x in range(1, 11):
    print(f'sum_recursive {x} = ', sum_recursive(x))




# 재귀함수로 하노이의 탑 만들기
def hanoi(n: int, x:int = 0, y:int = 0, z:int = 0) -> int:
    # 재귀함수의 맨 첫번째 값 (for not stack_overflow)
    if n == 1:
        return 1
        # 1개의 원반을 기둥 3(z: n-x-y)으로 옮긴다.
    elif n > 1:
        # n -1개의 원반을 기둥 1(x)에서 기둥 2(y)로 옮긴다. x + y + z = n
        hanoi(n - 1, x, z, y)
        # 남은 1개의 원반을 기둥 1(x)에서 기둥 3(z)로 옮긴다.
        # n개의 원반을 기둥 2(y)에서 기둥 3(z)로 옮긴다.
        hanoi(n - 1, y, x, z)
        return


hanoi(7)

# 재귀함수로 하노이의 탑 만들기 정답
def hanoi_tower(n:int, start:int, target:int, aux:int) -> int:
    """
    재귀 함수를 사용해서 하노이의 탑 문제를 해결 방법을 출력

    :param n: 옮길 원반 갯수(양의 정수)
    :param start: 처음에 원반들이 있는 시작 기둥 번호
    :param target: 원반들을 모두 옮겨놓을 목표 기둥 번호
    :param aux: 보조 기둥으로 사용할 기둥 번호 (Auxiliary의 줄임말)
    :return: None
    """
    # error 처리 n < 0 은 하지 않는다.
    if n == 1:
        print(f'{start} -> {target}')
        return
        # 함수를 종료하겠다는 뜻으로 return을 씀(return의 기능 2가지 : 함수호출, 함수종료)
    elif n > 1:
        # n > 1인 경우 : (n-1)개의 원반을 target을 보조기둥으로 사용하여 보조 기둥(aux)에 옮긴다.
        hanoi_tower(n-1, start, aux, target)
        # 시작 기둥에 있는 나머지 1개의 원반을 목표기둥으로 옮김
        print(f'{start} -> {target}')
        # aux 기둥에 남아있는 (n-1)개의 원반을 start 기둥을 보조기둥으로 사용해서 target으로 옮김
        hanoi_tower(                                                                                                                                                                                                                                                                                                                                                                                                                                       n-1, aux, target, start)

# 원반 1개
for n in range(1, 5):
    print(f'{n}개 원반이 있는 하노이탑')
    hanoi_tower(n, start = 1, target = 3, aux = 2)
    print('==============')





