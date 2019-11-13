'''

lab_python.utils.__init__

: 패키지에 대한 설명과 설정을 담당하는 파일
  다른 모듈에서 패키지이름을 import 했을 때, 공개할 모듈 이름들을 설정할 수 있다.

'''
# 1) for module01 - 1)
# from 패키지 import * 구문에서 공개할 모듈 이름들 리스트 설정
__all__ = ['mymath1']


# 2) for module05 - 2)
# import 패키지 구문에서 공개할 모듈 이름들 리스트 설정
from . import mymath1
from . import mymath2
# . : 같은 패키지 안의 모듈을 import해버림 -> __init__.py가 mymath1 & mymath2를 가질 수 있게 됨
# 다른 파일에서 import하면 자동으로 from . import mymath1이 호출된다. (이 파일 내에서 실행시킬 필요 없음)


# cf
# 상대경로 (like R)
# .\ : 현재 폴더의 밑
# ..\ : 현재 폴더의 위