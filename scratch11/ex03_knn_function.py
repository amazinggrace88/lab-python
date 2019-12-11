"""
kNN function 만들기
"""
from collections import Counter

import numpy as np


def train_test_split(X, y, test_size):
    """
    index 를 셔플하고 X, y가 같은 데이터를 뽑는 형태
    X: numpy.ndarray - n*m array
    y: numpy.ndarray - 1*n array (n개의 원소) 즉, 원소의 갯수가 n개인 1차원 배열 (1행, n열)
    len(X) == len(y) 가정
    test_size : 0.0~ 1.0 사이의 숫자
    """
    length = len(X)
    # 인덱스를 저장하는 array(배열)
    indices = np.array([i for i in range(length)])  # n 개 (len(n행*m열)=> [[]] => n개)
    print('shuffle 전: ', indices)
    # 인덱스를 임의로 섞음
    np.random.shuffle(indices)
    print('shuffle 후: ', indices)
    # 인덱스를 cut 을 기준으로 나눔
    # cut = train_set 갯수 = 전체 크기 * (1 - test_set 의 size) + int() 소숫점 자르기
    cut = int(length * (1 - test_size))
    X_train = X[indices[:cut]]  # Train set points # X[ [3, 1, 0, 4,..cut] ]
    y_train = y[indices[:cut]]  # Train set labels
    X_test = X[indices[cut:]]  # Test set points
    y_test = y[indices[cut:]]  # Test set labels
    return X_train, X_test, y_train, y_test


class MyScaler:  # init 생략해도 됨, class 의 엠버변수(클래스가 가지고 있는 data 들 = 변수)는 다른 def 에서 사용 가능
    def fit(self, X):
        """X 의 각 특성들의 평균과 표준 편차를 저장만! return 없음 (특성=feature=변수=variable 별 평균, 표준편차 계산)
        컬럼 갯수만큼 만들어져야 함
        """
        self.feature_means = np.mean(X, axis=0)
        self.feature_stds = np.std(X, axis=0)
        print(self.feature_means)
        print(self.feature_stds)
    # cf
    # np.mean(X) 전체 평균
    # np.mean(X, axis=0) 컬럼별 평균 -> array 에 넣어준다.
    # numpy axis = 0 column = pandas.df.mean axis = 0 column

    def transform(self, X):
        """X의 평균을 0, 표준편차를 1로 변환 및 리턴, fit 함수(메소드)에 있는 mean, std 를 사용한다"""
        # X의 행,열 만큼 빈 np.array(값은 들어가 있지 않음)
        dim = X.shape
        transformed = np.empty(dim)
        for row in range(dim[0]):  # row 갯수만큼 반복
            for col in range(dim[1]):  # col 갯수만큼 반복
                # 표준정규확률분포로 변환 z = (X - mu)/ sigma
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_stds[col]
        return transformed  # 목적 : 원본 X를 남겨두기 위해서 원본은 그대로 놔두고 새로운 array 를 리턴~


