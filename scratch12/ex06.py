"""
sort 알고리즘 확인

Iterable : for - in 구문에서 사용할 수 있는 타입들
list, tuple, set, dict, numpy.ndarray, pandas.DataFrame ... generator(?)
for x in list:
    ..  처럼 쓸 수 있다.

정렬할 수 있는 타입 : 숫자, 문자열
(문자열도 숫자로 변환하여 비교한다)
"""
a = [1, 3, 0, 9, -1]

# sorted 함수
# -> 리턴 타입 리스트
result = sorted(a, key=lambda x: abs(x), reverse=True)
# result = sorted(a, key=lambda x: -abs(x))  # 오쌤이 하신 방법! (오름차순 -> 내림차순)
# d(__iterable: Iterable[_T],
#            *, -------------> 그 다음에는 반드시 keyword argument 방식으로 써라~ (*는 어찌할 수 없음)
#            key: Optional[(_T) -> Any] = ...,
#            reverse: bool = ...) -> List[_T]
# reverse=True -> 내림차순 true! 거꾸로 = true / 기본값 reverse=False
print(f'a={a}, result={result}')  # a 는 바뀌지 않고, 결과값인 result 가 새로 생성됨

# .sort 메소드
result = a.sort()
print(f'a={a}, result={result}')  # a 는 바뀌어 있고, result 없음
# def sort(self,
#          *,
#          key: Optional[(_T) -> Any] = ...,
#          reverse: bool = ...) -> None  ----> return 이 None 이다! (즉, result 가 없다)
# Stable sort *IN PLACE*. ---> 그 자리에서 sort 를 해버린다 (즉, 원본 데이터를 바꾼다!)


# 문자열 : 크기를 비교할 수 있는 타입 by UTF-8 코드값
b = ['cat', 'bb', 'dogs', 'apple']
result = sorted(b, key=lambda x: len(x))
print(f'b={b}, result={result}')
# 첫번째 글자끼리 비교/ 두번째 글자 비교/ 세번째 글자 비교/.. A가 제일 작고, 그다음 B, C..
# lambda x: len(x) ----> 기준 key : len(x)


# dict : key, value 의 쌍
c = {'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}
# sorted 와 for in 구문은 같다.
for x in c:
    print(x)  # key 만 출력함(기본값)
result = sorted(c, key=lambda x: len(x))  # 정렬기준 key, lambda x 의 x 는 key 이다~
print(f'c={c}, result={result}')  # result 는 리스트 형태, 리스트 안의 문자열은 key!
result = sorted(c.values(), key=lambda x: abs(x))  # dict 의 value 들만 정렬한 리스트
print(f'c={c}, result={result}')
# result = sorted(c.items(), key=lambda x: len(x))  # (key, value) 의 len(x) -> 튜플의 갯수인 2 이다.
result = sorted(c.items(), key=lambda x: len(x[0]))  # why? x[0] 가 key 이므로!
print(f'c={c}, result={result}')  # 정렬의 기준 : key, lambda x 의 x는 (key, value) 이다~


# 결론 ex05
result = sorted(c.items(), key=lambda x: x[1])  # value 순서대로(오름차순대로)
print(f'c={c}, result={result}')


# min 과 max 에도 key 가 있다! why? class 정렬할 경우가 있기 때문
# min()
# def min(__iterable: Iterable[_T],
#         *,
#         key: (_T) -> Any = ...,---> key 값에 lambda 주면 된다~
#         default: _VT) -> Union[_T, _VT]


# class type 정렬
# why? class 의 object 들의 정렬기준이 많다 (이름순, 나이순, 키순..)
class Person:
    def __init__(self, name: str, age: int):  # : str 힌트!
        self.name = name
        self.age = age
        # 멤버변수 : 클래스 안에서 클래스가 가지고 있는 변수들 f(field), ~ property(특성, 속성), ~ member variable(멤버변수) 자세히 정리하기!

    def __repr__(self):
        return f'Person(이름 : {self.name}, 나이 : {self.age})'


p1 = Person('이지수', 10)  # 생성자 호출
p2 = Person('심진섭', 20)
p3 = Person('조성우', 30)
persons = [p1, p2, p3]
print(persons)


# result = sorted(persons)
# print(result)
# TypeError: '<' not supported between instances of 'Person' and 'Person' 인스턴스가 크다작다 비교불가
result = sorted(persons, key=lambda x: x.name)  # x.name 멤버변수 넣는 과정 -> (참조변수) x (참조 연산자) . (멤버변수) name
print(result)
result = sorted(persons, key=lambda x: x.age)  # x.age 멤버변수 넣는 과정 -> (참조변수) x (참조 연산자) . (멤버변수) age
print(result)
