"""
decision tree
"""
import math
from collections import Counter, defaultdict
import numpy as np
from typing import NamedTuple, Any
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


# 데이터 타입을 먼저 지정해준다
class Leaf(NamedTuple):  # NamedTuple 을 상속받는 클래스
    value: Any  # 어떤 타입이든 올 수 있다는 뜻, 합격 불합격 저장 용도로 사용


class Split(NamedTuple):
    # 무엇으로 가지를 치는지 attribute 이름이 있어야 해요
    attribute: str  # 트리에서 가지(branch)가 나눠지는 기준 : key 값은 무조건 문자열 ex_level
    subtree: dict  # 중간에 있는 tree (ex_senior 의 subtree)
    

# predict 함수
def predict(model, sample):
    """sample을 model(의사결정나무)에 적용했을 때, 예측 결과를 리턴"""
    # 기본원리 : leaf type 이 들어오면 우리가 예측을 멈춘다!
    if isinstance(model, Leaf):
        # model 이 최종 노드인 Leaf 타입이면, Leaf 가 가지고 있는 value (값) 을 리턴
        return model.value

    # model이 아닌 경우에는 가지를 따라 내려가야 하기 때문에
    # sample(ex_candidate) 이 attribute(ex_level) 로 가지고 있는 값을 찾아서, 해당 가지로 내려감
    subtree_key = getattr(sample, model.attribute)  # sample 의 attribute 의 값을 찾는다.
    # ex_model.attribute 가 level 이라면 sample 의 값인 ex_'Senior' 값이 나온다.
    print('subtree_key : ', subtree_key)

    # model 이 가지고 있는 subtree (ex_'Senior'라는 subtree 로 다시 간다)
    subtree = model.subtree[subtree_key]
    return predict(subtree, sample)  # 재귀함수 : (ex_ Senior)


def build_tree(dataset, by_splits, target):
    print('\n>> building tree.. ')
    print(f'dataset len : {len(dataset)} = {dataset}')
    print(f'by_split : {by_splits}, target : {target}')
    # dataset (data), by_splits (tree 나누는 기준), target(결과)
    
    # target 의 갯수를 셈 by Counter 객체 생성 Counter : {True: x, False: y}
    target_counts = Counter(getattr(sample, target)
                            for sample in dataset)  # 리스트로 만들어진 True, False 갯수를 센다. (counter 객체 dict 타입 리턴)
    print('target_counts : ', target_counts)  # dict 에서는 key:value 가 1개의 data, 그래서 dict 의 length 는 2
    
    # Counter 의 length 가 1개이면
    # leaf 가 될 수 있는 상태란? target 갯수, 즉 Counter 의 length 가 1개인 상태 - Leaf 생성하고 종료
    if len(target_counts) == 1:
        keys = list(target_counts.keys())
        # = [k for k in target_counts.keys()] -> [] 연산자 사용 불가.. why? keys() 는 generator 객체이므로,,
        # target_counts.keys() generator (반복문 안에서 리스트를 만들어주는 객체)이므로 리스트를 먼저 만들어 주어야 함 -> 리스트 함수 쓰면 됨
        result = keys[0]
        leaf = Leaf(result)
        print('leaf : ', leaf)
        return leaf

    # tree 의 depth 가 깊어져서 더이상 서브 트리를 나눌 기준이 없을 때 (ex_ 4가지 기준 모두 씀)
    # by_splits = []일때, 원소가 없으면 False
    # if len(by_splits) == 0:
    if not by_splits:
        return Leaf(list(target_counts.keys())[0])  # leaf node 를 무조건 리턴

    # Counter 의 length 가 1이 아니면, 파티션을 나눌 수 있음.
    # by_splits(가지 나누는 기준)의 각 변수로 파티션을 나눔.
    # 각 파티션별 엔트로피(level 로 나눴을 때 엔트로피.. )를 계산해서 가장 낮은 엔트로피 변수를 선택
    # best_splilter = min(by_splits, key=partition_entropy_by())
    # partition_entropy_by()를 key= 에 바로 못쓰는 이유
    # 파라미터 1개밖에 못주기 때문, by_splits 는 key 의 함수(dataset, ..)에 파라미터로 주는데, partition_entropy_by()는 파라미터 3개이다.
    # (ex_ sorted(list, key=lambda x: len(x)) # 리스트의 문자열 1개가 x가 되어서 글자 수 세고 글자수 기준으로 정렬 - 파라미터 1개만 된다)
    # 어디다 넣어야 할 지 알려주기 위해서 partition_entropy_by()를 호출할 수 있는 wrapper 함수(helper 함수)를 작성

    # wrapper 함수(helper 함수)
    # 내부함수(자신의 바깥쪽에 선언된 변수를 모두 가져다 쓸 수 있다 - ??? ctrl + 클릭으로 확인)
    def splitted_entropy(split_attr):
        print('split_attr = ', split_attr)
        # 파라미터 3개 중 1개를 딱 정해준다.(split_attr) / build_tree 의 파라미터 dataset, target 이 자동으로 파라미터로 들어간다 - ???)
        result = partition_entropy_by(dataset, split_attr, target)
        print('splitted entropy = ', result)
        return result

    best_splilter = min(by_splits, key=splitted_entropy)
    print('best_spliter : ', best_splilter)

    # 선택된 변수(entropy 최솟값을 주는 변수)로 Split 객체를 생성 - 첫번째 가지를 치자!
    partitions = partition_by(dataset, best_splilter)
    print('partitions : ', partitions)

    # partition 을 만든 이유 : 나눠준 candidate 들을 key 값(ex_level)의 value 들을 부분집합으로 만들어주기 위해서!
    # 각 부분집합들은 또다른 가지의 dataset 이 된다.
    # 선택한 변수를 제외한 나머지 변수들로 sub tree 를 만듬
    # branch 기준 리스트에서 선택된 변수 제거
    new_split = [x for x in by_splits
                 if x != best_splilter]  # best_spliter 와 다른 새로운 split 기준 리스트 생성
    print(f'제거 후 by_splits : {by_splits}, new_splits : {new_split}')

    # subtree 생성
    subtree = {k: build_tree(subset, new_split, target)  # 재귀함수로 가지 밑 다른 트리를 만듬 *by_splits 전의 변수 없어진 상태
               for k, subset in partitions.items()}
    # 해석 : {'Senior' - key ! : [Candidate(level='Senior', ..), ...- value 는 원소 5개짜리 부분집합

    # Split 객체를 생성하여 리턴
    return Split(best_splilter, subtree)

