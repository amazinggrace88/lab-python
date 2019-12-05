'''
csv module
'''
import csv

# 문자열(string)을 원소로 하는 리스트
row1 = ['test1', 'success', 'Mon']
row2 = ['test2', 'failure, kind of', 'Tue']
row3 = ['test3', 'success, kind of', 'Wed']
result = [row1, row2, row3]
print(result)

# 파일을 쓰기 모드로 열기
# 새로운 파일에 result를 입력한다.
with open('test_result.csv', mode='w', encoding='UTF-8') as f:
    # csv writer 객체 생성
    writer = csv.writer(f, delimiter=',')
    # writer 객체의 writerow()메소드를 사용하여 한 줄씩 쓰기
    for row in result:
        writer.writerow(row)
# csv 모듈을 사용하면 ','로 구분 (delimiter 뜻 구분자)
# 연산자를 쓰는 csv 파일은 "~,~"이 ','로 구분되지 않도록 ""로 감싸주고 csv 파일을 만든다.

# csv 모듈을 사용하지 않고 csv 파일을 읽었을 때 문제점
print('\ncsv 모듈 적용 전 ----------')
with open('test_result.csv', mode='r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip().split(','))

# "~,~"이 ,로 구분되 원소 4개의 list 가 된다.
# 원래 데이터에는 없어야 할 ""가 문자열에 포함된다.

# 모듈 적용(csv)
print('\ncsv 모듈 적용 후 ----------')
with open('test_result.csv', mode='r', encoding='UTF-8') as f:
    # csv  reader 객체를 생성
    reader = csv.reader(f)  # reader 객체를 통해서 for in 구문에 적용됨
    for row in reader:
        print(row)

# 큰따옴표 없음, "~,~"안의 ,를 데이터 처리함
# 모듈 적용(pandas)도 해보기!



# print('review-------') --> 왜 안될까? 선생님께 여쭤보기
# with open('emp.csv', mode='w', encoding='UTF-8') as a:
#     writer = csv.writer(a, delimiter=',')
#     for row in result:
#         writer.writerow(row)
# print('\n csv 모듈 적용')
# with open('emp.csv', mode='r', encoding='UTF-8') as a:
#     reader = csv.reader(a)
#     for row in reader:
#         print(row)
