'''
함수에서 return의 의미:
1) 함수를 종료한다. (아무값도 리턴하지 않고 return 만 써서 종료 가능)
2) 함수를 호출한 곳에 값을 반환(리턴)

yield의 의미:
리턴과 비슷한 기능을 하지만,
반복문 안에서만 함수의 결과를 반환 (그 위치에서 바로 결과를 반환하지 않음!, 지금 당장 반환하지 않고, 반복문 안에서 하나씩 반환)
'''


# 실습 1 yield 개념
def test():
    x = 0
    while x < 4:
        return x # 이 위치에서 함수 종료이므로 x = 0에서 리턴되고 함수는 종료된다.
        # x += 1   절대로 실핻될 수 없는 코드

for i in range(4):
    print(test())

def test2():
    x = 0
    while x < 4:
        yield x
        x += 1

print(test2()) # <generator object test2 at 0x00000145507CB5C8> : yield x 때문에 generator object를 만든다.
# generator object : for 문 안에서 사용된다. 
for x in test2():
    print(x)
# 과정 : yield가 generator object를 만들고, 반복문을 끝내지 않고 결과값을 keeping 즉, 내부적으로 가진다. for 문 안에서 하나씩 밖으로 나온다.


# 실습 2 range() 함수를 yield 를 이용해 만들기
def my_range(start = 0, end = 1):
    x = start
    while x < end:
        yield x
        x += 1

print(my_range()) # <generator object my_range at 0x0000025D61A1B5C8>
for x in my_range(start=1, end= 10):
    print(x)