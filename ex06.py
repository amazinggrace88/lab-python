"""
gapminder.tsv 파일을 읽어서 데이터 프레임 생성
"""
import os
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep="\t", encoding='UTF-8')
print('gapminder is ~~~ \n ', df.iloc[0:5])


# 1
# boolean indexing:
# 컬럼의 값을 이용해서 특정 레코드(행, row)들을 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
# SQL: select * from DataFrame where column == '';
df_afg = df[df['country'] == 'Afghanistan']
print('country = Afghanistan\n', df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print('country = korea\n', df_korea)

# 대한민국(Kores, Rep.)의 인구(pop)과 1인당 GDP(gpdPercap)을 출력
# print(df_korea[['pop', 'gdpPercap']]) : df_korea를 만들지 않고 df에서 바로 추출
print(df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']])
# print(df(데이터프레임)[df['colname'] == 조건식 -> 데이터 프레임의 일부 행만 추출] [<-인덱스 연산자 ['colname','colname2': 컬럼의 이름들을 리스트로 주었다]])
# df[0][0]


# 2
# mpg.csv 파일을 읽어서 DataFrame을 생성
file_path = os.path.join('..', 'scratch08', 'mpg.csv')  # 경로를 병합하여 새 경로 생성 ('C:\Tmp', 'a', 'b') -> "C:\Tmp\a\b"
mpg = pd.read_csv(file_path, encoding='UTF-8')  # csv 파일을 DataFrame 으로 만든다.
print('read_csv로 읽은 df \n', mpg.iloc[0:5])


# 3
# cty 컬럼의 평균을 계산
print(type(mpg['cty']))  # mpg['cty']의 데이터 타입: Series
print(mpg['cty'])  # 데이터타입 구별하기 : series # 0,1,2,3...은 인덱스! # 18, 21 ... 은 실제 데이터! -> 시리즈

print(type(mpg[['cty']]))  # mpg[['cty']]의 데이터 타입: DataFrame : 데이터 프레임에서 컬럼'들'을 뽑아내겠다
print(mpg[['cty']])  # select cty from mpg; 이렇게 한건 컬럼/들을 뽑아낸 것이기 때문에 하나의 시리즈 객체로 보지않고, 컬럼 이름이 있는 데이터 프레임으로 본다

mean_cty = mpg['cty'].mean()  # data type: float
print(mean_cty)

# cty 컬럼의 값이 평균보다 큰 레코드들을 출력
subset = mpg[mpg['cty'] > mean_cty]  # [[<- 행들을 뽑아내기 위한 조건식 ]] <- 행들을 뽑아내기 위한 괄호
print(subset)

# cty가 평균 이상인 자동차들의 model, cty, hwy 컬럼을 출력
print(subset[['model', 'cty', 'hwy']])

# cty 컬럼의 값이 평균보다 큰 레코드들을 출력 2
print('avg cty =', mean_cty)
mean_cty2 = mpg[['cty']].mean() #data type: series
# column 이 1개짜리인 컬럼의 평균을 계산해준 것 (비교할 때 괄호 2개 사용 불가! [[]]) --> ?
print(type(mean_cty2)) #<class 'pandas.core.series.Series'> # 왜 시리즈일까? 원소 1개짜리 시리즈...
print('avg cty2 =', mean_cty2)

# cty 컬럼의 값이 cty평균보다 큰 자동차들의 model, displ, cty, hwy를 출력
# select model, displ, cty, hwy from mpg where cty > avg(cty)
print(mpg[mpg['cty'] > mpg['cty'].mean()][['model','displ','cty','hwy']])
print(subset[['model', 'cty', 'hwy']])

# 데이터 프레임과 시리즈와 같은 데이터 타입을 잘 정리/생각을 해야 나중에 안 헷갈림!

