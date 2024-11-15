# path : crawling\\crawling3_bs4.py
# module : crawling.crawling3_bs4
# 네이버 개봉영화순위 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4

web_page = urllib.request.urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&oquery=%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94%EC%88%9C%EC%9D%B4&tqi=iy1HRdqo1Sossh4ViSossssstbC-439679")
decoding_code = bs4.BeautifulSoup(web_page, 'html.parser')
# print(decoding_code)

# 개봉영화 정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앨리먼트만 리턴함
# find(찾을 텍스트가 기록된 태그명, 태그속성_='속성값')
# find(태그속성_='속성')
# find(찾을 태그명)

# 영화 제목들만 추출 : div.title_box > strong 태그 안에 제목 확인
# data_box = decoding_code.find('div', class_='title_box')
# print(data_box) # 첫번째 항목 한개만 추출된 것을 확인함
# movie_title = data_box.find('strong', class_='name')
# print(movie_title)

# 대상 태그 앨리먼트 여러개 추출을 원한다면 : find_all() 사용
# movie_list = decoding_code.find_all('strong',{'class':'name'})
# print(movie_list)
# print(len(movie_list))

# 영화 제목만 추출하기
# for idx in range(len(movie_list)):
#     title = movie_list[idx].text  # strong.name 태그 안의 영화제목글자 추출
#     print(title)

# 영화제목, 관객수 추출
movie_list = list()  # 찾은 값을 저장할 공간
#movie_div = decoding_code.find_all('div',{'class':'title_box'}) # 값 추출하기
# 영화순위(rank), 상세정보링크 주소(link), 이미지 경로 정보(img_path), 영화제목, 관객수
# 영화순위(rank)
# 전체리스트 가져오기
#movie_box = decoding_code.find("ul",class_="_panel")
#movie_li = movie_box.find_all("li")
#print(movie_li)
#print(movie_box)

movie_li = decoding_code.find("ul",class_="_panel").find_all("li")

for idx in range(len(movie_li)):
    movie = dict() # 자료 저장할 딕셔너리 만들기
    movie['rank'] = int(movie_li[idx].find('span',{'class':'this_text'}).text)
    movie['link'] = movie_li[idx].find('a').attrs['href']
    movie['img_path'] = movie_li[idx].find('img').attrs['src']
    movie['title'] = movie_li[idx].find('strong',{'class':'name'}).text  # 값 추출하여 저장
    movie['persons'] = movie_li[idx].find('span',{'class':'sub_text'}).text  # 겂 추출하여 저장
    movie_list.append(movie) # 리스트에 dict객체 저장

print(movie_list)

# 오라클 db에 movie 테이블에 기록 저장 처리
import cx_Oracle, os
import common.dbConnectTemplate as dbtemp

# 2. db드라이브 등록 및 연결
dbtemp.oracle_init()
conn = dbtemp.connect()
# 3. insert 처리
query = "insert into c##testweb.movie values (:1,:2,:3,:4,:5)"

for movie in movie_list:
    tp_value = (movie['rank'], movie['title'], movie['persons'],movie['link'],movie['img_path'])
    cursor = conn.cursor()
    try:
        cursor.execute(query, tp_value)
        dbtemp.commit(conn)
    except Exception as e:
        print(e)
        dbtemp.rollback(conn)
    finally:
        cursor.close()

# for end -------------------------------------------
dbtemp.close(conn)