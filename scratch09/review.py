
# 1) with as ~ 구문으로 mpg.csv 파일 읽기
import csv
import os

with open('..\\..\\lab_python\\scratch08\\mpg.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()  # 한 줄 읽고 건너 뜀 -> 첫번째 줄은 컬럼 이름들이기 때문에 저장을 건너뛰어 데이터만을 저장한다.
    df = [line for line in reader]

print(df[0:1])

# 3) mpg.csv 파일에서 특정 column 을 새로운 리스트로 저장
displ = [float(row[2]) for row in df]
print(displ)  # float() : 숫자

# 4) DictReader 를 사용하여 mpg.csv 파일 열기
file_path = os.path.join('..', 'scratch08', 'mpg.csv')
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    df = [line for line in reader]

print(df[0:1])  # OrderedDict(key, value)
print(df[0]['manufacturer'])
displ = [float(row['displ']) for row in df]
print(displ)