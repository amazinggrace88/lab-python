'''
gradient descent 연습
'''
# import matplotlib.pyplot as plt
from lab_python.scratch08.ex01 import difference_quotient, tangent, move, plt  # plt ex01(패키지가 아닌 다른 파일)에서도 가지고 올 수 있음
# import 모듈 -> 모든 파일내용  run

def g(x):
    """y = (1/3)x**3 - x"""
    return x**3 / 3 - x


if __name__ == '__main__':
    # 함수 g(x)의 그래프를 그림
    # 3차 함수 -> 최소/최댓값 없다 즉, 범위가 주어져야 한다. (a <= x <= b)
    # 범위가 주어졌을 때, 최소/최대를 찾자.
    # 최소 - / 최대 +
    xs = [x / 10 for x in range(-10, 11)]
    ys = [g(x) for x in xs]
    init_x = 2
    tolerance = 0.0000001
    count = 0

    # 최솟값 찾기
    while True:
        count += 1
        # init_x, g(init_x)값의 기울기를 찾는다
        gradient = difference_quotient(g, init_x, h=0.01)
        # tangent_estimate = [tangent(x, gradient, init_x, g(init_x)) for x in xs]
        # plt.plot(xs, tangent_estimate, label=f'x = {init_x}')
        # x 좌표 이동: 최솟값을 찾기 위해 기울기 반대 방향으로 움직임
        next_x = move(init_x, gradient, step=-0.2)
        # 이동 전후 x 좌표 사이의 거리가 임계값보다 작으면 반복을 종료
        print(f'{count}: x = {next_x}')
        if abs(next_x - init_x) < tolerance:
            break
        else:
            init_x = next_x

    print()
    print('=========================================================================')
    init_x2 = -2
    count = 0
    while True:
        count += 1
        gradient = difference_quotient(g, init_x2, h=0.001)
        # tangent_estimate = [tangent(x, gradient, init_x2, g(init_x2)) for x in xs]
        # plt.plot(xs, tangent_estimate, label=f'x = {init_x2}')
        next_x = move(init_x2, gradient, step=0.1)
        print(f'{count}: x = {next_x}')
        if abs(next_x - init_x2) < tolerance:
            break
        else:
            init_x2 = next_x

    # 오쌤 정답
    # ex01에서 작성한 함수들을 이용
    # 함수 g(X)의 그래프를 그림
    xs = [x / 10 for x in range(-30, 31)]
    ys = [g(x) for x in xs]
    plt.plot(xs, ys)
    plt.axhline(y=0, color='0.3')
    plt.axvline(x=0, color='0.3')
    plt.axvline(x=-1, color='0.75')
    plt.axvline(x=1, color='0.75')
    plt.ylim(bottom=-2, top=2)
    plt.title('y = x**3 / 3 - x')
    plt.show()
