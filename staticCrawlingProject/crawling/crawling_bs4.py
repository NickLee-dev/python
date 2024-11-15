# path : crawling\\crawling_bs4.py
# module : crawling.crawling_bs4
# bs4 (BeautifulSoup4) 를 이용한 정적 웹 크롤링 테스트 1

# 패키지 설치 : pip install beautifulsoup4
#import bs4 # d웹 페이지의 html 태그들을 분석하는 모듈
#mport urllib.requst # 웹상의 html 문서를 가져오는 모듈
import urllib.request, bs4 # 한번에 임포트

# 1. url로 대상 웹페이지에 접속
web_page = urllib.request.urlopen('https://www.naver.com')
# 2. 접속한 페이지 소스를 읽어옴 > 출력확인(인코딩 상태임)
#html_code = web_page.read()
# 네이버 페이지 출력 테스트
#print(html_code)
# 3. 읽어온 인코딩된 소스를 html 태그 구문으로 바꿈
decoding_code = bs4.BeautifulSoup(web_page, 'html.parser') # > decoding 처리
print(decoding_code)