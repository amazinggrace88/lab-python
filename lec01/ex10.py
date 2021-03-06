"""
set{집합}: 저장되는 순서가 중요하지 않고, 같은 값이 중복 저장되지 않는 데이터 타입 (수학 - 집합과 동일한 개념)
"""

s1 = {1, 2, 3, 3, 2, 1}  # dict, set 만들 때 : 중괄호 사용 <-> set : value 만 넣는다.
print(s1)  # 중복되는 값들은 1개로 취급한다.

s2 = {4, 3, 2}
print(s2)  # 정렬된 form 으로 출력함 : 즉, input 순서가 중요하지 않다.

# 집합 연산 : 합집합, 교집합, 차집합
print(s1 | s2)  # 합집합
print(s1 & s2)  # 교집합
print(s1 - s2)  # 차집합

# 집합도 변경이 가능하다. (<-> tuple 변경 불가능)
# 집합의 원소 추가
s1.add(100)
print(s1)

# 집합의 원소 삭제
s1.remove(3)  # 삭제하고 싶은 element 넣기
print(s1)

s1.add(1)
s1.remove(1)
print(s1)


