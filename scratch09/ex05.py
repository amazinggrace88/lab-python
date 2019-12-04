"""
gapminder.tsv 불러온 방법: 선생님 컴퓨터에서 파일을 다운 받은 후에, scratch09 에 대고 ctrl + c, ctrl + v 그리고 확인, 확인
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame 으로 변환
DataFrame의 행과 열의 개수 확인
DataFrame의 앞의 데이터 5개를 출력
DataFrame의 뒷쪽 데이터 5개 출력
DataFrame 에서 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame에서 'country', 'lifeExp','gdpPercap' 컬럼들만 출력
DataFrame 에서 행 인덱스가 0, 99, 999번인 행들을 출력
DataFrame 에서 행 레이블이 840번부터 851번까지인 행들의 나라이름, 기대 수명, 1인당 GDP를 출력

<수업시간에 다루지 않은 내용>
DataFrame 에서 연도별 기대 수명의 평균을 출력하여라 (group by - mean)
DataFrame 에서 연도별, 대륙별 기대 수명의 평균을 출력하여라
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

# gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame 으로 변환
# file_path = os.path.join('gapminder.tsv')
# df = pd.read_csv(file_path, sep='\t')
# print(df)
# or
gapminder = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
# sep= 꼭꼭 \t 추가한다. (default 값: , )



# DataFrame.shape: (row 개수, column 개수)
print(gapminder.shape)
nrows, ncols = gapminder.shape
print(f'nrows={nrows}, ncols={ncols}')

print('shape:', gapminder.shape)   # DataFrame의 행과 열의 개수 확인

# DataFrame.head(n): 첫 n개의 row를 출력. n의 기본값은 5.
print(gapminder.head())

# DataFrame.tail(n): 마지막 n개의 row를 출력. n의 기본값은 5.
print(gapminder.tail())



# 행 인덱스를 이용한 출력
# DataFrame.iloc[row index, column index]
# 만약 column index를 생략하면, 선택한 row index 의 모든 컬럼이 선택된다 / row index는 생략할 수 없음
print(gapminder.iloc[0:5])
print(gapminder.iloc[nrows - 5:nrows])  # 인덱스 a:b는 a <= x < b를 의미함./ 파이썬은 마지막 숫자는 포함하지 않으니까 이렇게 씀
print('headers', list(gapminder))  # DataFrame 에서 컬럼 이름들을 출력
print('headers', list(gapminder.columns))
# DataFrame.columns: pandas.Index 클래스 객체. 컬럼 이름들의 리스트를 가지고 있음.
print(gapminder.columns)
# 컬럼이름들을 알아내면 변수처리해서 일하기가 쉬워진다/아니면 인덱스 번호만 가지고 사용해야 하는데, 그러면 내가 무슨 컬럼을 사용하는지 가독성이 떨어진다
# DataFrame.dtypes: pandas.Index 클래스 객체.(각 컬럼의 이름과 데이터 타입을 저장하고 있는 프로퍼티) - gapminder의 각 컬럼의 데이터 타입들을 출력
print('data types', gapminder.dtypes)



# pandas.read_csv() 함수는 파일의 문자열들을 타입에 맞게끔 변환하는 기능을 가지고 있음.
# pandas 데이터 타입: object(문자열), int64(64비트 정수), float64(64비트 실수) (# 1 byte = 8 bits)
# 파이썬 의 데이터 타입
# 더 많은 용량을 사용해서 정수를 사용한다. 64 바이트 = 8 비트, 그러니까 파이썬은 정수, 실수 모두 8 비트를 사용해서 저장한다
# 보통 C와 같은 다른 언어는 정수는 4비트를 사용해서 저장. 결론적으로 파이썬은 큰 정수까지 저장할 수 있는 타입이라고 생각해주면 된다

print(gapminder.dtypes)

# DataFrame[column names]: 데이터 프레임에서 컬럼을 선택.(# 행번호 주지 않고 컬럼 이름들만 주는 가장 간단한 방법)
col_names = ['country', 'lifeExp', 'gdpPercap']
print(gapminder[col_names])



# 데이터 프레임에서 특정 행을 선택하는 방법
# 1) index로 선택:
# 데이터 프레임에서 특정 행(row)들을 인덱스로 선택
# row_indices = [0, 9, 999]
# print(gapminder.iloc[row_indices])
# or
print(gapminder.iloc[[0, 9, 999]])

# DataFrame.iloc[row index, column index]
# DataFrame.loc[row label, column label]
# loc에서 범위 연산자(:)가 사용되면, 이름(label)로 취급하기 때문에 양쪽 숫자 모두 포함
# iloc에서  범위 연산자(:)가 사용되면, 인덱스로 취급하기 때문에 뒤쪽 숫자는 미포함
# DataFrame 에서 행 레이블이 840번부터 851번까지인 행들의 나라이름, 기대 수명, 1인당 GDP를 출력
print(gapminder.loc[840:851, ['country', 'lifeExp', 'gdpPercap']])  # Teacher's solutionn # N:M 으로 인덱스를 주면 이름을 주는거니까 그대로 출력해준다
print(gapminder.iloc[840:852, [0, 3, 5]])  # iloc 는 N:M 으로 인덱스를 줄 경우 이상 미만이라서 M + 1의 값을 줘야한다



# 2) 특정 행을 직접 선택:
# DataFrame.iloc: 특정행을 선택하는 방법
# DataFrame 에서 행 인덱스가 0, 99, 999번인 행들을 출력
print(gapminder.iloc[0])
print(gapminder.iloc[99])
print(gapminder.iloc[999])
# teacher's solution
row_indices = [0, 9, 99]
print('row_indices =', [gapminder.iloc[row_indices]])
# OR
print("row_indices' =", gapminder.iloc[[0, 9, 99]])



# 연도별 기대수명(lifeExp)의 평균
gapminder_by_year = gapminder.groupby('year')
print(gapminder_by_year)  # DataFrameGroupBy 객체
print(gapminder_by_year['lifeExp'])  # SeriesGroupBy 객체
print(gapminder_by_year['lifeExp'].mean())

# DataFrame 에서 연도별, 대륙별 기대 수명의 평균을 출력하여라
# df.groupby(year).mean(lifeExp)
# df_by_year2 = gapminder.groupby(['year','continent'])
# print(df_by_year2)
# print(df_by_year2['lifeExp'].mean())
# or
gapminder_by_year_continent = gapminder.groupby(['year', 'continent'])
print(gapminder_by_year_continent['lifeExp'].mean())

# 1차원 데이터를 series라고 부르고, series 의 집합이 데이터 프레임이 된다



# 연도별 기대수명 그래프
# df.groupby(year).mean(lifeExp)
year_lifeExp = gapminder.groupby('year')['lifeExp'].mean()
print(year_lifeExp)
plt.plot(year_lifeExp)
plt.title('lifeExp by year')
plt.show()



# 연도별 전세계 인구수(pop)를 그래프
year_pop = gapminder.groupby('year')['pop'].sum()
print(year_pop)
plt.plot(year_pop)
plt.title('pop by year')
plt.show()
