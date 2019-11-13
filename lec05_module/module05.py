'''
module05.py
: import by __init__.py
'''


# 방법 1)
# from lab_python.utils import *
# print(mymath1.pi)
# from 패키지 import *에서 임포트되는 모듈 이름들은
# 패키지 폴더의 __init__.py 파일의 __all__변수에 설정된 모듈이름들이다.


# 방법 2)
# import 패키지 구문을 사용하면
# 패키지 폴더의 __init__.py 파일에서 미리 import한 모듈 이름들을 방법 2처럼 사용가능
import lab_python.utils
print(lab_python.utils.mymath1.pi)