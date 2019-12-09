# coding=utf-8
'''
모듈 (module) : 파이썬 파일(.py)
- 쉽게 말해 파이썬 파일
- 변수, 함수, 클래스들이 정의된 스크립트 파일

패키지 (package) : 파이썬 모듈들을 찾기 쉽게, 관련된 기능들끼리 구분하여 모듈을 저장한 폴더
- 패키지 안에 모듈을 넣어둔다.
- 패키지를 다운로드 받는다 = (ex_ numpy 라는) 폴더가 생기고, 폴더 밑에 여러개 파일이 생긴다.
- import = 외부 모듈을 다운로드

기본 패키지/모듈 이외의 기능들을 사용할 때 import 구문을 사용함
< 사용법 3가지 >
1) import 모듈이름 : 파일를 가져옴
2) from 모듈이름 import 기능(변수, 함수, 클래스 이름) : 파일 안 기능을 가져옴
3) from 패키지이름 import 모듈이름 : 폴더 안 파일을 가져옴
'''


# 1) import 모듈이름 : 파일를 가져옴
# 파이썬은 여러가지 수학 함수들과 상수들을 정의한 math 모듈이 있음
import math  # math.py 파일안에 정의된 함수들과 상수들을 사용할 수 있음

# import 문 실행 과정
# math.py 파일을 열어서 파일 안의 함수들을 모두 실행함 -> heap 에 모두 저장함(주소는 math.~)
# math라는 변수 생성 -> math. : 참조 연산자
# math. ~ -> math 주소에 저장되어 있는 기능(~)을 찾아가서 실행한다
# 여러번 실행해도 처음 한번 파일을 오픈해서 해당 내용을 모두 실행한 후 다음 import 시 안에 있는 것을 사용한다.

# 모듈에 정의된 상수(변수) 사용
print(math.pi) 
# 모듈에 정의된 함수 사용
print(math.sqrt(2))

# 패키지(디렉토리) import
import numpy

# import ..(모듈, 패키지) as 별명
import numpy as np  # 패키지 numpy
from math import pi as PI  # 의미 : math에서 pi를 가져와서 PI라고 부르겠다

# chapter 6장 읽기