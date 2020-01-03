"""
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사
3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
4) 선형 회귀식
	cty = slope * displ + intersept(intersect로 부르기도 함)
의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
"""
import random
from lab_python.scratch04.ex01 import vector_mean
from lab_python.scratch08.ex03 import gradient_step
from lab_python.scratch08.ex04 import linear_gradient, minibatches
import matplotlib.pyplot as plt


# 오쌤 정답
with open('mpg.csv', encoding='UTF-8') as f:
    # file 사용이 모두 끝나면 자동으로 close 호출
    # 첫번째 라인을 읽고 버림 - 컬럼 이름들 / 파일 저장 방식 - 한 줄씩 읽고 저장
    f.readline()
    # 한 줄씩 반복 / split(sep=',')로 문자열을 분리해서 만든 (\n전까지) 한 줄이 하나의 list[]가 되었다. 2차원 리스트 생성 / strip()으로 앞,뒤의 공백 제거(줄바꿈, \n 제거)
    df = [line.strip().split(sep=',') for line in f]

print(df[0:5])  # 데이터 프레임 확인
# displ, cty : datatype - 숫자
displ = [float(row[2]) for row in df]  # row를 df에서 추출하고 그 중 index 2번 displ 추출
cty = [float(row[7]) for row in df]
displ_cty = [(d, c) for d, c in zip(displ, cty)]
print(displ_cty[0:5])  # x,y가 tuple로 사용하게 되어 있음 - plt.plot


def mini_batch_gd(dataset, epochs=5000, learning_rate=0.001, batch_size=1, shuffle=True):
    # dataset : list / epoch 반복횟수 / learning_rate step / batch_size 새로운 theta 반영 주기 / shuffle 랜덤 섞기
    dataset = dataset.copy()  # 원본 테이터를 복사해서 사용(shuffle된 데이터와 원본 데이터 구분 - 나중에 저장 위해서)
    theta = [random.randint(-10, 10), random.randint(-10, 10)]  # 직선의 기울기와 절편의 초기값 설정
    print('theta 초기값 : ', theta)
    for epoch in range(epochs):  # epochs 횟수만큼 반복
        if shuffle:
            random.shuffle(dataset)
        mini_batch = minibatches(dataset, batch_size, shuffle)
        for batch in mini_batch:  # 미니 배치 크기만큼 반복
            # 미니 배치 안 점들의 gradient들을 계산
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            # gradient들의 평균을 계산
            gradient = vector_mean(gradients)
            # gradient를 사용하여 theta 변경
            theta = gradient_step(theta, gradient, -learning_rate)
    return theta  # 바깥쪽 for 문에서 return 생성 잊지 말자~


# stochastic 경사 하강법
print('1) 확률적 경사 하강법 -----')
theta_stochastic = mini_batch_gd(displ_cty, epochs=200, shuffle=False)
print('확률적 경사 하강법의 theta 마지막 값 : ', theta_stochastic)

# batch 경사 하강법
print('2) 배치 경사 하강법 -----')
theta_batch = mini_batch_gd(displ_cty, epochs=10000, batch_size=len(displ_cty), learning_rate=0.01, shuffle=True)
print('batch 경사 하강법의 theta 마지막 값 : ', theta_batch)

# mini batch 경사 하강법
print('3) 미니 배치 경사 하강법 -----')
theta_mini = mini_batch_gd(displ_cty, epochs=500, learning_rate=0.01, batch_size=32, shuffle=True)
print('mini_batch 경사 하강법의 theta 마지막 값 : ', theta_mini)


# learning rate, epoch 로 정확도를 조절할 수 있다.

# linear 공식 함수 생성
def linear_regression(x, theta):
    slope, intercept = theta
    return slope * x + intercept


ys_stochastic = [linear_regression(x, theta_stochastic) for x in displ]
ys_batch = [linear_regression(x, theta_batch) for x in displ]
ys_mini = [linear_regression(x, theta_mini) for x in displ]

# pyplot 생성
plt.scatter(displ, cty)
plt.plot(displ, ys_stochastic, color = 'red', label='Stochastic GD')
plt.plot(displ, ys_batch, color = 'green', label='Batch GD')
plt.plot(displ, ys_mini, color = 'blue', label='Mini Batch GD')
plt.xlabel('displacement(cc)')
plt.ylabel('efficiency(mpg)')
plt.title('Fuel Efficiency vs Displacement')
plt.legend()
plt.show()


















# 2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사


from lab_python.lec07_file.file07 import my_csv_reader
# f = open('mpg_python', mode='r', encoding='UTF-8')
#
# while True:
#     line = f.readline()
#     # read(), readline()은 문서 끝에 도달하면 빈 문자열('')을 리턴
#     if line == '':  # 파일 끝(EOF: End Of File)에 도달
#         break  # 무한 루프 종료
#     print(line.strip())
#
# f.close()

# 2차원 행렬 형태로 csv 파일 열기

mpg_python = my_csv_reader('mpg_python')
print(mpg_python)



# 3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
displ = [mpg_python[i][3] for i in range(len(mpg_python))]
print(displ)

cty = [mpg_python[i][8] for i in range(len(mpg_python))]
print(cty)

dataset = [[float(x), float(y)] for x, y in zip(displ, cty)]
print(dataset)

# 4) 선형 회귀식
# cty = slope * displ + intersect 의 기울기(slope)와 절편(intersect)을
# 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
# 1) 확률적 경사 하강법(Stochastic Gradient Descent)
print('1) 확률적 경사 하강법 -----')
theta1 = [1, 1]
step = 0.001
for epoch in range(200):
    random.shuffle(dataset)
    for x, y in dataset:
        gradient = linear_gradient(x, y, theta1)
        theta1 = gradient_step(theta1, gradient, -step)
    if (epoch + 1) % 10 == 0:
        print(f'{epoch + 1}: {theta1}')
