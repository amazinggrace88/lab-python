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

# 2) from 모듈이름 import 기능(변수, 함수, 클래스 이름) : 파일 안 기능을 가져옴
# 2-1) from 모듈이름 import 기능(변수, 함수, 클래스 이름) : 파일 안 기능을 가져옴 (권장)
from math import pi
print(pi) # print(math.pi)가 아니다. why? math 파일로부터 pi 라는 변수만을 가져왔기 때문
from math import sqrt
print(sqrt(2))

# 2-2) math 라는 모듈 안의 모든 기능을 가져옴 (python 공식 문서에서 권하지 않음 why? 문제점 존재 : pi라는 변수를 설정하면 변수 pi가 바뀌어버림)
from math import * # 모듈이 가지고 있는 모든 변수를 가지고 온다.
print(pi)
pi = 6
print(sin(pi/2)) # 변수 6으로 바뀌었기 때문에, pi = 3.14가 아니게 된다.(즉, math 파일의 pi 변수가 아니게 된다)
