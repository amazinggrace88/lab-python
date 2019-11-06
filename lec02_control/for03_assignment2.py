'''
for-in 구문 연습
'''

# 구구단 2~9 출력
# for-in 구문
print('99dan')
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')
    print('------------')

# 구구단은 2*2/3*3/4*4/까지 출력
print('2nd 99dan')
for i in range(2, 10):
    for j in range(1, i+1):
        print(f'{i} x {j} = {i * j}')
    print('------------')
# or
print('3rd 99dan')
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
        if i == j:
            break #뜻 : break가 포함된 가장 가까운 반복문을 종료한다.
    print('------------')


