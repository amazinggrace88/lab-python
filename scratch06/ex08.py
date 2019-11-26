'''
scipy.stats 패키지에서 제공하는
확률 밀도 함수(PDF : Probability Density Function),
누적 분포 함수(CDF : Cumulative Distribution Function)
사용하여 6장 확률 구현
'''
import scipy.stats as stats
import matplotlib.pyplot as plt

# 그래프를 그릴 x 구간
xs = [x / 10 for x in range(-30, 31)]


# 균등 분포(Uniform Distribution)의 pdf 그리기 : stats.uniform.pdf
ys1 = [stats.uniform.pdf(x) for x in xs]
plt.plot(xs, ys1, color = 'b', label = 'PDF')


# 균등분포(Uniform Distribution)의 cdf 그리기 : stats.uniform.cdf
ys2 = [stats.uniform.cdf(x) for x in xs]
plt.plot(xs, ys2, color = 'r', label = 'CDF')
plt.legend()
plt.title('Uniform Distribution PDF, CDF')
plt.show()

# 평균 mu = 0이고 표준편차 sigma = 1인 표준정규분포
# 표준정규분포(Standard Normal Distribution)의 pdf 그리기 : stats.norm.pdf
ys1 = [stats.norm.pdf(x) for x in xs]
plt.plot(xs, ys1, color = 'b', label = 'PDF')

# 표준정규분포(Standard Normal Distribution)의 cdf 그리기 : stats.norm.cdf
ys2 = [stats.norm.cdf(x) for x in xs]
plt.plot(xs, ys2, color = 'r', label = 'CDF')
plt.legend()
plt.title('Standard Normal Distribution PDF, CDF')
plt.show()


# https://www.scipy.org/docs.html 에서 doc 확인하여 쓸 것
# https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html scipy.stats

