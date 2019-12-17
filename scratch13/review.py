import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 다항회귀 - DIS
datasets = load_boston()
np.random.seed(1217)
X = datasets.data
y = datasets.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train_dis = X_train[:, np.newaxis, 7]
X_test_dis = X_test[:, np.newaxis, 7]
lin_reg = LinearRegression()
poly = PolynomialFeatures(include_bias=False)
X_train_dis_poly = poly.fit_transform(X_train_dis)
X_test_dis_poly = poly.fit_transform(X_test_dis)
lin_reg.fit(X_train_dis_poly, y_train)
print(f'intercept : {lin_reg.intercept_}, coefficient : {lin_reg.coef_}')
y_pred_dis_poly = lin_reg.predict(X_test_dis_poly)

plt.scatter(X_test_dis, y_test)
xs = np.linspace(X_test_dis.min(), X_test_dis.max(), 100).reshape((100, 1))
xs_poly = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')
plt.show()
# goooooooooooooooooooooooooooooooooooooooooooooooooood~~~~~~~~~~~~~~~~~~~~~~~~~~~~
