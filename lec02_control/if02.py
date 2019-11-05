'''
python 에서 True / False 판별
1) 숫자 타입인 경우 0 False, 0 이외의 숫자는 True 취급(1은 True)
2) 숫자 이외의 타입인 경우, 비어있는 값('', "", [], {}, (),..)은 False, 그 이외의 다른 값들은 True 취급
3)
4)
값이 있으면 true, 값이 없으면 false~~
'''

# 1) 숫자 타입인 경우 0 False, 0 이외의 숫자는 True 취급
n = 2
if n % 2:
    print('홀수')
else:
    print('짝수')
# n을 2로 나누면 0(false) -> if false가 되어 else 문을 출력한다.
# if true 면 if 문을 출력한다.

# 2) 숫자 이외의 타입인 경우, 비어있는 값('', "", [], {}, (),..)은 False, 그 이외의 다른 값들은 True 취급
my_list = [] # 비어있는 list
if my_list:
    print(my_list)
else:
    my_list.append('python')
    print(my_list)
#[]이면 if false가 되어 else 문을 출력한다.
#if true면 if문을 출력한다.

# in 연산자
# 변수 in list/tuple/dict .. : ~안에 있으면
languages = ['pl/sql', 'r']
if 'python' in languages:
    pass
else:
    languages.append('python')
print(languages)
# in 안에 없으면, if false 가 되어 else 문을 출력한다.
languages = ['pl/sql', 'r']
if 'python' not in languages:
    languages.append('python')
print(languages)
# 대소문자를 구별한다.
languages = ['pl/sql', 'r', 'python']
if 'Python' not in languages:
    languages.append('Python')
print(languages)

