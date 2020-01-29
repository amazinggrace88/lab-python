'''
module04.py

mymath1과 mymath2를 모두 가져다 쓰기
'''

# step 1. import 하기
# utils 패키지 안에 있는 mymath1 과 mymath2 모듈을 사용
# import numpy as np: numpy는 파일!! np.모듈 이 나온다.
# import lab_python.utils 쓸 수 없음 why?
from lab_python.utils import mymath1
from lab_python.utils import mymath2


# step 2. 함수/변수 가져다쓰기
print(mymath1.pi)  # 모듈의 함수들을 볼 수 있다.
print(mymath2.divide(1, 2))


# 폴더 구조
'''
__init__.py에 대해서
: 패키지를 만들 때마다 만들어지는 패키지에 대한 설명 파일
__init__.py가 없으면, 패키지가 아니게 된다.

'''



