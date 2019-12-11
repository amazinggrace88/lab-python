"""
kNN function 만들기
"""
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
    def __init__(self, n_neighbots=5):  # 객체 생성
        pass  # 해보기

    def fit(self, X_train, y_label):  # 모델 훈련
        pass

    def predict(self, X_test):  # 예측
        pass

    # class MyKnnClassifier 에 필요한 함수들
    # 거리 계산 메소드(클래스가 가지고 있는 함수)
    # 투표 메소드(클래스가 가지고 있는 함수)


if __name__ == '__main__':
    np.random.seed(1210)  # 실행할 때마다 같은 숫자가 나오도록..
    X = np.random.randint(10, size=(5, 2))
    print(X)  # 5행 2열
    y = np.array(['a', 'b', 'a', 'b', 'a'])  # labels
    print(y)  # 원소 5개인 1차원 배열 즉, 1행 5열
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # cf. z라는 변수 하나만 주면( z = train_test_split(X, y, test_size=0.2 ), 값 4개 들어있는 tuple 이 된다.
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    scaler = MyScaler()  # 객체 생성 - 생성자 클래스 이름과 동일, self 의 역할을 하는 객체, 생성자에 파라미터가 없다면 ()만 쓰기
    scaler.fit(X_train)  # 객체가 가지고 있는 메소드 호출 [6.5 5. ]
    X_train_scaled = scaler.transform(X_train)
    print(X_train_scaled)  # 확인방법 : 다 더하면 0!
    X_test_scaled = scaler.transform(X_test)
    print(X_test_scaled)
