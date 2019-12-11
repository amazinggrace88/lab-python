# coding=utf-8
'''pandas : group_by / aggregate / apply 복습
'''
import numpy as np
import pandas as pd
import cx_Oracle
from lab_python.scratch09.ex10 import select_all_from

df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randint(0, 10, 5),
    'data2': np.random.randint(0, 5, 5)
})
print(df)

grouped = df.groupby(by='key1')
print(grouped)
cnt = grouped['data1'].count()
print(cnt)

mean = grouped[['data1', 'data2']].mean()
print(mean)

print('cnt_a = ', cnt['a'])
print('cnt_b = ', cnt['b'])

grouped2 = df.groupby(['data1', 'data2'])
print(grouped2[['data1', 'data2']].mean())  # index ['', ''] 2개 !

# 1)-3
people = pd.DataFrame(np.random.randint(0, 10, (5, 5)),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jimmy', 'Travis'])
# len으로 그룹 만들기
len_group = people.groupby(len).sum()
print('len_group = \n', len_group['a'])
print(people.groupby(len).sum())
# print(people.groupby(lambda x: x.contains('J')).sum()) # ----> ?? 여쭈어보기


# ex02
def peak_to_peak(x):
    return x.max() - x.min()

# oracle server connect & emp_df return
if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        with connection.cursor() as cursor:
            emp_df = select_all_from('emp', cursor)
    emp_df.to_csv('emp_df.csv', index=False)

    g1 = emp_df.groupby(by='DEPTNO')
    print(g1['SAL'].mean())
    g2 = emp_df.groupby(by='')

# ex08
with open('web01.html', mode='r', encoding='UTF-8') as f:
    # html parsor : html5lib, 분석 도구 BeautifulSoup
    soup = BeautifulSoup(f, 'html5lib')
    print(soup)
# h1 tag 찾는 방법 : find - 첫번째 1개만 출력
h1 = soup.find('h1')
print(h1)
h1_1 = soup.h1
print(h1_1)
# find_all
h1 = soup.find_all('h1')
print(h1)
h1_1 = soup('h1')
print(h1_1)
# .get (태그의 속성이 가지고 있는 값만 추출하여 리턴)

# ex09
# 파일 열어서 soup 에 분석한 BeautifulSoup 객체를 생성 - DOM tree가 만들어진다.
with open('web02.html', mode='r', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

# class로 요소를 찾는 방법
# Dictionary 로 찾기
# class_ 로 찾기


