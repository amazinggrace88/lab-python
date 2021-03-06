'''
베이즈 정리(Bayes's Theorem)

: 사건 F가 발생했다는 가정 하에 사건 E가 발생할 확률을 활용하여 사건 E가 발생할 확률을 구하는 과정
    사후확률을 활용하여 사전확률을 구한다.
P(A|B) = P(A,B)/P(B)
       = P(B,A)/P(B)
       = P(B|A)P(A)/P(B)
       = P(B|A)P(A)/( P(A,B) + P(B, ~A) ) *전체 사건이 A와 ~A로만 이루어졌을 경우에 전개 가능

10，000명 중에 1 명이 걸리는 질병(Disease):
    P(D) = 1/10000 = 0.01% = 0.0001
    P(~D) = 1 - P(D) = 9999/10000 = 99.99% = 0.9999

질병이 있는 경우 '양성', 질병이 없는 경우 '음성'이라고 판단하는 검사의 정확도 99%
    질병이 있는 경우에 양성인 경우
    P(T|D) = 99/100 = 99%
    질병에 걸리지 않는 사람을 양성이라고 한 경우
    P(T|~D) = 1/100 = 1%

양성 판정인 경우 실제로 병에 걸렸을 확률
    P(D|T) = P(T|D)P(D) / [P(T|D)P(D) + P(T|~D)P(~D)]
           =  0.99*0.0001 / [0.99*0.0001 + 0.01*0.9999]
           =  0.98%
why?
    P(D|T) = P(D,T)/P(T)
           = P(T|D)P(D)/P(T)
           = P(T|D)P(D)/[P(T|D)P(D) + P(T|~D)P(~D)]
'''
print(0.99*0.0001 / (0.99 * 0.0001 + 0.01 * 0.9999))  # 0.0098

'''
확률변수(random variable)
'''
range(10)  # 0~9까지 모든 변수


