"""
반복문 연습
***cf. shift + f6 (mac shift+fn+F6) : refactor / rename 의 기능이 있다. (변수가 쓰인 곳을 한번에 바꿔줌 - 한글의 바꾸기 기능)
"""


# 1 + 2 + .. 100 = ?
x = 1                                       # x, sum_while = 1, 0 으로 써도 괜찮다.
sum_while = 0                               # 변수 이름을 sum 이라고만 하면, sum 이라는 함수를 쓰지 못한다
while x <= 50:
    sum_while += x + (101 - x)
    x += 1
print(f'while문으로 만든 합 : {sum_while}')
# or
sum_for = 0
for x in range(101):
    sum_for += x
    x += 1
print(f'for문으로 만든 합 : {sum_for}')
# or
numbers = [x for x in range(1, 101)]
print('list comprehension으로 만든 합 :', sum(numbers))


# 1 + 2 + .. x <= 100
x = 1
while 1:
    if (x * (x+1) / 2) <= 100:
        x += 1
    else:
        print(f'{x}이면 {x*(x+1)/2} > 100입니다.')
        break
# or
x = 1
while True:
    if ( x * (x+1) / 2 ) <= 100:
        x += 1
    else:
        print(f'{x}이면 {x*(x+1)/2} > 100입니다.')
        break
# or (sam answer)
x, total = 1, 0
while 1:
    total += x
    if total > 100:
        print(f'{x}이면 {x * (x + 1) / 2} > 100입니다.')
        break
    x += 1
# or
x, total = 1, 0
while total <= 100:
    total += x
    print(f'x = {x}, sum = {total}')
    x += 1

