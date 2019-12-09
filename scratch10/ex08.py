"""
파이썬으로 HTML 문서 분석:
설치해야 할 패키지
- pip install requests (순서1)
HTTP 요청(requests)을 보내고 서버로부터 응답(response)을 받는 기능을 담당하는 패키지
- pip install html5lib (순서2)
실제로 HTML 문서를 파싱(parsing)하여 DOM tree 안에 elements 를 찾아주는 패키지
- pip install BeautifulSoup (순서3)
html5lib 을 이용하여 HTML 요소들을 분석하는 패키지
1) with ~ as 구문 이용 : html 파일일 때!
2) request : 웹에 접근할 때(요청할 때)
"""

from bs4 import BeautifulSoup  # 먼저 cmd 에 설치해야 import 가능

# 파일 열기 (html 파일일 때!)
with open('web01.html', mode='r', encoding='UTF-8') as f:
    # HTML 문서와 HTML parser(분석기)를 파라미터에 전달해서, BeautifulSoup 객체 생성
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)  # html5lib 을 사용해서 BeautifulSoup 이 분석을 다 해놓은 상태가 출력된다.

    # HTML 요소들 중에서 tag 이름으로 h1, h2 요소를 찾음 (방법 (1) (2))
    # (1) soup.find('태그이름')
    h1 = soup.find('h1')
    print(h1)  # element 를 찾았다!
    print(h1.text)  # h1 element 안의 다른 html tag 들어가 있어서 - text 사용
    # (2) soup.태그이름
    h2 = soup.h2
    print(h2)
    print(h2.string)  # string 사용 - 문자열 찾아줌 (text 도 사용 가능)

    # paragraph 요소 안의 문자열을 찾아서 출력
    p1 = soup.find('p')  # (1)
    print(p1)
    print(p1.text)  # (1).text
    p2 = soup.p  # (2)
    print(soup.p.text)  # (2).text - html 태그는 생략되고 문자열만 남아있음 ( <p>여기는 <strong>paragraph</strong>입니다.</p>)

    # find
    # : for 문처럼 찾으면 바로 리턴 (처음부터 분석 하다가 가장 처음에 만나는 요소를 리턴)
    print(soup.find('a'))  # a (anchor tag) 를 하나 밖에 찾을 수 없다.
    print(soup.a)  # 같은 결과

    # find_all
    # : HTML 문서 전체에서 찾은 모든 해당 요소들의 리스트를 리턴함.
    # soup('태그이름')과 같다.
    print(soup.find_all('a'))
    print(soup('a'))  # 같은 결과 : soup('태그이름')은 soup.find_all('태그이름')과 동일
    print(soup('a')[0])  # 0 번째 인덱스

    # .get('attribute_이름')
    # : HTML 문서의 'a'라는 element 에서 attribute_이름을 가지고 있는 값을 구한다.
    # HTML 문서의 모든 링크에서 링크 주소(href)만 추출해서 출력 (for in 구문)
    for link in soup('a'):
        # HTML_element.get('attr 이름') - attr 의 값을 구함. - 링크만 리턴
        print(link.get('href'))
