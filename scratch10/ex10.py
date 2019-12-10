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

# 접속할 사이터(웹 서버) 주소
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
    pass
    # print(link.get('href'))
# 관심 있는 링크(뉴스 링크들)만 찾을 수 있는 방법 찾기
for link in soup('a', attrs={'class':'f_link_b'}):
    print(link.get('href'))

