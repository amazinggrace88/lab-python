'''
csv 모듈을 사용한 mpg.csv 파일 읽기
'''

import csv

with open('..\\..\\lab_python\\scratch08\\mpg.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    df = [line for line in reader]

print(df[0:5])