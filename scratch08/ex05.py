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