stochastic_theta = theta1
print('stochastic_theta = ', stochastic_theta)

# 2) 배치 경사 하강법(Batch GD)
print('2) 배치 경사 하강법 -----')
theta2 = [1, 1]
step = 0.001
for epoch in range(5000):
    gradients = [linear_gradient(x, y, theta2) for x, y in dataset]
    gradient  = vector_mean(gradients)
    theta2 = gradient_step(theta2, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch+1}: {theta2}')
batch_theta = theta2
print('batch_theta = ', batch_theta)

# 3) 미니 배치 경사 하강법(Mini-batch GD)
print('3) 미니 배치 경사 하강법 -----')
theta3 = [1, 1]
step = 0.001
for epoch in range(3000):
    mini_batches = minibatches(dataset, 20, True)
    for batch in mini_batches:
        gradients = [linear_gradient(x, y, theta3) for x, y in dataset]
        gradient = vector_mean(gradients)
        theta3 = gradient_step(theta3, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch+1}: {theta3}')
mini_batch_theta = theta3
print('mini_batch_theta = ', mini_batch_theta)

# 5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인


def stochastic_function(x):
    result = []
    for i, j in stochastic_theta:
        result.append(i*x + j)
    return result


def batch_function(x):
    result = []
    for i, j in batch_theta:
        result.append(i*x + j)
    return result


def mini_batch_function(x):
    result = []
    for i, j in mini_batch_theta:
        result.append(i*x + j)
    return result
#
# s_y = stochastic_function(displ)
# b_y = batch_function(displ)
# m_y = mini_batch_function(displ)
#
# plt.plot(displ, s_y)
# plt.plot(displ, b_y)
# plt.plot(displ, m_y)

# plt.scatter(dataset[0], dataset[1])
# plt.axhline(y=0, color='black')
# plt.axvline(x=0, color='black')

=======
'''
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사
3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
4) 선형 회귀식
	cty = slope * displ + intersect
의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
'''

# 2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사
import random

from lab_python.lec07_file.file07 import my_csv_reader
# f = open('mpg_python', mode='r', encoding='UTF-8')
#
# while True:
#     line = f.readline()
#     # read(), readline()은 문서 끝에 도달하면 빈 문자열('')을 리턴
#     if line == '':  # 파일 끝(EOF: End Of File)에 도달
#         break  # 무한 루프 종료
#     print(line.strip())
#
# f.close()

# 2차원 행렬 형태로 csv 파일 열기
from lab_python.scratch04.ex01 import vector_mean
from lab_python.scratch08.ex03 import gradient_step
from lab_python.scratch08.ex04 import linear_gradient, minibatches
import matplotlib.pyplot as plt

mpg_python = my_csv_reader('mpg_python')
print(mpg_python)



# 3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
displ = [mpg_python[i][3] for i in range(len(mpg_python))]
print(displ)

cty = [mpg_python[i][8] for i in range(len(mpg_python))]
print(cty)

dataset = [[float(x), float(y)] for x, y in zip(displ, cty)]
print(dataset)

# 4) 선형 회귀식
# cty = slope * displ + intersect 의 기울기(slope)와 절편(intersect)을
# 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
# 1) 확률적 경사 하강법(Stochastic Gradient Descent)
print('1) 확률적 경사 하강법 -----')
theta1 = [1, 1]
step = 0.001
for epoch in range(200):
    random.shuffle(dataset)
    for x, y in dataset:
        gradient = linear_gradient(x, y, theta1)
        theta1 = gradient_step(theta1, gradient, -step)
    if (epoch + 1) % 10 == 0:
        print(f'{epoch + 1}: {theta1}')
stochastic_theta = theta1
print('stochastic_theta = ', stochastic_theta)

# 2) 배치 경사 하강법(Batch GD)
print('2) 배치 경사 하강법 -----')
theta2 = [1, 1]
step = 0.001
for epoch in range(5000):
    gradients = [linear_gradient(x, y, theta2) for x, y in dataset]
    gradient  = vector_mean(gradients)
    theta2 = gradient_step(theta2, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch+1}: {theta2}')
batch_theta = theta2
print('batch_theta = ', batch_theta)

# 3) 미니 배치 경사 하강법(Mini-batch GD)
print('3) 미니 배치 경사 하강법 -----')
theta3 = [1, 1]
step = 0.001
for epoch in range(3000):
    mini_batches = minibatches(dataset, 20, True)
    for batch in mini_batches:
        gradients = [linear_gradient(x, y, theta3) for x, y in dataset]
        gradient = vector_mean(gradients)
        theta3 = gradient_step(theta3, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch+1}: {theta3}')
mini_batch_theta = theta3
print('mini_batch_theta = ', mini_batch_theta)

# 5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인


def stochastic_function(x):
    result = []
    for i, j in stochastic_theta:
        result.append(i*x + j)
    return result


def batch_function(x):
    result = []
    for i, j in batch_theta:
        result.append(i*x + j)
    return result


def mini_batch_function(x):
    result = []
    for i, j in mini_batch_theta:
        result.append(i*x + j)
    return result
s_y = stochastic_function(displ)
b_y = batch_function(displ)
m_y = mini_batch_function(displ)

plt.plot(displ, s_y)
plt.plot(displ, b_y)
plt.plot(displ, m_y)

plt.scatter(dataset[0], dataset[1])
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

>>>>>>> b698240d953ddbe567f907dd4d5e2692599f16a2
