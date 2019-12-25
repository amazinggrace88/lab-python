"""
matplotlib.pyplot 모듈을 사용한 데이터 시각화 - 산점도 그래프 & 그래프 왜곡
(교재 제 3장 데이터 시각화)

like r ggplot

"""
import matplotlib.pyplot as plt


# scatter plot
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # 산점도의 point 에 표시할 label : annotate

plt.scatter(friends, minutes)  # x, y만 있어도 그래프 그릴 수 있다.

# plt.annotate('a', xy=(70, 175), xytext=(5, -5), textcoords='offset points')
# plt.annotate (산점도 뿐 아니라 모든 그래프에서 활용 가능)
# 'a' : point
# xy=(70, 175) point 에 'a'를 집어넣자 : xy의 좌표
# xytext=(5, -5) : point의 좌표 x + 5, y - 5만큼 떨어져서 point를 표시하여라
# textcoords='offset points' : 절대위치가 아니라 offset 은 상대적으로 위치를 설정한다. 즉 함수의 기준(input)대로 떨어뜨려서 위치를 지정하는 것이다.

for l, f, m in zip(labels, friends, minutes):  # zip 2개 이상을 할 수 있으므로! 중요!! *****
    plt.annotate(l, xy=(f, m), xytext=(5, -5), textcoords='offset points')
plt.title('Minutes vs Friends')
plt.xlabel('# of friends')
plt.ylabel('daily minutes spent on the site')
plt.show()

for l, f, m in zip(labels, friends, minutes):
    plt.annotate(l, xy=(f, m), xytext=(5, -5), textcoords='offset points')
# 그래프 왜곡된 경우 : scale 의 중요성
math = [99, 90, 85, 97, 80]
science = [100, 85, 60, 90, 70]
# 상관관계 => 그래프로 알고 싶을 때
plt.scatter(math, science)  # 자동으로 scaling
# plt.show() # 시험점수이기 때문에 x, y scale 이 같아야 하는데, 서로 다르기 때문에 그래프만 보고 정확하게 관계를 정의할 수 없다
# solution
plt.axis('equal')
plt.title('Science VS Math')
plt.xlabel('Math')
plt.ylabel('Science')
plt.show() # scale equalized

