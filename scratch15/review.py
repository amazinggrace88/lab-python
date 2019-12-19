# NamedTuple -> ? 차이가 뭐지?
# namedTuple -> ? 차이가 뭐지?
import math
from collections import namedtuple, Counter, defaultdict
from typing import NamedTuple

# namedtuple 사용 방법
student = namedtuple('Student', ('no', 'name', 'math', 'science', 'cs'))
class student2(NamedTuple):
    no: int
    name: str
    math: int
    science: int
    cs: int

student = student2(10, 'you', 99, 99, 99)
print(student.name)

# entropy - 불확실성의 정도, E() : 모든 경우에 대한 불확실성이다. 즉, 각 사건에 대한 불확실성의 합이다.
# partitioning 별 entropy 측정
# defaultdict test
d = defaultdict(lambda: 0)
print(d)


def partition_by(dataset, attr_name):
    partitions = defaultdict(list)  # dict 기본값 만듬
    for sample in dataset:  # dataset 에서 sample 1개 꺼냄
        key = getattr(sample, attr_name)
        partitions[key].append(sample)
    return partitions


def class_probabilities(labels):  # class 들의 확률을 구해주는 함수.
    total_count = len(labels)  # 전체 갯수
    counts = Counter(labels)  # collection 의 Counter
    print(counts)
    probabilities = []  # 집어넣을 확률 정하기
    for count in counts.values():  # value 만 빼냈다
        p = count / total_count  # 확률을 구해주었다.
        probabilities.append()  # 각 value의 확률 리스트에 더함
    return probabilities


def uncertainity(p):
    return -p * math.log(p, 2)


def entropy(class_probabilities):
    ent = 0
    for p in class_probabilities:
        if p != 0:
            ent += uncertainity(p)
    return ent


def partition_entropy_by(dataset, by_partition, by_entropy):
    partitions = partition_by(dataset, by_partition)  # partitioning
    labels = []
    for partition in partitions.values():
        values = []
        for sample in partition:
            values.append(getattr(sample, by_entropy))
        labels.append(values)
    print(labels)
    total_count = sum(len(label) for label in labels)
    ent = 0
    for label in labels:
        cls_prob = class_probabilities(label)
        part_ent = entropy(cls_prob)
        ent += part_ent * len(label) / total_count
    return ent


def user_input():
    while True:
        try:
            try:
                n = int(input('1, 2, 3 input your number'))
            except ValueError:
                raise ValueError('no string')
            if n in (1, 2, 3):
                return n
            else:
                raise ValueError('no string')
        except ValueError as e:
            print(e.args)

user = user_input()
print('입력값 =', user)






