'''
csv 모듈을 사용한 mpg.csv 파일 읽기
'''

import csv
import os

with open('..\\..\\lab_python\\scratch08\\mpg.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()  # 한 줄 읽고 건너 뜀 -> 첫번째 줄은 컬럼 이름들이기 때문에 저장을 건너뛰어 데이터만을 저장한다.
    df = [line for line in reader]

print(df[0:5])

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
# path.join 을 사용하면 세개를 붙여서 이름을 만들어준다
# Window OS: ..\scratch08\mpg.csv
# Linux, macOS: ../scratch08/mpg.csv
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()  # 한 줄 읽고 건너뜀.
    # 첫번째 줄은 컬럼 이름들이기 때문에.
    df = [line for line in reader]
# \ 는 파이썬에서 특수 문자로써 \n (줄바꿈) 등 으로 사용되는데
# 문자열에서 \가 오기를 원하면 \\ 두개 사용! 해주세욤

print(df[0:5]) #리스트 df에서 인덱스 0~4 까지 행을 출력
# 리스트 df 에서 0번째 행의 0, 1, 2번째 컬럼 아이템만 출력
print(df[0][0], df[0][1], df[0][2]) # audi a4 1.8

# 리스트에서 각 행 마다 반복하면서, 각 행의 인덱스 2번 아이템을 숫자로 변환해서 새로운 리스트에 저장
# 배기량만 꺼내겠다 [행에서 처음부터 끝까지] [선택적인 컬럼 넘버] 하면 대여,,,
displ = [float(row[2]) for row in df]
print(displ) #[1.8, 1.8, 2.0, ...] 비로소 숫자가 되었다
# displ = [row[2] for row in df] -> row 를 float 에 넣어버리기!
#['1.8', '1.8', '2', '2',...]
# string type 으로 숫자들이 들어가 있어서 문제! 데이터 타입 변형 필요필요

with open(file_path, mode = 'r', encoding = 'UTF-8') as f:  # column header 를 제거하지 않고 읽어달라고 함
    # 사전(dict) 타입으로 데이터들을 읽어주는 reader 객체
    # 보통 csv 파일에 컬럼 이름이 포함된 경우 사용
    reader = csv.DictReader(f)
    # DictReader 객체의 read 기능을 사용하면, 각 행은 '컬럼이름: 값'의 쌍으로 이루어진 dict(사전)가 됨.
    df = [row for row in reader]

print(df[0:5])
# [OrderedDict([('manufacturer', 'audi'), ('model', 'a4'), ('displ', '1.8'), ('year', '1999'), ('cyl', '4'), ('trans', 'auto(l5)'), ..]
# returned a list of tuples (colname, value)
# If we take a close look at the returned value, key - value; and the keys are the column names
print(df[0])
# OrderedDict([('manufacturer', 'audi'), ('model', 'a4'), ('displ', '1.8'), ('year', '1999'), ('cyl', '4'), ('trans', 'auto(l5)'), ('drv', 'f'), ('cty', '18'), ('hwy', '29'), ('fl', 'p'), ('class', 'compact')])
print(df[0]['manufacturer']) # audi
print(df[0]['model']) # a4
print(df[0]['displ']) #1.8
# 왜 편하지? 0번째 이름에서 컬럼의 인덱스를 몰라도 이름만 알면 끄집어 낼 수 있다
# 행의 특정 원소를 찾아갈 때, 인덱스가 아닌 컬럼 이름으로 찾을 수 있다
displ = [float(row['displ']) for row in df]
print(displ) # [1.8, 1.8, 2.0, 2.0,..]
# 변수가 커지면 컬럼이름은 많고, 컬럼의 숫자는 세기가 어려워질 때가 많다

