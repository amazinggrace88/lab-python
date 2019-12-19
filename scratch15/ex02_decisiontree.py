"""
decision tree
"""
import math
from collections import Counter, defaultdict
import numpy as np
from typing import NamedTuple
import matplotlib.pyplot as plt


# NamedTuple 을 상속받는 클래스 선언
class Candidate(NamedTuple):
    level: str
    lang: str
    tweet: bool
    phd: bool
    result: bool = None  # 기본값 쓸 수 있다! (클래스 선언 방식의 장점!)


def uncertainty(p):
    """
    엔트로피 : 불확실성의 정도 0 < p <= 1
    확률 p=0이면, 사건이 항상 발생하지 않는다라고 확신 -> 불확실성 0
    확률 p=1이면, 사건이 항상 발생한다고 확신 -> 불확실성 1
    확률 0 < p < 1이면, 사건이 발생할 수도, 발생하지 않을 수도 있다 -> 불확실성이 있다.
     """
    # math.log(p, base=2) -> log_2 가 밑수
    # 1보다 작은 로그는 음수에 -을 붙여서 양수로 만든다
    return -p * math.log(p, 2)


def entropy(class_probabilities):
    """
    주어진 확률들의 리스트에 대해서 엔트로피를 계산
    E = sum(i) [uncertainty(p_i)] = -p_1 * log(p_1) - p_2 * log(p_2) * ... 
    E = 모든 경우에 대한 불확실성 = 각 사건에 대한 불확실성 + 각 사건에 대한 불확실성 + ...
    가장 불확실성이 큰 경우 : 50%, 50% -> 엔트로피 max (최댓값)
    """
    ent = 0
    for p in class_probabilities:
        if p != 0:
            ent += uncertainty(p)
            # 만약 p=0이면 log(p)를 계산할 때 Error 가 발생
        # 더하지 않는 건, 더하기 0과 같으므로, else 부분은 없어도 되~
    return ent


def binary_entropy(p):
    """사건이 두 가지인 경우, 사건이 일어날 확률 p, 사건이 일어나지 않을 확률 1-p
    두가지만 더하면 된다"""
    return uncertainty(p) + uncertainty(1-p)


def class_probabilities(labels):
    """"""
    total_count = len(labels)
    counts = Counter(labels)  # 갯수, {label1: x개, label2: y개.. } -> dict 와 비슷
    print(counts)
    probabilities = []
    for count in counts.values():
        p = count / total_count  # 각 레이블의 확률
        probabilities.append(p)
    return probabilities
#
# def class_probabilities(labels):
#     total_count = len(labels)
#     counts = Counter(labels)  # 갯수, {label1: x개, label2: y개.. } -> dict 와 비슷
#     print(counts)
#     pass


def partition_by(dataset, attr_name):
    """NamedTuple 들의 리스트로 이루어진 dataset 을 NamedTuple 의 특정 attribute 로 partitioning"""
    # list 를 value 로 갖는 dict 만듬
    # 전체적 흐름 : 지원자 1 row 가 senior 그룹에 들어감. (맞다면), 아니면 그룹 만들어 들어감
    partitions = defaultdict(list)
    for sample in dataset:
        # 지원자 1 row 추출
        # sample.attr_name 은 글자 그대로 인식함
        # sample 의 getattr 함수에 지정된 attr_name(ex_level) 으로 준다. defaultdict 의 key 로 준다.
        key = getattr(sample, attr_name)
        # dict 의 키로 사용하여 sample 을 value 에 저장(새로 생성)
        partitions[key].append(sample)
    return partitions

# defaultdict : dictionary 에 기본값을 정의하고, 키값이 없더라도 에러를 출력하지 않고 기본값을 출력한다.


def partition_entropy_by(dataset, by_partition, by_entropy):
    """
    attr_name 으로 분리된 각 파티션에서 label_name 의 엔트로피를 각각 계산하고, 파티션 내에서의 엔트로피 * 파티션의 비율들의 합을 리턴
    dataset : 데이터 전체
    by_partition : patitioning 을 나눌 컬럼명(특성)
    by_entropy : 합격 불합격 결과(엔트로피를 계산할 컬럼명)

    과정
    : attr_name 이 예를 들어 level 일 때, level 이 Junior 일 때, 합격할 확률의 엔트로피를 구한다.
    level 이 mid 일 때, 합격할 확률의 엔트로피를 구한다.
    level 이 Senior 일 때, 합격할 확률의 엔트로피를 구한다.
    """
    # partition 을 나눔
    partitions = partition_by(dataset, by_partition)
    # label(class) 별 확률을 계산하기 위해서 각 label 들의 리스트 만들기
    labels = []
    for partition in partitions.values():  # partition 갯수 만큼 반복
        values = []
        for sample in partition:  # 부분집합인 partition 안의 sample 들(candidate)의 갯수 - 원소 1개 만큼 반복
            values.append(getattr(sample, by_entropy))
        labels.append(values)  # [Junior 의 T, F, T, F], [Senior 의 T, F, T, F]..
    print(labels)  # [[t,f,t,f], [..], [..] ..] 위의 리스트를 모아 하나의 리스트로!
    # 각 파티션이 차지하는 비율을 계산하고, 각 파티션에서의 엔트로피에 그 비율을 곱해주기 위해서
    total_count = sum(len(label) for label in labels)
    # 함수 안에도 for 문 쓸 수 있음
    # labels 은 리스트를 3개 가지고 있음, 실제로는 5 + 5 + 5 = 15개이다. 
    # 따라서 for 문 :  [[t,f,t,f], [..], [..] ..] 안의 [t,f,t,f] 에서의 label 의 갯수 계산
    ent = 0
    for label in labels:
        # 파티션이 가지고 있는 [t,f,t,f] 에서 확률 계산 (ex_P(t) = 1/2, P(f) = 1/2)
        cls_prob = class_probabilities(label)  # 파티션의 엔트로피 계산
        part_ent = entropy(cls_prob)
        ent += part_ent * len(label) / total_count  # 파티션 내에서의 엔트로피 * 파티션의 비율들의 합
    return ent