class MyKnnClassifier:
    def __init__(self, n_neighbors=5):  # 객체 생성
        """최근접 이웃으로 선택할 개수 저장"""
        self.k = n_neighbors

    def fit(self, X_train, y_label):  # 모델 훈련
        """레이블을 가지고 있는 데이터(point)를 저장함 - train data 의 답지를 저장함"""
        self.points = X_train  # 저장만 하기 때문에, 객체 생성할 때 init 에 저장해도 된다 즉, 굳이 필요 없는 함수 - 비슷하게 흉내내기 위해서 넣어주었다.
        self.labels = y_label

    def predict(self, X_test):  # 예측
        """테스트 세트 X_test 의 각 점들마다
         1)학습 세트에 있는 모든 점들과의 거리를 계산
         2)계산된 거리들 중에서 k개의 가장 가까운 거리를 찾는다
         3) k개의 선택된 레이블 중에서 가장 많은 것(다수결)을 예측값으로 선택한다
         X_test 개수 = 예측값 개수"""
        predicts = []  # 예측값을 저장할 리스트
        for test_pt in X_test:  # 테스트 세트에 있는 점들의 개수만큼 반복
            # 1)학습 세트에 있는 모든 점들과의 거리를 계산
            # 2)계산된 거리들 중에서 k개의 가장 가까운 거리를 찾는다 (distance)
            distances = self.distance(self.points, test_pt)  # fit 의 모든 점들(self.points) 과 검증세트의 한 점(test_pt)
            print(test_pt)
            print(distances)
            # 3) k개의 선택된 레이블 중에서 가장 많은 것(다수결)을 예측값으로 선택한다 (majority_vote)
            winner = self.majority_vote(distances)  # 함수의 리턴값이 winner로 온다
            predicts.append(winner)
        return np.array(predicts)  # np.array 변환 후 리턴

    # class MyKnnClassifier 에 필요한 함수들
    # distance : 거리 계산 메소드(클래스가 가지고 있는 함수)
    # majority_vote : 투표 메소드(클래스가 가지고 있는 함수)

    def distance(self, X, y):  # X : 점들의 집합(대문자), y : 점 하나(소문자)
        """거리 여러개를 모두 리턴하는 것 : 점 y 와 점들 X 사이의 배열을 리턴"""
        return np.sqrt(np.sum((X - y) ** 2, axis=1))  # axis=1 : 가로 축으로 더함..공책 필기 보기
        # self.distance 를 해야 predict 에서 현재 있는 distance 를 출력하게 됨

    def majority_vote(self, distances):
        """거리 순서대로 정렬된 인덱스를 찾는다 즉, index 거리 순서대로 정렬"""
        indices_by_distance = np.argsort(distances)  # 거리 순서대로 정렬 - 인덱스만 정렬, 원본 distances 건들지 않는다. (argsort - 인덱스만 정렬)
        print(indices_by_distance)

        # 가장 가까운 k개의 이웃 label 을 찾는다.
        k_nearest_neighbor = []
        for i in range(self.k):  # init 에서 저장해뒀던 k 를 찾는다.
            idx = indices_by_distance[i]  # 값이 인덱스이다. ex_[3 0 1 2]
            k_nearest_neighbor.append(self.labels[idx])
            # self.label 이 y_train 이다.(즉, label 이다) self.labels[3] = 'a' 를 append
        # or
        # for i in indices_by_distance[:self.k]:  # ex_[3 0 1] k=3일때
        #     k_nearest_neighbor.append(self.labels[i])  # self.labels[3] = 'a'
        # or (list comprehension)
        # k_nearest_neighbor = [self.labels[i] for i in indices_by_distance[:self.k]]
        print(k_nearest_neighbor)

        # 가장 많은 vote 를 얻은 레이블을 찾는다.
        vote_counts = Counter(k_nearest_neighbor)
        print(vote_counts)
        # most_common(n) : 가장 많은 빈도수 순위 n 까지의 리스트를 튜플 형태로 리턴 [()]
        # print(vote_counts.most_common(1))
        # 1(숫자) 등만 보여주기 & 몇 개인지 보여주기 [()] : list 안에 tuple - 동점 있을 수 있다. (동점이 나오면 함수 내부에서 정렬 기준을 통해 나옴)
        # print(vote_counts.most_common(1)[0])  # 가장 많은 빈도수 찾게 됨 - 홀수여도 동점 있을 수 있다. 짝수는 지양하기~
        winner, winner_count = vote_counts.most_common(1)[0]  # 리스트의 첫번째 원소만 뽑는다.-첫번째 원소 (counter의 key, value)
        return winner


if __name__ == '__main__':
    np.random.seed(1210)  # 실행할 때마다 같은 숫자가 나오도록..
    X = np.random.randint(10, size=(10, 2))
    print(X)  # 5행 2열
    y = np.array(['a', 'b', 'a', 'b', 'a'] * 2)  # labels
    print(y)  # 원소 5개인 1차원 배열 즉, 1행 5열
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # cf. z라는 변수 하나만 주면( z = train_test_split(X, y, test_size=0.2 ), 값 4개 들어있는 tuple 이 된다.
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    scaler = MyScaler()  # 객체 생성 - 생성자 = 클래스 이름, self 의 역할을 하는 객체, 생성자에 파라미터가 없다면 ()만 쓰기
    # scaler # 참조연산자 = # MyScaler()  # 생성자 호출
    scaler.fit(X_train)  # 객체가 가지고 있는 메소드 호출 [6.5 5. ]
    X_train_scaled = scaler.transform(X_train)
    print(X_train_scaled)  # 확인방법 : 다 더하면 0!
    X_test_scaled = scaler.transform(X_test)
    print(X_test_scaled)

    knn = MyKnnClassifier(n_neighbors=3)  # 객체 생성
    print('k=', knn.k)
    knn.fit(X_train_scaled, y_train)  # 공책 필기 보기
    y_pred = knn.predict(X_test_scaled)
    print(y_pred)
    print(y_pred == y_test)

# iris / wibc data 에 적용해보기~