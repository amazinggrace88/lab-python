"""
matplotlib.pyplot 모듈을 사용한 데이터 시각화
(교재 제 3장 데이터 시각화)

like r ggplot

순서
1) terminal을 연다
2) 명령어 입력
pip list
pip install
pip show matplotlib ) Location: c:\dev\python37\lib\site-packages 에 설치되었다. 설치되었을 때만 보여짐
pip uninstall (패키지 메모리에서 없애고 싶을 때)
"""

# plotting 을 위한 패키지 임포트
import matplotlib.pyplot as plt  # 많이 하는 방법 (패키지 안 모듈)
from collections import Counter  # 기본 패키지 collections 에서 클래스 counter 꺼내서 import - import는 항상 위에 쓰자!

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]



# 1) 선 그래프 그리기
# plot : 선 그래프 생성만(호출하지 않음)
# plt.plot(x 좌표, y 좌표, color = 'green', marker= 데이터마다 점 표시, linestyle='solid')
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# 제목 더하기 함수 (D2Coding을 사용하여 한글 이름 사용 가능)
plt.title("연간 GDP", fontname='NanumGothic')
# 레이블 추가
plt.ylabel("Billions of $")
plt.xlabel('Year')
# savefig : 그래프 저장
plt.savefig('../image_output/year_gdp.png') # save를 먼저 하고 show를 하면 작동.
# show : 그래프를 화면에 보여줌
plt.show()



# 2) 막대 그래프 그리기
# 이산적인 항목/연속적인 항목에 대한 변화(histogram)이라고 한다.
movies = ['Anne Hall', "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]  # 이산 데이터
num_oscars = [5, 11, 3, 8, 10]  # 수치 데이터

# 막대그래프 for 이산 데이터
plt.bar(movies, num_oscars)
font_name = {'fontname':'NanumGothic'}  # 변수 선언하여 매번 글꼴 지정하는 불편함 줄이자
plt.title('아카데미 수상작', font_name)  # keyword argument = 함수 내부에서 dict 취급
plt.xlabel('수상 횟수', font_name)
plt.show()  # 그래프를 닫아야 과정이 끝남 (exit code 0 출력)

# 막대그래프 for histogram(연속 데이터) using counter
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
# from collections import Counter # 기본 패키지 collections 에서 클래스 counter 꺼내서 import - import는 항상 위에 쓰자!
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print(histogram) # 그냥 histogram 만들기
plt.bar(histogram.keys(), histogram.values()) #bar 그래프 만들기 : dict의 key, value를 한꺼번에 꺼낼 때는 items
plt.yticks([0, 1, 2, 3, 4, 5])
plt.show()
# 설명
# Counter({80: 4, 90: 3, 70: 3, 0: 2, 60: 1}) : 구간의 갯수를 센다. - 워드카운팅할때 많이 사용
# min(grade // 10 * 10, 90) for grade in grades : grades에서 item을 꺼내서 나눈 몫*10(버림) - list comprehension
# list comprehension : [x for x in range(10)] : 0~9까지 list 만듬
# min()의 의미 : 100점이 90점대로 들어가기 위해서, 즉, 90~100구간에 포함시키기 위해서

# 권장 : 막대그래프 for histogram(연속 데이터) using plt.hist
plt.hist(grades, edgecolor = 'black') # histogram 자체가 grade의 갯수를 세어준다. / edgecolor = 'black' : 선 색
plt.yticks([0, 1, 2, 3, 4, 5])
plt.show()
# bins : histogram 의 구간 길이

# histogram 비교 : y 축 제대로 설정하기
mentions = [500, 505]
years = [2013, 2014]
plt.bar(years, mentions, 0.5) # year가 순서대로 출력되지 않고 연속적으로 출력된다.
plt.axis([2012.5, 2014.5, 499, 506])
plt.xticks(years) # xticks : x축에 표시할 눈금
plt.ylabel(' # of times I heard someone say \'data science\'')
plt.show()

# https://matplotlib.org/