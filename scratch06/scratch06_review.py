import random
from collections import Counter

dice = [1, 2, 3, 4, 5, 6]
trials = 10_000


def experiment(type, n, t):
    """
    실험의 결과를 [ [ [], [], [] ],/  [ [], [], [] ],/  [ [], [], [] ] ]

    :param type: 실험 타입(동전던지기 or 주사위 던지기, ..)
    :param n: 실험의 개수
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t):  # 실험 횟수만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 실험 갯수만큼 반복
            rand = random.choice(type)  # H or T
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 저장
        cases.append(tuple(case))
    return cases


dice_exp = experiment(dice, 2, 10_000)

dice_event_counts = Counter(dice_exp)

for _ in range(trials):
    num_of_sums_even = 0
    for key, value in dice_event_counts.items():
        if (key[0] % 2 == 0) or (key[1] % 2 == 0):
            num_of_sums_even += value

print('주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 = ', (num_of_sums_even) / trials)