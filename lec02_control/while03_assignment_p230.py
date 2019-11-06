'''
assignment python programming manual - p.230
'''

# 중첩 for 루프를 사용해 문자 t로 채워진 직각 삼각형을 화면에 출력하세요. 이 삼각형은 가장 좁은 지점에서는 문자 하나로, 가장 넓은 지점에서는 문자 7개로 표현됩니다.
for i in range(8):
    print('t'*i)

# 중첩 for 루프를 사용해 13번에서 설명했던 삼각형을 빗변이 왼쪽에 있도록 화면에 출력하세요.
for i in range(8):
    print(' '*(7-i), 't'*i)

# 위 두 문제를 while 문을 사용해서 다시 풀어보세요.
# 1
i = 1
while i <= 7:
    print('t' * i)
    i += 1
# 2
i = 1
while i <= 7:
    print(' ' * (7 - i), 't' * i)
    i += 1


# rat_1_weight 와 rat_2_weight 는 실험을 시작할 때 두 생쥐의 몸무게입니다. 변수 rat_1_rate 와 rat_2_rate 는 생쥐들의 몸무게가 매주 얼마씩 증가할지에 대한 예상 비율입니다.
# while 루프를 사용해 첫 번째 생쥐의 몸무게가 처음보다 25% 더 나가려면 몇주가 걸릴 지 계산하세요.
rat_1_weight = 10
rat_2_weight = 10
rat_1_rate = 1.04
rat_2_rate = 1.04
x = 1
while rat_1_weight <= 12.5:
    rat_1_weight = rat_1_weight*(rat_1_rate)**x
    x += 1
print('첫 번째 생쥐의 몸무게가 처음보다 25% 더 나가려면', x, '주가 걸린다.')


# 두 생쥐가 처음에는 같은 몸무게였지만 생쥐 1이 생쥐 2보다 더 빨리 몸무게가 늘어난다고 가정합시다. while 루프를 사용해 생쥐 1이 생쥐 2보다 몸무게가 10% 더 나가려면 몇 주가 걸릴지 예상하세요.
rat_1_weight = 10
rat_2_weight = 10
rat_1_rate = 1.04
rat_2_rate = 1.04
x = 1
while 1:
    rat_1_rate = 0.01 + rat_2_rate
    rat_1_weight = rat_1_weight*(rat_1_rate)**x
    rat_2_weight = rat_2_weight*(rat_2_rate)**x
    if rat_1_weight >= 1.1*rat_2_weight:
        print('생쥐 1이 생쥐 2보다 0.01% 더 빨리 몸무게가 늘어난다고 가정하면, 생쥐 1이 생쥐 2보다 몸무게가 10% 더 나가려면', x, '주가 걸린다.')
        break
    else:
        x += 1
