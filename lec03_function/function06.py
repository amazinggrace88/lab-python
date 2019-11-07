"""
variable - length keyword argument:
함수 정의할 때 파라미터 이름 앞에 **를 사용
함수 내부에서는 dict 처럼 취급함.
"""

# example 1
def test(**kargs):
    print(kargs)
    for key in kargs:
        print(key, kargs[key])

test() # {} 사전/집합이 출력됨
test(name='ohsam', age=16) #파라미터 이름 = 값 자신이 직접 정할 수 있음. {'name': 'ohsam', 'age': 16} python 의 특징
