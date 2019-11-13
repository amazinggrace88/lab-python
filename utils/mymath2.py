'''
mymath2.py
'''


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

if __name__ == '__main__': # 다른 모듈에서는 사용하지 못하고 이 모듈에서만 사용하는 코드
    print('multiply=', multiply(1,2))
    print('divide=', divide(1, 2))
