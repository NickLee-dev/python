# path : crawling\\crawling l
# url 을 키보드로 입력받아서 크롤링 테스트

import urllib.request as rq, bs4

url=input('접속할 url 입력 : ')
# url은 웹상의 자원까지의 경로를 의미함
# 프로토콜://도메인명/폴더명/파일명?이름=값&이름=값
# 쿼리스트링(queryString) : 서버측의 대상 파일(컨트롤러)로 전달되는 값들을 표현한 것
#                           ?이름=값&이름=값
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84

# 1. url로 대상 웹페이지에 접속
web_page = rq.urlopen(url)
# 2. 접속한 페이지 소스를 읽어옴 > 출력확인(인코딩 상태임)
#html_code = web_page.read()
# 네이버 페이지 출력 테스트
#print(html_code)
# 3. 읽어온 인코딩된 소스를 html 태그 구문으로 바꿈
decoding_code = bs4.BeautifulSoup(web_page, 'html.parser') # > decoding 처리
print(decoding_code)