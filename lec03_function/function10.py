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