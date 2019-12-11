import matplotlib.pyplot as plt
import pandas as pd

# 차원 축소 (4차원 - 2차원)
# 하나의 화면을 분할하여 plot 대치하는 방법
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
iris = pd.read_csv('iris.csv', header=None, names=col_names)
iris_groupby_class = iris.groupby(by='Class')

xy = []  # x축, y축에 사용할 변수 이름
for i in range(4):  # i = 0, 1, 2, 3
    for j in range(i+1, 4):  # j = 0+1, ..3 (i=0)
        xy.append((col_names[i], col_names[j]))
print(xy)

fig, ax = plt.subplots(2, 3)  # tuple 을 리턴
# fig figure 화면 - 1개의 창 6개 로 나눌 것이다. (열 2, 행 3)
# figure 안의 하나하나 - subplot (6개 들어감)
# ax axis 축 - 그래프 종류 barplot, plot, scatter 를 그려주는 곳 (한 창에 여러 그래프 종류 그릴 수 있다)
xy_idx = 0
for row in range(2):
    for col in range(3):
        axis = ax[row, col]  # numpy array 에서 사용하는 방법 (= ax[row][col] 가능)
        x = xy[xy_idx][0]
        y = xy[xy_idx][1]
        xy_idx += 1
        axis.set_title(f'{x} vs {y}')  # subplot 의 제목
        axis.set_xlabel(x)  # subplot 의 x 레이블
        axis.set_ylabel(y)  # subplot 의 y 레이블
        for name, group in iris_groupby_class:
            axis.scatter(group[x], group[y], label=name)  # ex04 에서 했었던 종류별로 묶어 그래프 점 뿌리는 형태
plt.legend()
plt.show()
# 목적 : 차원축소 했을 때 setosa 를 구분하는 축은 뭐가 좋을 까? (0, 1), (1, 0) 번째가 제일 잘 구분하는 축일 것이다 - 하고 분석하면 되요
#       머신러닝 전에 알고리즘 어떤 걸 써야 하는지 알려주는 역할
#       petal 2 개 축으로 차원축소하면 분류 잘 되겠다 - 하고 분석하면 되요~

# 암 데이터도 해보기