# leaf 하고 나서 다시 올라가는데 왜 올라가지? 다시 올라가서 재귀함수인가?
# 같은 depth 에서는 같은 기준으로 나누게 하기 위하여 new_split 을 써야 한다. (근데 다시 올라가는 거 모르겠음)


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
    [[False, False, False, True, True], [True, True, True, True], [True, True, False, True, False]] : 파티션
    Counter({False: 3, True: 2}) : 1번의 FALSE 3, 3 엔트로피 계산 * 비율 곱하여 더한다.
    Counter({True: 4})           : 2번의 TRUE 4  
    Counter({True: 3, False: 2}) : 3번의
    entropy partitioned by level : 0.6935361388961919
    
    [[False, False, True], [True, True, False, True, True, True, False], [True, False, True, True]]
    Counter({False: 2, True: 1})
    Counter({True: 5, False: 2}) : 확실성 더 높다. 엔트로피 더 낮다.
    Counter({True: 3, False: 1})
    entropy partitioned by lang : 0.8601317128547441  불확실성이 더 많아 전체 엔트로피 더 커질 수 밖에 없다.
      
    [[False, False, True, True, False, True, False], [True, False, True, True, True, True, True]]
    Counter({False: 4, True: 3}) : 불확실성 크다
    Counter({True: 6, False: 1}) : 불확실성 상대적으로 적다
    entropy partitioned by tweets : 0.7884504573082896
    
    [[False, True, True, True, False, True, True, True], [False, False, True, True, True, False]]
    Counter({True: 6, False: 2})
    Counter({False: 3, True: 3})
    entropy partitioned by phd : 0.8921589282623617  --> 박사학위가 엔트로피가 제일 크다.
    """

    # test - 자료구조를 만들고 있다!
    hire_tree = Split(
        'level',                                          # branch 나누는 기준 : root node
        {
            'Senior': Split(                              # 첫번째 가지
                'tweet',
                {True: Leaf(True), False: Leaf(False)}),  # subtree
            'Mid': Leaf(True),  # 전부 합격인 leaf 노드
            'Junior': Split(
                 'phd',
                 {True: Leaf(False), False: Leaf(True)})
        }
    )

    # 두번째 그림도 만들어보기 (노트 필기)

    # predict test
    print(hire_tree)
    candidate_1 = Candidate('Senior', 'Java', False, False, False)
    result = predict(hire_tree, candidate_1)
    print(result)

    candidate_2 = Candidate('Mid', 'Python', False, False, True)
    result = predict(hire_tree, candidate_2)
    print(result)

    # built tree 함수 테스트
    tree = build_tree(candidates, ['level', 'lang', 'tweet', 'phd'], 'result')
    print(tree)  # 최소 엔트로피로 이루어진 tree 를 출력한다.

    # pip install graphviz
    