# coding=utf-8
"""
daum 뉴스 web crawling
머신러닝 (한글로) 검색 결과
https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0
beautifulsoup official documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
"""
import requests
from bs4 import BeautifulSoup

# 사이트(웹 서버)로 요청(request)의 종류
# 1) get 방식 (기본값)
# 1)-1 search.daum.net/ 서버이름 에 요청을 보낸다.(검색어 머신러닝을 검색하겠다~)
# https://search.daum.net/(서버이름) search?w=tot (컴퓨터에서 서버로 전송되는 정보의 단위1) & q=%EC%A0%95%EA%B2%BD%EC%A7%84&DA (정보의 단위2) =NTB
# 1)-2 검색어가 url 주소와 함께 서버로 같이 전송된다.
# 1)-3 서버에서 응답된 결과를 변수에 저장하고, 리턴한다.
# 2) post 방식
# 2)-1 (ex 로그인) 정보를 감춰서 요청을 보낸다.

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'
# 사이트(웹 서버)로 요청(request)을 보냄
html = requests.get(url).text.strip()
# 요청의 결과(응답 response)을 html 이라는 변수에 저장
print(html[0:100])
# 문자열 인덱싱 가능! 앞부터 100까지 보여주라~
# .text.strip() 안써도 되! text 만 보이게 / strip() 앞뒤 공백 빼게

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
soup = BeautifulSoup(html, 'html5lib')
for link in soup('a'):
    print(link.get('href'))
# 관심 있는 링크(뉴스 링크들)만 찾을 수 있는 방법 찾기
print()
# 개발자도구에서 코드에 더블클릭 - coll_cont
# class = "coll_cont" 는 사이트 내 여러개 있을 수 있으므로 확인해보자
# id 를 여러개 사용하는 경우도 있으므로, 장담할 수 없음
# 방법 1 : class 로 찾기 - 같은 클래스 이름이 있는 모든 HTML 요소들을 찾음
div_coll_cont = soup.find_all(class_='coll_cont')  # soup.find_all(attrs={'class': 'coll_cont'})
print(len(div_coll_cont))  # div_coll_cont 가 4 개가 나옴 - 개발자도구에서 우리가 찾는 coll_cont 가 몇번째인지 찾기 (ctrl+f) : 다른 부분들 찾기 (enter)

print()
# HTML 하위 요소(sub/child element)를 찾는 방법:
# 1) parent_selector >(꺽쇠) child_selector : 바로 아랫쪽에 있는 element 를 찾아갈 수 있는 방법
# ex_ TAG : div > ul > li
# class, id 도 똑같이 쓸 수 있다.
# ex_ CLASS/ID : .coll_cont > #clusterResultUL > .fst
# 문제점 : 너무 많이 써야 해서 a 로 가기 힘들다 (하나씩 밑으로 내려가니까)

# 2) ancestor_selector(조상 선택자) descendant_selector(자손 선택자) : 자손들을 모두 찾아가겠다는 의미..공백을 주면 된다.
# ex_ div li (div 의 자손 요소들 중에 li 들)
# ex_ .coll_cont .fst (클래스 .coll_cont 요소의 자손 요소들 중 클래스가 .fst 인 요소들)

# <결론>
# soup.select(css_selector) : soup 객체에서 CSS 선택자로 요소들을 찾는 방법
news_link = soup.select('.coll_cont ul li a.f_link_b')  # webpage 보고 복습 !
for link in news_link:
    print(link.get('href'))


# id 로만 찾으면 안되는 이유!
print()
for link in soup('a', attrs={'id':'clusterresultUL'}):
    print(link.get('href'))
# id = clusterresultUL 이 어디 있을 지 모르기 때문에 범주를 정해서 down 시켜 id 를 범주화해야 한다.
