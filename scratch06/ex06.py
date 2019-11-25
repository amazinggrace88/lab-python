'''
연속확률분포
    1) 확률밀도함수 (Probability Density Function : PDF)
    : f(x)
    : f(x)={\frac  {d}{dx}}F(x)
    : p(a <= x < b) = integral from a to b [pdf(x)dx]
    
    2) 누적분포함수 (Cumulative Destribution Function : CDF)
    : \int_{a}^{b}f(x)dx
    : F(x)=\int _{{-\infty }}^{x}f(x)dx
    : cdf(x) = P(x <= b)
    (확률밀도함수의 적분값이 누적분포함수)
    : p(a <= x < b) = F(b) - F(a)


간단한 실습
1. 균등분포 그래프로 나타내기
2. 정규분포 그래프로 나타내기
* Scipy 패키지를 사용하여서도 구현해보기
'''
import math
from matplotlib import pyplot as plt


# 1. 균등분포 그래프로 나타내기
# 균등분포의 확률밀도함수(Probability Density Function)
def uniform_pdf(x):
    return 1 if 0 <= x < 1 else 0


# 균등분포의 누적분포함수(Cumulative Distribution Function)
def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


# 2. 정규분포 그래프로 나타내기
# 정규분포의 확률밀도함수(Probability Density Function)
def normal_pdf(x, mu=0.0, sigma=1.0):
    """평균이 mu이고, 표준편차가 sigma인 정규분포의 확률 밀도 함수"""
    sqrt_two_pi = math.sqrt(2 * math.pi)  # sqrt(2 * 3.14(pi))
    return (math.exp(-(x-mu)**2/ 2/ sigma ** 2) / (sqrt_two_pi * sigma))


# 정규분포의 누적확률변수(Cumulative Distribution Function)
def normal_cdf(x, mu=0.0, sigma=1.0):
    """
    평균이 mu이고, 표준편차가 sigma인 정규분포의 누적 확률 변수
    math.erf() 함수(error function-오차함수 : 정규분포의 누적분포함수와 같으며 초월함수)를 이용하여 구현
    """
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2


# 누적확률을 알고 있을 때, 확률변수를 찾아라 percentile!
# 역함수를 이용하자.
# ex : y = 2^x <-> x = {\log_2 y}

# process
# z-score 표준화 : z = (x - mu) / sigma
# x = sigma * z + mu
# 표준정규확률변수의 cdf로 만들고, percentile에 따른 x 값을 구한다.
# 이진 정렬 알고리즘 -> 중간에 있는 값의 확률이 우리가 찾으려고 하는 확률보다 큰지 작은지 보고, 범위를 좁혀서
# 다시 그 중간에 있는 값의 확률이 우리가 찾으려고 하는 확률보다 큰지 작은지 본다.
#  tolerance=0.00001 : 소수점 5번째까지 일치했다면, 일치했다고 판단한다.

def inverse_normal_cdf(p, mu=0.0, sigma=1.0, tolerance=0.00001):
    """누적확률 p를 알고 있을 때, 정규 분포 확률 변수 x 를 찾는다"""
    # 표준 정규 분포가 아니라면 표준 정규 분포로 변환
    if mu != 0.0 or sigma !=1.0:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)  # 재귀함수
    low_z, low_p = -10.0, 0  # 누적확률이 0이 되는 값이 -10.0이다.
    high_z, high_p = 10.0, 1  # 누적확률이 1이 되는 값이 10.0이다.
    while high_z - low_z > tolerance:  # 범위를 계속 좁혀나갈 것
        mid_z = (low_z + high_z) / 2.0  # 중간 값을 찾으면서
        mid_p = normal_cdf(mid_z)  # 중간값의 누적분포 값을 계산한다.
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            high_z, high_p = mid_z, mid_p
        else:
            break
    return mid_z


