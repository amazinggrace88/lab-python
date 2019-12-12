# coding=utf-8
"""
(실습)
다음에서 "머신러닝"으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력
"""

# ***** 웹 주소 (usi, url) 구조(형식) *****
# 프로토콜://서버주소[:포트번호]/경로?쿼리스트링
# 쿼리 스트링(query string) : 클라이언트(브라우저)가 서버로 보내는 정보
#                           param 이름=param 값(주소) (param = parameter)
#                           param 이 여러개일 때는 &로 파라미터 구분


# https://www.youtube.com/watch?v=3IqEVdHrJtE
# https:// : 프로토콜
# www.youtube.com/ : ~ 첫번째 / 까지 서버의 주소
# watch? : ~ 첫번째 ?까지 경로(path) - 기능 - html 을 만들기 위한 주소
# v=3IqEVdHrJtE : ? 바로 다음부터 시작 - 쿼리스트링 - 로컬 컴퓨터에서 서버로 보내는 정보 (ex_ 동영상의 id)
#                  v = 정보 1개

# https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon
# webtoon/list.nhn : 경로
# titleId=183559 & weekday=mon : 쿼리스트링 : 정보 2개 & 로 묶음
# title(parameter 이름) = parameter 값 --> url 상에서의 파라미터!

# http://192.168.20.31:8888/
# 192.168.20.31 : 서버주소 (ip 주소로 설정해놓으심)
# 8888 : 포트번호

# 다음에서 "머신러닝"으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력
# 웹페이지에서 1 page 에 10 개씩 보여주는 것을 확인
# 10 개 나오는지 확인하는 과정을 거치자~
# 웹페이지 1 ~ 10 page 돌리는 과정
# url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'
# %EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D : UTF-8
# page 1 = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=1'
# 검색 한 후 다시 다른 페이지 갔다오면, &p=1 가 추가된다. 파라미터가 없는 경우에는 무조건 1 page 보여준다.
# page 2 = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=2' 로
# for 문으로 url 을 반복해주면 된다, 쿼리스트링에서 파라미터를 추가하기
import requests
from bs4 import BeautifulSoup

# 나의 정답
url = []
for i in range(11):
    url.append(f'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing={i}')
print(url)

for i in url:
    html = requests.get(i).text.strip()
    soup = BeautifulSoup(html, 'html5lib')
    news_link = soup.select('.coll_cont ul li a.f_link_b')
    for link in news_link:
        print(link.get('href'))


# 다음에서 임의의 검색어(키워드)로 검색한 기사 100개의 URL 주소와 기사 제목을 출력하는 함수를 작성하고 테스트
keyword = str(input('검색할 키워드 : '))
url = []
for i in range(11):
    url.append(f'https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q={keyword}&p={i}')

for i in url:
    html = requests.get(i).text.strip()
    soup = BeautifulSoup(html, 'html5lib')
    news_link = soup.select('.coll_cont ul li a.f_link_b')
    for link in news_link:
        print(link.get('href'))


# 오쌤 정답
# 다음에서 임의의 검색어(키워드)로 검색한 기사 100개의 URL 주소와 기사 제목을 출력하는 함수를 작성하고 테스트
def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD&spacing=0'
    # 검색 결과는 1 page 부터 10 page 까지
    for page in range(1, 11):
        print(f'=== Page {page} ===')
        req_params = {'q': keyword,  # 검색어(keyword)를 쿼리 스트링에 파라미터로 추가 --> &q=keyword
                      'p': page}  # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가  --> &p=page
        response = requests.get(url, params=req_params)
        html = response.text.strip()  # ~페이지에 대한 html

        soup = BeautifulSoup(html, 'html5lib')
        # ex_ coll_cont 라는 class 는 웹페이지에 여러개 있을 수 있기 때문에, 경로를 따라 들어가주는 게 좋다.
        # select***** -> find_all / find 대체할 수 있는 함수
        news_link = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_link:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)
    # 링크까지 알아내는 것은 어렵지 않은데, 신문사마다 본문을 둘러싼 class 가 다 다르므로, 본문을 가져오는 것은 어렵다. (하려면 신문사마다 다르게 해야함)


if __name__ == '__main__':
    daum_search('딥러닝')

if false:
# 다음에서 "머신러닝"으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력
#     url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0'
    for page in range(1, 11):
        print(f'=== Page {page} ===')
        # page_url = url + str(page)  # 문자열 + 문자열 - 같은 타입끼리만 + 가능
        # print(page_url)
        # 해당 패이지 URL 주소로 GET 방식 요청(request)을 보내고, (사용자의 정보를 url 주소에 실어서 보낸다)
        # 서버에서 보낸 응답(response)을 문자열로 처리
        # html = requests.get(page_url).text.strip()
        # html = requests.get(url, params={'p': page}).text.strip() or
        response = requests.get(url, params={'p': page})  # query string 에 파라미터 추가를 자동으로 넣어 줌
        html = response.text.strip()
        # request.get(url, params={key:value}) : param 의 내용을 url 의 query string 의 파라미터로 추가해줌. 즉,  &key=parameter 를 url 에 추가함
        # Soup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont ul li a.f_link_b')  # 1 page 10개
        for link in news_link:  # 10개 중 1개
            # HTML element 의 href 속성 (attribute) 값을 읽음(.get)
            news_url = link.get('href')
            # HTML element 가 가지고 있는 content 문자열을 읽음
            news_title = link.text
            print(news_url, news_title)
            # 파일로 저장하기 ~ 만들어보기 (숙제)



