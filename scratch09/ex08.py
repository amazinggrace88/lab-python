'''
lec08 database 패키지 내용들을 참조하여
1) oracle database에서 emp table의 모든 레코드를 검색해오고, (select) -> 2차원 리스트
2) csv 모듈을 사용해서, csv 파일로 저장

cf. pip install cx-Oracle==7.2.0 을 dos창에서 써주기 or 파이참 file - setting - project interpreter 에서 upgrade (^)
'''
import csv
import cx_Oracle

if __name__ == '__main__':
    # DSN: Data Source Name: 데이터베이스에 접속할 수 있는 정보
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    # 오라클 데이터베이스 서버에 접속(connection): 함수의 실행결과를 conn 에 저장한 뒤, 모두 끝나면 connection.close() 호출
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # cursor 생성 : cursor : sql 문을 데이터베이스 서버에서 실행
        with connection.cursor() as cursor:  # connection 이라는 클래스가 cursor를 가진다.
            # sql 문장 작성
            sql_select_emp = 'select * from emp'
            # sql 문장을 db 서버에서 실행
            cursor.execute(sql_select_emp)
            # sql 문장 실행 결과 처리: 리스트로 만든다.
            emp = [row for row in cursor]
            print(len(emp))  # emp 테이블의 item의 갯수
            print(emp[0])  # 0번도 실제 데이터값만 들어감 - column 이름 없음 ***** -> pandas에서 파일을 읽을때 맨 처음이 data인지/ header인지 확인하자~

    # tab 1개만 들여쓰기: connect와 같은 level: why? connection 닫혀도 상관 없다
    # emp 내용을 파일에 csv 형식으로 저장
    file_path = 'emp.csv'
    with open(file_path, mode='w', encoding='UTF-8', newline='') as f:  # newline=' ' 줄바꿈 부분을 공백으로 주었다 - 필요없는 한 줄 없애줘~
        # csv writer 객체를 생성
        writer = csv.writer(f)
        for item in emp:
            writer.writerow(item)  # 아이템을 csv 파일에 한 줄씩 써서 csv 파일을 만들었다.



