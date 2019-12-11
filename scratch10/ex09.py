# coding=utf-8
from bs4 import BeautifulSoup

with open('web02.html', mode='r', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

    # HTML 문서 안의 모든 div 태그의 문자열 찾음
    for div in soup('div'):  # soup('div') 와 soup.find_all('div') = 동일한 기능
        print(div.text)

    # class 로 요소를 찾는 방법 (1) (2)
    # (1) Dictionary 로 찾기
    # HTML 문서 안의 "class1" 클래스 속성을 갖는 모든 요소들을 찾음
    for cls_1 in soup.find_all(attrs={'class':'class1'}):
        print(cls_1)
    # class (attribute 이름) = "class1" (attribute 값)
    # 클래스의 이름과 값을 dict 형태로 attrs= 속성에 넣어준다
    # or
    for cls_1 in soup(attrs={'class':'class1'}):
        print(cls_1)

    # (2) class_ 라는 속성으로 찾기
    # 속성으로 찾을 때에는
    # (class는 이미 파이썬에서 사용하는 예약어이기 때문에 _를 붙였다)
    # HTML 문서 안의 "class2" 클래스 속성을 갖는 모든 요소들을 찾음
    for cls_2 in soup.find_all(class_='class2'):
        print(cls_2)
    # or
    for cls_2 in soup(class_='class2'):
        print(cls_2)

    # HTML 문서 안의 "id1" 아이디 속성을 갖는 요소를 찾음
    print()
    for id_1 in soup(attrs={'id':'id1'}):
        print(id_1)
    print(soup.find(attrs={'id':'id1'}))  # 같은 결과 dict 방식
    print(soup.find(id='id1'))  # 같은 결과 keyword argument 방식
    print(soup.find(id='id1').text)  # text property 사용 가능
    print(soup(id='id1'))  # 다른 결과 - find_all 과 같이 [] 리스트 안에 묶인다.
    # print(soup(id='id1').text)  # error! why? [] 안에 묶였기 때문에..텍스트로 만들려면 인덱스 필요해~!
    print(soup(id='id1')[0].text)  # soup.find_all(id='id1')[0].text 같은 결과

    # 즉, 반복문을 사용할 때는
    # 리스트에 인덱스를 가지고 사용!
    