if __name__ == '__main__':
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]


# decision tree = 스무고개
# 첫 질문이 제일 중요하다! (확률적 - 엔트로피 개념 파악하기)
# 질문 순서에 따라 decision tree 갯수 엄청 많아져~
# 그런데 트리 크기가 짧은게 꼭 좋은 건 아니다 -> 다른 데이터에 예측력이 떨어질 수 있다.

    # 엔트로피 : 질문을 선택하는 기준
    # uncertainty 함수 그래프
    x_pts = np.linspace(0.0001, 0.9999, 100)  # 시작값, 끝값, 그사이를 나누는 값
    y_pts = [uncertainty(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.xlim(0.0)  # 0 <= x 그 밑은 그리지 않는다.
    plt.ylim(0.0)  # 0 <= y 그 밑은 그리지 않는다.
    plt.title('-p * log(p)')
    plt.show()
    # 해석
    # 엔트로피는 불확실성! https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node56.html
    # 확률 1 = 모두 발생하는 경우, 불확실성이 없다. 확실하게 정해져 있으므로
    # 확률 0 = 발생하지 않는 경우, 불확실성이 없다. 확실하게 정해져 있으므로

    # binary entropy graph
    x_pts = np.linspace(0.0001, 0.9999, 100)
    y_pts = [binary_entropy(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.xlim(0)
    plt.axvline(0.5)
    plt.ylim(0)
    plt.show()
    # 0.5 일때 가장 불확실성이 커진다. 소금물100% + 맹물 100% = 50%, 50%으로 불확실성이 가장 커지는 방향으로 변화한다.

    # entropy 함수 테스트
    # 확률 1개, p=1
    rain_prob = [1]  # 내일 비올확률 1 (확률 1개)
    ent = entropy(rain_prob)
    print('entropy = ', ent)  # binary entropy 의 그래프의 최솟값 0

    # 확률 2개, p1=0.5, p2=0.5 (p1+p2=1)
    rain_prob = [0.5, 0.5]
    ent = entropy(rain_prob)
    print('entropy = ', ent)  # binary entropy 의 그래프의 최댓값 1

    # 확률 2개, p1=0.9, p2=0.1 (p1+p2=1) 비가 올 확률 90%
    rain_prob = [0.9, 0.1]
    ent = entropy(rain_prob)
    print('entropy = ', ent)  # entropy 0.47

# decision tree = 스무고개에서의 엔트로피 활용
# E(level), E(lang), E(mid) .. 계산 -> 엔트로피가 가장 낮은 질문을 첫번째로 삼는다. 
# 2번째 질문 -> partitioning group 1 을 다시 partitioning 하여 엔트로피를 계산한다.

    # class_probabilities 함수 테스트
    level = ['junior', 'senior', 'mid', 'junior']
    cls_prob = class_probabilities(level)
    print(cls_prob)

    # 실전!
    # 전체 집합을 나누는 기준(Partitioning) 에 따라 엔트로피가 달라질 수 있다.
    # 함수 만듬
    partition_by_level = partition_by(candidates, 'level')
    print('partitioning by level: \n', partition_by_level)
    partition_by_tweets = partition_by(candidates, 'tweet')
    print('partitioning by tweets: \n', partition_by_tweets)

    # partition entropy by 함수 테스트
    # 전체 지원자들을 level 로 partition 을 나눠서 result 의 엔트로피를 계산하자~
    ent_level = partition_entropy_by(candidates, 'level', 'result')
    print(f'entropy partitioned by level : {ent_level}')
    # 결과 : [[False, False, True, True, True], [True, True, True, True], [True, True, False, True, False]]
    ent_lang = partition_entropy_by(candidates, 'lang', 'result')
    print(f'entropy partitioned by lang : {ent_lang}')
    ent_tweets = partition_entropy_by(candidates, 'tweet', 'result')
    print(f'entropy partitioned by tweets : {ent_tweets}')
    ent_phd = partition_entropy_by(candidates, 'phd', 'result')
    print(f'entropy partitioned by phd : {ent_phd}')

    """ 결과 해석 - 불확실성이 적은 질문을 먼저 던지는 것이 좋다. 즉 엔트로피가 가장 적은 것부터 트리를 그리자.
    [[False, False, False, True, True], [True, True, True, True], [True, True, False, True, False]]
    Counter({False: 3, True: 2}) 1번 의 FALSE 3, 3
    Counter({True: 4})
    Counter({True: 3, False: 2})
    entropy partitioned by level : 0.6935361388961919
    
    [[False, False, True], [True, True, False, True, True, True, False], [True, False, True, True]]
    Counter({False: 2, True: 1})
    Counter({True: 5, False: 2})  확실성 더 높다. 엔트로피 더 낮다.
    Counter({True: 3, False: 1})
    entropy partitioned by lang : 0.8601317128547441  
      
    [[False, False, True, True, False, True, False], [True, False, True, True, True, True, True]]
    Counter({False: 4, True: 3})
    Counter({True: 6, False: 1})
    entropy partitioned by tweets : 0.7884504573082896
    
    [[False, True, True, True, False, True, True, True], [False, False, True, True, True, False]]
    Counter({True: 6, False: 2})
    Counter({False: 3, True: 3})
    entropy partitioned by phd : 0.8921589282623617  --> 박사학위가 엔트로피가 제일 크다.
    """
