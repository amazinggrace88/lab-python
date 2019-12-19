'''
matplotlib.pyplot 모듈을 사용한 데이터 시각화 - 선 그래프
(교재 제 3장 데이터 시각화)

like r ggplot

'''
import matplotlib.pyplot as plt



# 선 그래프(line chart)
x = [i for i in range(10)]
print(x)

y1 = [2 ** x for x in range(10)]
print(y1)
plt.plot(x, y1, 'go--', label = 'example1')  # x축의 scale과 y축의 scale이 같지 않지만, plt.plot이 자동 조정해준다.
# r: red + : 점선 => ctrl+q 해서 문서에서 찾아보고 조합한다.
# go-- : 선 green , o 마커, -- dashed line style
# 여러개 선 그래프 만들기 -> plt.show() 하기 전까지 여러가지의 plt.plot을 둔다.
y2 = [2 ** x for x in range(9, -1, -1)]
print(y2)
plt.plot(x, y2, 'r--', label = 'example2')
# vector 합 using list comprehension
y3 = [x + y for x, y in zip(y1, y2)] # 중요*****list2개를 zip하여 dict를 만들기도 함.
print(y3)
plt.plot(x, y3, 'b:', label = 'example3')
plt.legend(loc = 'best') # 범례 #  **kwargs : 파라미터 여러개 쓸 수 있다.
plt.title('Line Chart Example')
plt.show()
# plot 에 쓸 수 있는 #색깔의 의미
# RGB : #00(R)80(G)00(B) 가 16진수로 0부터 16까지 표현된다. (16진수 : 2^16 = 256가지 만들 수 있는 수)
# RGBA tuples ((0,1,0,1)) : 0.0~ 1.0까지의 정도로 R, G, B 선택, 마지막 1은 투명도

