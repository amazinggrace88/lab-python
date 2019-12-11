# coding=utf-8
import os
import icrawler.builtin import GoogleImageCrawler

# 이미지 저장 경로
save_dir = os.path.join()  # mac 은 뭐지?
# GoogleImageCrawler 객체 생성
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
filters = {'size':'large'}
# 검색 필터링(google-도구) 조건 만들기
google_crawler.crawl(keyword='펭수', filters=filters, max_num=1000)


# ex11
def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD&spacing=0'
    # 검색 결과는 1 page 부터 10 page 까지
    for page in range(1, 11):
        print(f'==={page}Page===')
        r_params = {'q': keyword, 'p':page}
        response = requests.get(url, params=r_params)
        html = response.text.strip()
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_link:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)