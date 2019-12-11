# coding=utf-8
"""
한겨례 신문사 페이지에서 특정 검색어 검색 결과 50개의
URL 주소, 기사 제목, 기사 내용을 출력 -> 파일에 저장
"""

# 한겨례 신문사 웹크롤링 (신문사 하나이므로, 웹페이지의 형식이 모두 같다. 즉, 기사 내용까지를 웹크롤링 할 수 있다) -> 출력 및 text file 로 저장하기
import requests
from bs4 import BeautifulSoup

url = 'http://search.hani.co.kr/Search?command=query&keyword=%EB%A8%B8%EC%8B%A0+%EB%9F%AC%EB%8B%9D&sort=d&period=all&media=news'


def hani_search(keyword):
    url = 'http://search.hani.co.kr/Search?command=query&media=news&sort=d&period=all'  # 파라미터 값 없는 거 지워도 됨! / 날짜 지워도 됨! (가변이므로)
    for page in range(5):
        print(f'=== Page {page} ===')
        req_params = {'keyword': keyword,
                      'pageseq': page}
        # get : 서버로 요청을 보낸 후, 응답을 받음.
        response = requests.get(url, params=req_params)
        # 응답에서 HTML 문서를 추출
        html = response.text.strip()  # text 는 문서 추출, strip() 은 문자열의 앞,뒤 공백만 자르고 중간 공백을 없애주지는 않는다.
        # HTML 문서를 분석하기 위한 BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select(' ul.search-result-list  li dl dt a')  # 같은 결과 : [] 로 출력됨  /  # 시작점은 자기가 정해도 되~
        for link in news_link:
            news_url = link.get('href')  # 검색 결과 뉴스 링크 URL
            news_title = link.text  # 검색 결과 뉴스 제목
            print(news_url, news_title)
            hani_article(news_url)  # 검색 결과 뉴스 링크를 새로 열기 (링크 주소 클릭)


def hani_article(url):
    # 기사 하나 열고 다시 f12
    response = requests.get(url)
    html = response.text.strip()
    # print(html[:500])
    soup = BeautifulSoup(html, 'html5lib')
    # article = soup.find('div', class_='text').text.strip()  # 제일 처음 만난 클래스를 리턴한다. (미리 내가 찾는 클래스가 제일 처음 만나는 클래스인지 확인)
    article = soup.select('div.article-text div.text')[0].text.strip()  # 리턴 타입 list [] --> [0]으로 1개 있는 원소를 빼낸다.
    print(article)
    # 공백의 이유 : 중간에 태그 들어간 것 / 이미지 등 모두 공백으로 처리되어서.. -> 공백 2줄 이상이면 제거하는 함수를 만들자.

    # with ~ as 구문 + mode='w'으로 파일 저장하기.
    # 다른 사이트로 연습하기.


if __name__ == '__main__':
    hani_search('머신러닝')


