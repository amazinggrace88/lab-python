# coding=utf-8
# 외울 것
import numpy as np

scores = []
for i in range(10):
    x = np.random.randint(0, 101)
    scores.append(x)
print(scores)
# list comprehension
scores_c = [np.random.randint(0, 101) for _ in range(10)]
print(scores_c)

total = 0
for score in scores:
    total += score
print(total)










# ctrl + R : Run!

