'''
for-in 구문 연습 2
'''


# if in if
for i in range(1, 10):
    if i == 5:
        continue  # for loop 시작점으로 올라감.(if문 안에 있는 밑의 구문들을 건너뛰고 다시 시작점으로 올라가서 계속 한다)
    print(i, end=' ')
print()


# 피보나치 수열(fibonacci sequence)
# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n-2], n >= 2
f = [0, 1]
for i in range(2, 20):
    f.append(f[i-1] + f[i-2]) #x를 합쳐주어 넣어주었다. 원래 x = f[i-1] + f[i-2] / f.append(x)
print('fibonacci sequence : ', f)
# why .extend()는 안될까 ? extend(반복가능한 변수 = 즉, list ex) [4, 5]안의 값을 하나씩 append 하는 작업을 반복한다. )


# 소수(prime number) : 1과 자기자신으로만 나누어지는 정수
# 2~10까지의 정수들 중에서 소수를 찾아서 출력
# 암호화와 복호화에 응용된다.
for i in range(2, 101):
    if i // 2 == 1 and i % 2 == 0:
        print('prime number : ', i)
    if i // 3 == 1 and i % 3 == 0:
        print('prime number : ', i)
    if i // 5 == 1 and i % 5 == 0:
        print('prime number : ', i)
    if i // 7 == 1 and i % 7 == 0:
        print('prime number : ', i) # 다른 소수들 11, 13은 구별할 수 없음!
# or
for n in range(2, 11):
    isPrime = True
    for divider in range(2, n): # 나눠주는 숫자
        if n % divider == 0:
            print(f'{n} = {divider} x {n / divider}')
            isPrime = False
            break
    if isPrime: #break 되었는지 아닌지 확인
        print(f'{n}은 소수!')


# for/while 반복문과 else 가 함께 사용되는 경우 : python의 특수 기능
# 반복문이 break 를 만나지 않고, 범위 전체를 반복했을 때 else 가 실행됨
# 반복문 중간에 break 를 만나면 else 는 실행되지 않음.
for i in range(5):
    if i == 3:
        break
    print(i, end='')
else:
    print('모든 반복을 끝냄') #else의 위치가 안쪽으로 들어가면 안된다! why? for문에서 실행되어야 하기 때문.
# other case
for i in range(5):
    if i == 5:
        break
    print(i, end='')
else:
    print('모든 반복을 끝냄') #else:범위 전체를 반복함.(break 미실행)
# continue 를 만날 때는 else 를 실행한다.
for i in range(5):
    if i == 3:
        continue
    print(i, end='')
else:
    print('모든 반복을 끝냄')

# for else 구문을 이용하여 소수 찾기 실습
for n in range(2, 11):
    for divider in range(2, n): # 나눠주는 숫자 n-1
        if n % divider == 0:
            break
    else: #break 만나지 않았을 때 즉, 소수일 때
        print(f'{n}은 소수!')
