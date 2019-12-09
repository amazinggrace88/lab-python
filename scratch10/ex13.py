'''
# 이미지 웹크롤링
icrawler 패키지를 사용해서, Google 이미지 검색 결과의 이미지들을 다운로드
# pip install icrawler cmd에 설치 후 settings -> python interpreter 에서 설치 되어있는지 확인하기
'''
import os
from icrawler.builtin import GoogleImageCrawler

# 이미지 저장 경로
save_dir = os.path.join('C:' + os.sep, 'dev', 'images_for_pangsoo')  # (window만)
# GoogleImageCrawler 객체 생성
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})  # storage=이미지 저장 경로
# 검색 필터링(google - 도구) 조건 만들기
filters = {
    'size': 'large',
    # 'license': 'noncommercial, modify',  # noncommercial비상업적 용도 재사용, modify수정가능 --> icrawler 를 구글에 검색해서 상세내역 보기
}
# 이미지 다운로드
google_crawler.crawl(keyword='펭수', filters=filters, max_num=1000)
# 이미지 저장 경로로 파일들이 들어가게 된다. /  Exception caught when downloading file 실패
# 다운로드 받으면서 파일 이름들이 순서대로 00001, 00002,,로 들어간다.
# https://icrawler.readthedocs.io/en/latest/builtin.html#search-engine-crawlers GoogleImageCrawler 문서
# threads => 컴퓨터의 코어, 컴퓨터의 용량을 얼마나 많이 사용해서 컴퓨터의 코어를 돌리는지!

# https://scrapy.org/ ==> 문서 보고 이용하기 꼭 사용해보기 + beautifulsoup 이랑 비교하기~