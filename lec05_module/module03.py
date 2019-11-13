'''
module03.py
: utils 패키지(폴더, 디렉토리) 안에 있는 mymath1 모듈(파이썬 파일)의 기능(변수,함수 등)을 사용하자

------방법------
1) import 모듈이름
2) from 모듈이름 import 변수/함수 etc
3) from 패키지이름 import 모듈이름
---------------
'''

# 전체 모듈 : 어떤 폴더 밑에 어떤 파일 이름으로 있는지 **경로를 포함하여** 모두 작성해야 함
# import mymath1 # no! 파일이 패키지 안에 들어있기 때문에

# 1)
import lab_python.utils.mymath1
# 의미 : utils라는 폴더 밑에 mymath1이 있다. # C:\dev\lab_python\lab_python\utils
# 과정 : import시 모든 함수들의 프린트문이 나온다(한번은 모두 실행한다)

# 2)
# from lab_python.utils.mymath1 import pi
# 모듈 전체를 import하던, 함수 하나만 import하던 작동과정은 똑같다 (메모리 줄어들지 않고 똑같다)
# module03에 if 문을 사용하여 모든 함수들의 프린트문이 나오는 것을 방지

# 1) 함수 실행
print('pi = ', lab_python.utils.mymath1.pi)
# 2) print('pi = ', pi) # pi라는 이름을 가지고 왔으므로 .(참조연산자)는 필요가 없다
