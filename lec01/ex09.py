"""
dict (dictionary) : key-value의 쌍으로 이루어진 데이터들을 저장하는 사전식 데이터타입
"""

person = {'name': 'ohsam', 'age': 16, 'height': 170.5}  # 중괄호 key:value - 1개의 데이터타입
print(person)
print(type(person))

# dict 의 데이터 참조 - key 이용
# print(person[0]) : dict 은 인덱스 없음
print(person['name'])
print(person['age'])

# dict의 key를 찾아주는 함수 .keys()
print(person.keys())
# dict의 value를 찾아주는 함수 .values()
print(person.values())
# dict의 (key, value)를 찾아주는 함수 .items() : (각각의 원소들은 튜플)
print(person.items())
# for문에서 사용될 것

students = {1:'강다혜', 2:'김수인', 3:'김영광', 10:'안도연'}
print(students)
print(students[1])  # index 연산자같지만, 우리가 사실은 key 를 지정한 것! => 우리가 index 를 이름짓는다고 생각할 수 있다.

# dict 에 값 추가
students[4] = '김재성'
print(students)  # 제일 마지막에 추가됨

# dict 의 값 변경
students[4] = '홍길동'
print(students)

# dict 의 값 삭제 - pop(key) 메소드 사용 ---> **
students.pop(4)  # pop - 꺼내다
print(students)

# dict 의 활용
book = {
    'title':'python programming manual',
    'authors' : ['ohsam', 'jennifer', 'paul'],
    'company' : 'gilbut',
    'isbn' : 97911
}
print(book)
print(book['authors'])
print(book['authors'][0])
print(book['company'])


