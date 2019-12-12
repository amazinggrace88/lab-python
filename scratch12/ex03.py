"""
1. 이산 확률 변수에서의 나이브 베이즈 원리 구현
"""
# nb-test 를 나이브베이즈 알고리즘으로 분석하자
import pandas as pd


# dataset = pd.read_csv('nb_test.csv')
# print(dataset)  # tab 으로 data 가 나누어져 있어서(\t) 컬럼 1개짜리 데이터 프레임으로 리턴된다.
dataset = pd.read_csv('nb_test.csv', sep='\t')
print(dataset)  # 카테고리 데이터 (특정 경우만 갖는 경우: 이산)

# 확률 계산하기 (과거의 데이터를 기반으로 미리 알고 있는 확률 계산 : 사전확률)
# 외출할 확률 : P(go_out)
p_go_out = 5 / 10
# 집에 있을 확률 : P(stay_home)
p_stay_home = 5 / 10  # = 1 - p_go_out 서로 배타적
# 외출했을 때 날씨가 맑을 확률 : P(sunny | go_out)
p_sunny_when_go_out = 4 / 5
# 외출했을 때 비가 올 확률 : P(rainy | go_out)
p_rainy_when_go_out = 1 / 5
# 외출했을 때 자동차가 정상일 확률 : P(working | go_out)
p_working_when_go_out = 4 / 5
# 외출했을 때 자동차가 고장일 확률 : P(broken | go_out)
p_broken_when_go_out = 1 / 5
# 방콕일 때 맑을 확률 : P(sunny | stay_home)
p_sunny_when_stay_home = 2 / 5
# 방콕일 때 비가 올 확률 : P(rainy | stay_home)
p_rainy_when_stay_home = 3 / 5
# 방콕일 때 자동차가 정상일 확률 : P(working | stay_home)
p_working_when_stay_home = 1 / 5
# 방콕일 때 자동차가 고장일 확률 : P(broken | stay_home)
p_broken_when_stay_home = 4 / 5

# 사후확률 계산하기 : class 없는 경우, weather, car 로 class 예측하기
# 만약 날씨 맑고, 자동차가 정상이면 외출할 확률 : P(go_out | sunny, working)
# P(go_out|sunny,working) = ?, P(stay_home|sunny,working) = ? 단, sunny 와 working 이 독립이라는 가정이 있어야 함
# P(A|B) = P(A, B) / P(B)
# P(B|A) = P(B, A) / P(A) 즉, P(B, A) = P(B|A) * P(A)
# P(A|B) = P(B|A) * P(A) / P(B) - 베이즈 정리
# P(X|A, B, C .. etc) 를 계산하기 위해서 베이즈 정리 적용
# P(X|A,B) = P(A,B|X)P(X) / P(A,B)

# naive(순진한) 가정: P(A,B|X) = P(A|X) * P(B|X)
# P(X|A,B) ~ P(A|X) * P(B|X) * P(X) : Naive 베이즈 정리

# 날씨가 맑고 차가 정상이면 외출할 확률 : P(go_out|sunny, working) ~ P(sunny|go_out)*P(working|go_out)*P(go_out)
p_go_out_when_sunny_working = p_sunny_when_go_out * p_working_when_go_out * p_go_out
print(f'{p_go_out_when_sunny_working} ~ {p_sunny_when_go_out} * {p_working_when_go_out} * {p_go_out}')

# 날씨가 맑고 차가 정상이면 방콕일 확률 : P(stay_home|sunny, working) ~ P(sunny|stay_home)*P(working|stay_home)*P(stay_home)
p_stay_home_when_sunny_working = p_sunny_when_stay_home * p_working_when_stay_home * p_stay_home
print(f'{p_stay_home_when_sunny_working} ~ {p_sunny_when_stay_home} * {p_working_when_stay_home} * {p_stay_home}')

# 결론, 날씨가 맑고 차가 정상일 때 외출, 방콕 확률을 각각 계산하여 비교하고, 둘 중 더 큰 값으로 예측함 (나이브 베이즈 정리 증명 완료!)
# cf. 암 데이터에도 적용 가능~ 나이브 베이즈 정리를 이용 여러 조건을 기반으로 암인지 아닌지 판별


# 비가 오고 차가 고장일 때 외출/방콕 예측
# P(go_out|rainy, broken) = ? , P(stay_home|rainy, broken) = ?
# P(go_out|rainy, broken) ~ P(rainy|go_out) * P(broken|go_out)*P(go_out)
p_go_out_when_rainy_broken = p_rainy_when_go_out * p_broken_when_go_out * p_go_out
print(f'{p_go_out_when_rainy_broken} ~ {p_rainy_when_go_out} * {p_broken_when_go_out} * {p_go_out}')
# P(stay_home|rainy, broken) ~ P(rainy|stay_home)*P(broken|stay_home)*P(stay_home)
p_stay_home_when_rainy_broken = p_rainy_when_stay_home * p_broken_when_stay_home * p_stay_home
print(f'{p_stay_home_when_rainy_broken} ~ {p_rainy_when_stay_home} * {p_broken_when_stay_home} * {p_stay_home}')
# 결론 : stay_home 이 더 많다!

