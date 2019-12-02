'''
csv 모듈을 사용한 mpg.csv 파일 읽기
'''

import csv

with open('..\\..\\lab_python\\scratch08\\mpg.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()  # 한 줄 읽고 건너 뜀 -> 첫번째 줄은 컬럼 이름들이기 때문에 저장을 건너뛰어 데이터만을 저장한다.
    df = [line for line in reader]

print(df[0:5])

# reader / writer 기억!