def inverse_normal_cdf(p, mu=0.0, sigma=1.0, tolerance=0.00001):
    """누적확률 p를 알고 있을 때, 정규 분포 확률 변수 x 를 찾는다"""
    # 표준 정규 분포가 아니라면 표준 정규 분포로 변환
    if mu != 0.0 or sigma !=1.0:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)  # 재귀함수
    low_z, low_p = -10.0, 0  # 누적확률이 0이 되는 값이 -10.0이다.
    high_z, high_p = 10.0, 1  # 누적확률이 1이 되는 값이 10.0이다.
    while high_z - low_z > tolerance:  # 범위를 계속 좁혀나갈 것
        mid_z = (low_z + high_z) / 2.0  # 중간 값을 찾으면서
        mid_p = normal_cdf(mid_z)  # 중간값의 누적분포 값을 계산한다.
        if mid_p < p:
            low_z = mid_z
        else:
            high_z = mid_z
    return mid_z

# 이산 quentile함수와 유사한 개념이지만, 연속에서는 모든 확률변수가 연속이므로 이진 정렬 알고리즘을 사용하여 x를 구한다.
# binary search - 이진 정렬 알고리즘 - 스무고개 게임과 같은 논리로 작동한다.




if __name__ == '__main__':
    xs = [x/10 for x in range(-50, 51)]  # -5<= x <= 5 구간을 0.1씩 나눔
    print(xs)  # 균일분포의 범위(x값)
    ys = [uniform_pdf(x) for x in xs]  # 확률밀도함수 계산
    plt.plot(xs, ys)
    plt.title('Uniform Distribution PDF')
    plt.show()

    ys_cdf = [uniform_cdf(x) for x in xs]  # 누적분포함수 계산
    plt.plot(xs, ys_cdf)
    plt.title('Uniform Distribution CDF')
    plt.show()

    # 정규분포의 확률밀도함수 계산(평균/표준편차 상이하게 그래프 출력)
    ys_norm_pdf = [normal_pdf(x) for x in xs]
    # mu(평균) = 0.0 sigma(표준편차) = 1.0
    plt.plot(xs, ys_norm_pdf, '-', label = 'mu=0, sigma=1')

    ys_norm_pdf_custom = [normal_pdf(x, 0, 2) for x in xs]
    plt.plot(xs, ys_norm_pdf_custom, '--', label = 'mu=0, sigma=2')

    ys_norm_pdf_custom2 = [normal_pdf(x, 0, 0.5) for x in xs]
    plt.plot(xs, ys_norm_pdf_custom2, ':', label = 'mu=0, sigma=0.5')

    ys_norm_pdf_custom3 = [normal_pdf(x, -1.0) for x in xs]
    plt.plot(xs, ys_norm_pdf_custom3, '-.', label = 'mu=-1, sigma=1')

    plt.title('Normal Distribution PDF')
    plt.legend()
    plt.show()

    # 정규분포의 누적분포함수 오차함수를 이용하여 구현
    ys_norm_cdf = [normal_cdf(x) for x in xs]
    plt.plot(xs, ys_norm_cdf, '-', label = 'mu=0, sigma=1')

    ys_norm_cdf_custom = [normal_cdf(x, 0, 2) for x in xs]
    plt.plot(xs, ys_norm_cdf_custom, '--', label = 'mu=0, sigma=2')

    ys_norm_cdf_custom2 = [normal_cdf(x, 0, 0.5) for x in xs]
    plt.plot(xs, ys_norm_cdf_custom2, ':', label = 'mu=0, sigma=0.5')

    ys_norm_cdf_custom3 = [normal_cdf(x, -1, 1) for x in xs]
    plt.plot(xs, ys_norm_cdf_custom3, '-.', label = 'mu=-1, sigma=1')
    plt.legend()
    plt.title('Normal Distribution CDF')
    plt.show()

    # 누적 확률이 0.9, 0.99, 0.999 인 확률변수 x를 찾음
    # 표준 정규 분포표와 비교
    random_variable_x = inverse_normal_cdf(0.95)
    print('95th percentile = ', random_variable_x)
    # 95th percentile =  1.6448497772216797
    random_variable_x_1 = inverse_normal_cdf(0.94)
    print('94th percentile = ', random_variable_x_1)
    # 94th percentile =  1.5547657012939453
