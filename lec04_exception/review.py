# try 구문
try:
    numbers = [1, 2, 3]
    for i in numbers:
        print(i)
    print('try ~ ')
except ValueError:
    print('value error ~ ')
except IndexError:
    print('index error ~ ')
else:
    print('실행')
finally:
    print('finally 블록')

